# 적용 예시 — 3개 장면을 끝까지 통과시킨 기록

`장면표 → 이미지 프롬프트 → 이미지 검증 → 영상 프롬프트 → 영상 검증` 전 구간을 실제로 돌린 샘플.
**나머지 장면은 이 형식을 그대로 복제한다.**

---

# 예시 1 — SC_01 오프닝 훅 (hero)

## 1-1. 장면표 (입력)

```json
{
  "scene_id": "SC_01",
  "timecode": "0:00-0:12",
  "script_line": "매달 돈이 들어오고, 연으로 계산하면 10%, 15%, 어떤 ETF는 20%에 가까운 숫자가 보입니다.",
  "visual_purpose": "'매달 들어오는 돈'을 사물 하나로 각인시켜 영상 전체의 앵커를 세운다. 엔딩에서 이 사물이 되돌아온다.",
  "shot_role": "hero",
  "anchor_id": "ANC_ENVELOPE",
  "continuity_ids": ["ANC_ENVELOPE"],
  "screen_direction": "downward",
  "transition_out": "envelope mouth swallows the frame",
  "state_out": "camera has descended to the envelope opening, frame 80% filled by the dark interior",
  "next_scene_id": "SC_02"
}
```

## 1-2. 이미지 프롬프트 (IMAGE_PROMPT_AGENT 출력)

```json
{
  "image_id": "IMG_SC_01",
  "scene_id": "SC_01",
  "timecode": "0:00-0:12",
  "script_line": "매달 돈이 들어오고, 연으로 계산하면 10%, 15%, 어떤 ETF는 20%에 가까운 숫자가 보입니다.",
  "visual_purpose": "'매달 들어오는 돈'을 사물 하나로 각인시켜 영상 전체의 앵커를 세운다.",
  "shot_role": "hero",
  "needs_revision": false,

  "location": "a dim 1970s-style tabletop workshop at night, cold air, fine dust suspended and drifting under a single lamp",
  "subject": "a single kraft paper envelope standing upright on a worn oak workbench",
  "subject_action": "the envelope flap caught mid-lift, warm gold light spilling upward out of the opening like steam",
  "camera_position": "low-angle",
  "shot_scale": "medium-wide",
  "lens_mm": "24mm",
  "depth_plan": {
    "fg": "out-of-focus brass coin edge occupying the lower-left corner, catching a hard gold specular",
    "mg": "the upright kraft envelope, flap lifting, gold light escaping",
    "bg": "eleven more identical envelopes receding into darkness in a shallow arc, progressively unlit"
  },
  "palette": { "id": "PAL_LURE", "hex": ["#0B1526", "#F5B72E", "#E8E4DA"] },
  "lighting": "single warm key light from camera-left 45 degrees, hard falloff into black, weak cool navy rim from behind the envelope row, 3200K key / 7000K rim",
  "environment": "worn oak grain, kraft paper fibre visible at the torn edge, brass coin milling sharp in the foreground — every material reads as physical and countable, so the viewer feels the money is real before being told it might not be",
  "continuity_ids": ["ANC_ENVELOPE"],
  "next_transition_object": { "object": "envelope mouth interior", "screen_location": "center, upper two-thirds" },
  "screen_direction": "downward",

  "prompt_en": "Medium-wide low-angle shot, 24mm lens, a single kraft paper envelope standing upright on a worn oak workbench, the envelope flap caught mid-lift with warm gold light spilling upward out of the opening like steam, in a dim 1970s-style tabletop workshop at night, cold air, fine dust suspended and drifting under a single lamp. Foreground: out-of-focus brass coin edge occupying the lower-left corner, catching a hard gold specular. Midground: the upright kraft envelope, flap lifting, gold light escaping. Background: eleven more identical envelopes receding into darkness in a shallow arc, progressively unlit. Lighting: single warm key light from camera-left 45 degrees, hard falloff into black, weak cool navy rim from behind the envelope row, 3200K key / 7000K rim. Color: deep navy #0B1526, oversaturated gold #F5B72E, bone white #E8E4DA. Materials and detail: worn oak grain, kraft paper fibre visible at the torn edge, brass coin milling sharp in the foreground. Style: photoreal cinematic 3D render, physically based materials, shallow depth of field, subtle film grain, tabletop miniature scale. Composition: 16:9, subject kept out of the lower 18% caption safe area. No legible text, no numerals, no labels, no logos.",

  "negative_prompt": "text, letters, hangul, korean characters, numerals, digits, watermark, signature, logo, brand mark, ticker symbol, chart axis labels, legend, UI overlay, user interface, extra fingers, deformed hands, warped face, duplicated face, stock-photo smile, person looking at camera and smiling, thumbs up, fanning cash, money rain, red and blue candlestick chart, cluttered composition, busy background, flat lighting, low contrast, oversharpened, plastic skin",

  "tech": {
    "aspect_ratio": "16:9",
    "resolution": "1920x1080",
    "seed_policy": "fixed_per_anchor",
    "reference_image": null,
    "variants": 4
  },

  "ip_selfcheck": [
    { "check_id": "IP01", "status": "PASS-A", "evidence": "location = 'a dim 1970s-style tabletop workshop at night, cold air, fine dust...' — 장소+시대+시간대+공기상태" },
    { "check_id": "IP02", "status": "PASS-A", "evidence": "subject = 'a single kraft paper envelope' — 단일. 배경 봉투 11개는 아웃포커스 처리" },
    { "check_id": "IP03", "status": "PASS-A", "evidence": "subject_action = 'flap caught mid-lift, light spilling upward' — 진행 중 상태" },
    { "check_id": "IP04", "status": "PASS-A", "evidence": "camera_position = 'low-angle' — 사물을 크게 보이게 해 앵커로 각인" },
    { "check_id": "IP05", "status": "PASS-A", "evidence": "shot_scale = 'medium-wide'" },
    { "check_id": "IP06", "status": "PASS-A", "evidence": "lens_mm = '24mm'" },
    { "check_id": "IP07", "status": "PASS-A", "evidence": "depth_plan 3층 전부 채움. hero 요건 충족" },
    { "check_id": "IP08", "status": "PASS-A", "evidence": "palette.id = 'PAL_LURE', timecode 0:00-0:12 → A1막. BIBLE 표 일치" },
    { "check_id": "IP09", "status": "PASS-A", "evidence": "lighting에 광원(key/rim) + 방향(camera-left 45deg / behind) + 색온도(3200K/7000K) 3요소 전부" },
    { "check_id": "IP10", "status": "PASS-A", "evidence": "environment에 '재질이 물리적으로 읽혀야 돈이 진짜처럼 느껴진다'는 목적 명시" },
    { "check_id": "IP11", "status": "PASS-A", "evidence": "transition_out='envelope mouth swallows the frame' ↔ next_transition_object='envelope mouth interior', prompt_en 본문에 'the opening'으로 실재" },
    { "check_id": "IP12", "status": "PASS-A", "evidence": "continuity_ids=['ANC_ENVELOPE'], BIBLE 고정묘사 'kraft paper envelope, slightly worn edge, no text, warm gold light leaking from the opening' 본문 반영" },
    { "check_id": "IP13", "status": "PASS-A", "evidence": "visual_purpose 1문장. 이 그림이 없으면 엔딩 회수(S15)가 성립하지 않음" }
  ]
}
```

