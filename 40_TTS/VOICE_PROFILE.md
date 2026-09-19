# 음성 프로필 — Qwen3 로컬 VoiceBox

> 새 대본을 만들 때 **완성 WAV를 다시 복제하지 말 것.** 아래 참조 음성과 프로필로 새로 생성한다.

## 공통 기준 (V1 · V2 동일)

```
엔진        LOCAL_VOICEBOX
모델        Qwen3-TTS-12Hz-0.6B-Base
프로필 ID   fb4021a9-c98f-486f-8d56-0daa33f824da
참조 음성   C:\Users\llorr\Videos\flow건축\편집본_20260827\revision_39s\deliverables\02_reference_voice_39s.wav
언어        ko
속도        1.10배
출력        24000Hz, Mono PCM WAV
음량        -16 LUFS, True Peak -1.5 dBTP
```

V1과 V2는 **참조 음성이 같고 seed와 연기 지시만 다르다.**

---

## V2 — 필재 스타일 (이 영상에 사용)

```
SEED: 8312
```

### VOICE INSTRUCT

```
안정감 있는 중저음의 한국인 중년 남성 스토리텔러.
차분하고 따뜻한 신뢰감과 라디오 DJ처럼 자연스러운 대화 호흡을 사용합니다.
은근한 위트와 아주 옅은 미소가 느껴지게 읽습니다.
핵심 명사는 또렷하게 하되 세게 찍지 않습니다.
문장 전체를 한 호흡의 자연스러운 억양 곡선으로 연결합니다.
문장 끝은 급격히 떨어뜨리지 말고 부드럽고 분명하게 닫습니다.
과장된 방송 진행, 광고 목소리, 지나치게 굵은 다큐멘터리 연기는 피합니다.
```

### POSTPROCESS

```
불필요한 긴 무음 제거.
0.32초 이상 내부 무음은 0.18초로 축소.
음높이를 보존하면서 1.10배속.
24000Hz Mono PCM WAV.
-16 LUFS, True Peak -1.5 dBTP.
```

### 기존 산출물 경로

```
ZIP
C:\Users\llorr\dev\repos\AI_.2.dea_img_chracter\videos\kospi_vox_gold_60s_v2\tts_cast_qwen3_piljae_style_v2\
KOSPI_VOX_QWEN3_PILJAE_STYLE_V2_20260831.zip

완성 WAV
...\tts_cast_qwen3_piljae_style_v2\01_audio\qwen3_piljae_style_v2_refined_1p1_master.wav

매니페스트
...\tts_cast_qwen3_piljae_style_v2\02_metadata\generation_manifest...
```

---

## V1 — 정보 미비

V1은 **seed 와 VOICE INSTRUCT 를 전달받지 못했다.** 참조 음성과 프로필 ID만 V2와 공유한다는 것만 확인됐다.

V1 을 다시 쓰려면 V1 결과 폴더의 `02_metadata/generation_manifest*` 를 열어 `seed` 와 `voice_instruct` 를 확인해 이 문서에 채워 넣는다.
추정해서 적지 않는다 — seed 가 틀리면 다른 목소리가 나온다.

---

## 이 영상에서 V2 를 쓰는 이유

대본이 **다큐멘터리형 설명**이고 흥분한 주식 유튜브 톤이 아니다. `PROJECT_BIBLE` 의 톤 규정과 V2 의 연기 지시가 정확히 일치한다.

특히 두 줄이 이 대본에 결정적이다.

- **"핵심 명사는 또렷하게 하되 세게 찍지 않습니다"** — 총수익률, 기초자산, 옵션 프리미엄 같은 용어가 또렷해야 하지만, 세게 찍으면 판매 톤이 된다
- **"문장 끝은 급격히 떨어뜨리지 말고 부드럽고 분명하게 닫습니다"** — 이 대본은 문장 끝마다 장면을 전환하므로, 끝이 뭉개지면 컷 포인트가 흐려진다

---

## 생성 방식 — 반드시 문장별로 나눠서

**마스터 WAV 한 개로 만들지 말 것.** `sentences_ko.tsv` 의 98문장을 **각각 개별 WAV** 로 생성한다.

| | 마스터 1개 | 문장별 98개 |
|---|---|---|
| 장면 타이밍 | 귀로 찾아야 함 (추정) | 길이 합산으로 **계산** (정확) |
| 한 문장 재생성 | 전체 재생성 | 그 문장만 |
| 일본어판 | 처음부터 다시 | **같은 문장 ID로 교체, 장면 ID 유지** |
| 리빌 단어 정렬 | 불가능에 가까움 | 문장 내 비율로 계산 가능 |

Qwen3 VoiceBox 는 Edge TTS 와 달리 **단어 단위 타임스탬프를 주지 않는다.**
문장별 생성이 그 부재를 메우는 유일한 실용적 방법이다.

### 파일명 규칙 (필수)

```
S001.wav, S002.wav, ... S098.wav
```

`build_timeline.py` 가 이 이름으로 길이를 읽는다. 이름이 다르면 동작하지 않는다.

### 출력 폴더

```
01_audio\ko\S001.wav ... S098.wav
```
