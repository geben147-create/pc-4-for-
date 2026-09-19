#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
문장별 TTS WAV 를 읽어 장면 타임라인을 계산한다.

동기화 방식 ③ — 의미 장면 고정 + 문장 끝/핵심 단어 병용
  · 의미 장면(SC01~SC24)은 대본 논리 단위이므로 절대 쪼개지지 않는다
  · 장면 안의 샷 전환은 문장 끝에 붙인다 (호흡 유지)
  · 리빌 단어는 문장 끝을 기다리지 않고 그 단어 발음 순간에 컷한다

표준 라이브러리만 사용한다. pip 설치 불필요.

사용법
  python build_timeline.py --lang ko
  python build_timeline.py --lang ja        # 일본어판, 장면 ID 동일

입력
  sentences_<lang>.tsv
  01_audio/<lang>/S001.wav ... S0NN.wav

출력
  out/timeline_<lang>.json    장면/샷 타임라인
  out/subtitles_<lang>.srt    자막
  out/edit_<lang>.csv         편집 프로그램용
  out/master_<lang>.wav       문장 연결 마스터 (--concat 지정 시)
"""
import argparse, csv, json, os, sys, wave

# ──────────────────────────────────────────────────────────────
# 편집 파라미터 — 여기가 결과의 질을 결정한다
# ──────────────────────────────────────────────────────────────
GAP_MS                 = 180   # 문장 사이 간격. Qwen3 POSTPROCESS 의 0.18초와 맞춤
CUT_OFFSET_SENTENCE_MS = 120   # 문장 끝 +120ms 에 컷.
                               # 문장 끝에 정확히 붙이면 급하게 느껴진다.
                               # 숨 쉬는 지점에 컷이 걸려야 자연스럽다.
CUT_OFFSET_REVEAL_MS   = -80   # 리빌 단어 발음 시작보다 80ms 먼저 컷.
                               # 그림이 먼저 있고 말이 따라와야 '공개'가 된다.
                               # 말이 먼저 나오고 그림이 늦으면 그냥 '설명'이 된다.
MIN_SHOT_S             = 2.2   # 이보다 짧은 샷은 앞 샷에 병합. 컷이 잦으면 피로하다
MAX_SHOT_S             = 6.0   # 이보다 길면 같은 그림 안에서 카메라 무브로 버틴다


def wav_duration_s(path):
    with wave.open(path, 'rb') as w:
        return w.getnframes() / float(w.getframerate())


def srt_time(t):
    ms = int(round(t * 1000))
    h, ms = divmod(ms, 3600000)
    m, ms = divmod(ms, 60000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def load_sentences(lang):
    path = f"sentences_{lang}.tsv"
    if not os.path.exists(path):
        sys.exit(f"[중단] {path} 가 없습니다.")
    with open(path, encoding='utf-8') as f:
        return list(csv.DictReader(f, delimiter='\t'))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--lang', default='ko')
    ap.add_argument('--audio-dir', default=None)
    ap.add_argument('--out-dir', default='out')
    ap.add_argument('--concat', action='store_true', help='마스터 WAV 도 생성')
    args = ap.parse_args()

    lang = args.lang
    audio_dir = args.audio_dir or os.path.join('01_audio', lang)
    os.makedirs(args.out_dir, exist_ok=True)

    rows = load_sentences(lang)

    # ── 1. 문장 길이 측정 → 절대 시각 확정 ────────────────────
    t = 0.0
    missing = []
    for r in rows:
        wav = os.path.join(audio_dir, f"{r['sent_id']}.wav")
        if not os.path.exists(wav):
            missing.append(wav); continue
        dur = wav_duration_s(wav)
        r['_start'] = t
        r['_dur']   = dur
        r['_end']   = t + dur
        t += dur + GAP_MS / 1000.0

    if missing:
        sys.exit(f"[중단] WAV {len(missing)}개 없음. 첫 항목: {missing[0]}\n"
                 f"       파일명은 반드시 S001.wav 형식이어야 합니다.")

    total = t - GAP_MS / 1000.0

    # ── 2. 컷 포인트 산출 (방식 ③) ────────────────────────────
    cuts = []
    for r in rows:
        if r['cut_type'] == 'reveal' and r['reveal_word']:
            # 리빌 단어가 문장 안 어디쯤에서 발음되는지 글자 비율로 추정
            txt = r['text_spoken']
            pos = txt.find(r['reveal_word'])
            ratio = (pos / len(txt)) if pos >= 0 and len(txt) else 0.0
            at = r['_start'] + r['_dur'] * ratio + CUT_OFFSET_REVEAL_MS / 1000.0
            cuts.append({'at': max(0.0, at), 'kind': 'reveal',
                         'sent_id': r['sent_id'], 'scene_id': r['scene_id'],
                         'scene_label': r['scene_label'], 'note': r['reveal_word']})
        else:
            at = r['_end'] + CUT_OFFSET_SENTENCE_MS / 1000.0
            cuts.append({'at': at, 'kind': 'sentence',
                         'sent_id': r['sent_id'], 'scene_id': r['scene_id'],
                         'scene_label': r['scene_label'], 'note': ''})

    cuts.sort(key=lambda c: c['at'])

    # ── 3. 샷으로 변환 + 최소 길이 병합 ───────────────────────
    shots, start = [], 0.0
    for c in cuts:
        end = c['at']
        # 짧은 샷은 앞 샷에 흡수하되, 그 결과가 MAX_SHOT_S 를 넘기면 흡수하지 않는다.
        # 흡수만 반복하면 짧은 문장이 몰린 구간(특히 오프닝 훅)이
        # 통째로 한 장의 정지 화면이 되어 버린다. 훅에서 가장 치명적이다.
        absorb = (end - start < MIN_SHOT_S
                  and shots
                  and c['kind'] != 'reveal'
                  and (end - shots[-1]['start']) <= MAX_SHOT_S)
        if absorb:
            shots[-1]['end'] = end
            shots[-1]['merged'] += 1
        else:
            shots.append({'start': start, 'end': end, 'kind': c['kind'],
                          'scene_id': c['scene_id'], 'scene_label': c['scene_label'],
                          'sent_id': c['sent_id'], 'note': c['note'], 'merged': 0})
        start = shots[-1]['end']

    if shots:
        shots[-1]['end'] = total

    for i, s in enumerate(shots, 1):
        s['shot_id']  = f"SH{i:03d}"
        s['duration'] = round(s['end'] - s['start'], 3)
        s['start']    = round(s['start'], 3)
        s['end']      = round(s['end'], 3)
        s['over_max'] = s['duration'] > MAX_SHOT_S

    # ── 4. 출력 ───────────────────────────────────────────────
    timeline = {
        'lang': lang,
        'total_duration_s': round(total, 3),
        'sentence_count': len(rows),
        'shot_count': len(shots),
        'params': {'GAP_MS': GAP_MS,
                   'CUT_OFFSET_SENTENCE_MS': CUT_OFFSET_SENTENCE_MS,
                   'CUT_OFFSET_REVEAL_MS': CUT_OFFSET_REVEAL_MS,
                   'MIN_SHOT_S': MIN_SHOT_S, 'MAX_SHOT_S': MAX_SHOT_S},
        'shots': shots,
    }
    with open(f"{args.out_dir}/timeline_{lang}.json", 'w', encoding='utf-8') as f:
        json.dump(timeline, f, ensure_ascii=False, indent=2)

    with open(f"{args.out_dir}/subtitles_{lang}.srt", 'w', encoding='utf-8') as f:
        for i, r in enumerate(rows, 1):
            f.write(f"{i}\n{srt_time(r['_start'])} --> {srt_time(r['_end'])}\n"
                    f"{r['text_spoken']}\n\n")

    with open(f"{args.out_dir}/edit_{lang}.csv", 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.writer(f)
        w.writerow(['shot_id','start_s','end_s','duration_s','scene_id',
                    'scene_label','cut_kind','reveal_word','over_max'])
        for s in shots:
            w.writerow([s['shot_id'], s['start'], s['end'], s['duration'],
                        s['scene_id'], s['scene_label'], s['kind'],
                        s['note'], 'YES' if s['over_max'] else ''])

    if args.concat:
        first = os.path.join(audio_dir, f"{rows[0]['sent_id']}.wav")
        with wave.open(first, 'rb') as w0:
            params = w0.getparams()
        silence = b'\x00' * int(params.framerate * GAP_MS / 1000.0
                               * params.sampwidth * params.nchannels)
        out = f"{args.out_dir}/master_{lang}.wav"
        with wave.open(out, 'wb') as ow:
            ow.setparams(params)
            for i, r in enumerate(rows):
                with wave.open(os.path.join(audio_dir, f"{r['sent_id']}.wav"), 'rb') as w:
                    ow.writeframes(w.readframes(w.getnframes()))
                if i < len(rows) - 1:
                    ow.writeframes(silence)
        print(f"  master  {out}")

    # ── 5. 보고 ───────────────────────────────────────────────
    over = [s for s in shots if s['over_max']]
    reveals = [s for s in shots if s['kind'] == 'reveal']
    print(f"\n[{lang}] 총 길이 {total/60:.0f}분 {total%60:04.1f}초")
    print(f"  문장 {len(rows)}개 → 샷 {len(shots)}개 (평균 {total/len(shots):.1f}초)")
    print(f"  리빌 컷 {len(reveals)}개")
    if over:
        print(f"  ! {MAX_SHOT_S}초 초과 샷 {len(over)}개 — 카메라 무브 필요:")
        for s in over[:10]:
            print(f"      {s['shot_id']} {s['duration']:.1f}s  {s['scene_label']}")
    print(f"\n  timeline  {args.out_dir}/timeline_{lang}.json")
    print(f"  srt       {args.out_dir}/subtitles_{lang}.srt")
    print(f"  csv       {args.out_dir}/edit_{lang}.csv")


if __name__ == '__main__':
    main()