## 1-3. 영상 프롬프트 (VIDEO_PROMPT_AGENT 출력)

```json
{
  "video_id": "VID_SC_01",
  "scene_id": "SC_01",
  "image_id": "IMG_SC_01",
  "generation_units": { "index": "A", "total": 1 },
  "timecode": "0:00-0:12",
  "script_line": "매달 돈이 들어오고...",
  "semantic_reason": "대본이 '들어오고'라고 말하므로, 시청자의 시점이 봉투 안으로 들어가는 하강 이동이 필요하다. 카메라가 돈을 따라 들어가면 다음 컷부터 '안에서 보는 시점'이 자연스럽게 성립한다.",

  "start_frame_image": "IMG_SC_01",
  "state_in": "Low-angle 24mm, envelope upright on the bench, flap mid-lift, gold light rising, brass coin edge in lower-left foreground, eleven unlit envelopes in the dark background arc.",
  "state_out": "Camera has risen and tilted down over the envelope mouth; the dark interior fills 80% of the frame, only a gold rim of the opening remains at the frame edge.",

  "subject_motion": "the gold light column rising from the envelope opening thickens and drifts upward past the lens",
  "camera_motion": "crane-up",
  "motion_path": "arcing rise of 40cm while tilting down 60 degrees to look into the envelope mouth",
  "speed_curve": {
    "approach": "0.0-1.0s near-static, only the light drifting",
    "accelerate": "1.0-2.2s the rise begins and builds",
    "peak": "2.2-3.4s sustained travel over the opening",
    "decelerate": "3.4-5.0s ease-out as the dark interior fills the frame"
  },
  "screen_direction": "downward",
  "direction_flip_reason": null,
  "foreground_element": "the out-of-focus brass coin edge sweeps down and out of the bottom-left of frame at 1.6s as the camera rises, giving parallax against the static bench",
  "transition_action": "the envelope's dark interior fills the frame until it is effectively black, handing off to SC_02",
  "lighting_continuity": "3200K key from camera-left 45 degrees and cool navy rim from behind — unchanged from IMG_SC_01 throughout",

  "energy": 4,
  "energy_prev": null,
  "energy_next": 2,

  "next_scene_id": "SC_02",
  "clip_seconds": 5,
  "fps": 24,
  "motion_strength": "medium",

  "prompt_en": "The gold light column rising from the envelope opening thickens and drifts upward past the lens. Camera: crane-up along an arcing rise of 40cm while tilting down 60 degrees to look into the envelope mouth. Near-static for the first second, the rise builds from 1.0s, sustained travel over the opening, then eases out as the dark interior fills the frame. The out-of-focus brass coin edge sweeps down and out of the bottom-left of frame at 1.6s, giving parallax against the static bench. Lighting and color remain unchanged: 3200K key from camera-left 45 degrees, cool navy rim from behind. The shot ends with the envelope's dark interior filling 80% of the frame, only a gold rim of the opening remaining at the frame edge. Single continuous take, no cuts, no scene change.",

  "negative_prompt": "scene change, cut, jump cut, new character appearing, new object appearing, morphing, warping, melting geometry, flickering, strobing, text appearing, numbers changing, letters forming, face distortion, duplicated limbs, extra fingers, hands manipulating small objects, walking full-body figure, crowd of faces, lip movement, talking, camera shake, handheld jitter, zoom pump, speed ramp, watermark, logo, subtitles",

  "vp_selfcheck": [
    { "check_id": "VP01", "status": "PASS-A", "evidence": "camera_motion = 'crane-up' 단일. prompt_en 본문에도 다른 카메라 동사 없음" },
    { "check_id": "VP02", "status": "PASS-A", "evidence": "subject_motion = 빛 기둥의 상승 1개" },
    { "check_id": "VP03", "status": "PASS-A", "evidence": "state_in이 IMG_SC_01의 depth_plan 3층을 그대로 서술" },
    { "check_id": "VP04", "status": "PASS-A", "evidence": "state_out = '어두운 내부가 80% 채움' → SC_02의 state_in('어둠 속에서 시작')과 연결" },
    { "check_id": "VP05", "status": "PASS-A", "evidence": "motion_path = '40cm 호형 상승 + 60도 하향 틸트'" },
    { "check_id": "VP06", "status": "PASS-A", "evidence": "hero이므로 4구간 전부. 구간 합 = 5.0s = clip_seconds" },
    { "check_id": "VP07", "status": "PASS-A", "evidence": "screen_direction = 'downward'. 첫 컷이므로 비교 대상 없음, flip 없음" },
    { "check_id": "VP08", "status": "PASS-A", "evidence": "foreground_element = 브라스 코인 엣지, 1.6s에 좌하단 이탈" },
    { "check_id": "VP09", "status": "PASS-A", "evidence": "transition_action = 봉투 내부 암전 (물리적 차폐. 디졸브 아님)" },
    { "check_id": "VP10", "status": "PASS-A", "evidence": "next_scene_id = 'SC_02'" },
    { "check_id": "VP11", "status": "PASS-A", "evidence": "대본 '들어오고' → 안으로 들어가는 하강 시점. 카메라와 대본 단어가 직결" },
    { "check_id": "VP12", "status": "PASS-B", "evidence": "상승+틸트 동시이나 둘 다 카메라 한 리그의 연속 동작이고 5s 이내. 분할 불필요", "fix": "생성 1차에서 공간이 무너지면 A(상승) / B(틸트 다운)로 분할" },
    { "check_id": "VP13", "status": "PASS-A", "evidence": "lighting_continuity가 IMG_SC_01의 lighting 문자열과 동일" },
    { "check_id": "VP14", "status": "PASS-A", "evidence": "energy 4. energy_next=2 (SC_02는 locked-off). 5 연속 없음" }
  ]
}
```

---

# 예시 2 — SC_18 옵션 프리미엄 (explain) · **검증에서 FAIL이 잡힌 사례**

## 2-1. 이미지 프롬프트 1차 (문제 있음)

```json
{
  "image_id": "IMG_SC_18",
  "timecode": "1:48-2:02",
  "script_line": "그 권리를 팔아주는 대가로 돈을 받습니다.",
  "location": "a workshop",
  "subject": "an engine and a device and coins",
  "camera_position": "eye-level",
  "shot_scale": "close",
  "lens_mm": "85mm",
  "lighting": "soft cinematic lighting",
  "palette": { "id": "PAL_LURE", "hex": ["#0B1526", "#F5B72E"] },
  "continuity_ids": ["ANC_ENGINE", "ANC_DEVICE"],
  "next_transition_object": null
}
```

## 2-2. 검증 결과 (IMAGE_PROMPT_VALIDATOR 출력)

```json
{
  "image_id": "IMG_SC_18",
  "results": [
    {
      "check_id": "IP01", "requirement": "실제 장소 특정",
      "quoted": "location = 'a workshop'",
      "status": "FAIL",
      "reason": "시간대·조명 상태·공기 상태 없음. SC_01과 같은 공간인데 생성 시마다 다른 작업실이 나온다.",
      "fix": "location = 'the same dim 1970s-style tabletop workshop at night as IMG_SC_01, dust settled, lamp dimmer than before'"
    },
    {
      "check_id": "IP02", "requirement": "주체 1개",
      "quoted": "subject = 'an engine and a device and coins'",
      "status": "FAIL",
      "reason": "and로 병렬된 주체 3개. 시선이 갈 곳이 없다. SC01 위반이기도 하다.",
      "fix": "subject = 'a single brass valve on the matte black module' — 엔진과 코인은 depth_plan의 mg/fg로 내린다"
    },
    {
      "check_id": "IP09", "requirement": "빛 (광원+방향+색온도)",
      "quoted": "lighting = 'soft cinematic lighting'",
      "status": "FAIL",
      "reason": "3요소 전무. IMG_SC_17~19 연속성이 전부 깨진다.",
      "fix": "lighting = 'single warm key light from camera-left 45 degrees, hard falloff, cool teal fill from behind the flywheel, 3200K key / 6500K fill'"
    },
    {
      "check_id": "IP11", "requirement": "다음 컷 연결",
      "quoted": "next_transition_object = null",
      "status": "FAIL",
      "reason": "장면표의 transition_out = 'gold light floods the frame'인데 그 광원이 프레임 안에 지정되지 않았다.",
      "fix": "next_transition_object = { object: 'brass valve aperture', screen_location: 'center-right third' } 로 지정하고 prompt_en 본문에 밸브 개구부를 명시한다"
    }
  ],
  "cross_checks": [
    {
      "check_id": "X-ARC",
      "quoted": "palette.id = 'PAL_LURE' at timecode 1:48-2:02",
      "status": "FAIL",
      "reason": "1:20 이후는 A2막 = PAL_DISSECT. A1 팔레트를 쓰면 '유혹'에서 '해부'로 넘어간 감정 전환이 화면에서 사라진다.",
      "fix": "palette = { id: 'PAL_DISSECT', hex: ['#1E5F6B', '#E8E4DA', '#B8892A'] }"
    },
    {
      "check_id": "X-BIBLE",
      "quoted": "continuity_ids = ['ANC_ENGINE', 'ANC_DEVICE'] 이나 prompt_en에 바이블 고정묘사 없음",
      "status": "FAIL",
      "reason": "ID만 적고 본문에 'exposed brass-and-steel mechanical engine, visible flywheel' / 'matte black bolt-on module with a single brass valve, clamped ON TOP' 가 없다. 가장 흔한 실패 유형.",
      "fix": "바이블 고정 묘사를 글자 그대로 prompt_en에 삽입한다"
    }
  ],
  "counts": { "PASS-A": 5, "PASS-B": 2, "PARTIAL": 0, "FAIL": 6 },
  "verdict": "REVISE"
}
```

> **이 6개를 잡지 못하고 생성했다면**: 다른 작업실, 다른 조명, 틀린 팔레트, 장치가 엔진에서 분리된 그림이 나온다.
> 그 시점에는 이미지 재생성 + 영상 재생성 + 편집 재작업이 전부 다시 발생한다. **글 단계에서 6줄 고치면 끝나는 일이다.**

---

# 예시 3 — SC_52 엔딩 회수 (hero)

```json
{
  "image_id": "IMG_SC_52",
  "scene_id": "SC_52",
  "timecode": "8:15-8:30",
  "script_line": "분배금이 가장 큰 ETF가 아니라, 내 목적에 맞는 ETF를 찾는 겁니다.",
  "visual_purpose": "오프닝의 봉투를 같은 각도로 되돌려주되 채도를 낮춰, 시청자가 '같은 것을 다르게 보게 되었다'는 상태를 설명 없이 느끼게 한다.",
  "shot_role": "hero",
  "needs_revision": false,

  "location": "the same 1970s-style tabletop workshop as IMG_SC_01, now at dawn, dust settled, the lamp off and daylight entering from camera-right",
  "subject": "the same kraft paper envelope, now resting flat on the workbench beside the engine",
  "subject_action": "the flap settling closed, the last of the gold light fading from the opening as daylight takes over",
  "camera_position": "low-angle",
  "shot_scale": "medium-wide",
  "lens_mm": "24mm",
  "depth_plan": {
    "fg": "the same brass coin, now still and fully in focus in the lower-left",
    "mg": "the envelope lying flat, flap closing",
    "bg": "the engine running quietly, the black module no longer clamped on top of it but set aside on the bench"
  },
  "palette": { "id": "PAL_RESOLVE", "hex": ["#C9902F", "#0B1526", "#E8E4DA"] },
  "lighting": "soft daylight key from camera-right 30 degrees, wide falloff, no hard specular, 5600K single source — deliberately the mirror direction of IMG_SC_01's camera-left key",
  "environment": "same oak grain, same kraft fibre, same coin milling as IMG_SC_01 — the materials are identical so that only the light and the saturation have changed",
  "continuity_ids": ["ANC_ENVELOPE", "ANC_ENGINE", "ANC_DEVICE"],
  "next_transition_object": null,
  "screen_direction": "static",

  "prompt_en": "Medium-wide low-angle shot, 24mm lens, the same kraft paper envelope now resting flat on the workbench beside an exposed brass-and-steel mechanical engine, the flap settling closed and the last of the gold light fading from the opening as daylight takes over, in the same 1970s-style tabletop workshop at dawn, dust settled, the lamp off and daylight entering from camera-right. Foreground: the same brass coin, now still and fully in focus in the lower-left. Midground: the envelope lying flat, flap closing. Background: the engine running quietly with its visible flywheel turning, the matte black bolt-on module no longer clamped on top of it but set aside on the bench. Lighting: soft daylight key from camera-right 30 degrees, wide falloff, no hard specular, 5600K single source. Color: warm amber #C9902F, deep navy #0B1526, bone white #E8E4DA, noticeably lower saturation than the opening shot. Materials and detail: same oak grain, same kraft paper fibre, same coin milling as the opening shot. Style: photoreal cinematic 3D render, physically based materials, shallow depth of field, subtle film grain, tabletop miniature scale. Composition: 16:9, subject kept out of the lower 18% caption safe area. No legible text, no numerals, no labels, no logos.",

  "tech": { "aspect_ratio": "16:9", "resolution": "1920x1080", "seed_policy": "fixed_per_anchor", "reference_image": "IMG_SC_01", "variants": 4 },

  "ip_selfcheck_excerpt": [
    { "check_id": "IP08", "status": "PASS-A", "evidence": "PAL_RESOLVE. A1(PAL_LURE)과 같은 골드 계열이되 #F5B72E → #C9902F 로 채도 하락 = S15 엔딩 회수의 시각적 증거" },
    { "check_id": "IP09", "status": "PASS-A", "evidence": "키 라이트 방향이 camera-left(오프닝) → camera-right(엔딩)로 반전. 같은 공간이지만 시점이 바뀌었음을 빛으로 표현" },
    { "check_id": "IP12", "status": "PASS-A", "evidence": "ANC_DEVICE가 ANC_ENGINE 위가 아니라 '옆에 내려놓인' 상태. 대본 '엔진 자체를 먼저 보라'의 결론을 배치로 표현" }
  ]
}
```

> **이 컷의 핵심은 `ANC_DEVICE`의 위치다.** 영상 내내 엔진 **위**에 있던 장치가 마지막에 **옆**에 놓인다.
> 내레이션이 한 번도 말하지 않지만, 이 배치 변화가 "순서가 뒤집혔다 → 순서를 바로잡았다"를 화면으로 끝낸다. (S05 변화 / S15 회수)
> `ip_selfcheck`는 여기서 3개만 발췌했다. **실제 산출물은 IP01~IP13 13개 전부 필수다.**

---

# 다음 작업

1. 이 형식으로 나머지 장면표를 채운다 (8분 30초 ÷ 평균 9초 ≈ **52컷 내외**)
2. `hero`는 3~5컷만 (SC03). 지금 확정: `SC_01` / `SC_28`(엔진 위 장치 제거) / `SC_52`
3. 이미지 검증 → 영상 검증 순으로 전부 통과시킨 뒤 `READY_TO_GENERATE = true`
4. 그때 처음으로 실제 생성을 시작한다
