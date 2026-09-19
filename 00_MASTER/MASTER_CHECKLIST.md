# MASTER CHECKLIST — 제작 전 1:1 검증 기준

모든 에이전트는 이 문서의 ID를 그대로 인용한다.
**"있음/없음" 체크는 금지한다.** 반드시 `요구조건 → 결과물의 위치 → 실제 증거 → 판정 → 수정안` 5종을 제출한다.

## 판정 등급

| 등급 | 뜻 | 후속 조치 |
|---|---|---|
| `PASS-A` | 완전 충족 | 없음 |
| `PASS-B` | 충족하나 개선 여지 | 개선안 1줄 기록, 진행 가능 |
| `PARTIAL` | 일부만 충족 | 수정 후 재검사 |
| `FAIL` | 미충족 | 수정 후 재검사, 게이트 차단 |

---

## S — 대본 (Script)

| ID | 요구 | 검증 방법 | 제출 증거 | 기준 |
|---|---|---|---|---|
| S01 | 중심 질문 1개 | 영상 전체를 질문 하나로 요약 가능한가 | `central_question` 문장 | 없으면 FAIL |
| S02 | 0~30초 훅 | 역전·숫자·위기·강한 질문 중 1개 이상 | 훅 문장 + 타임코드 | 명확하면 PASS |
| S03 | 훅의 본문 회수 | 초반에 던진 것을 후반에 실제로 설명 | 훅 ID ↔ 회수 Beat ID | 대응 없으면 FAIL |
| S04 | 이야기의 주인공 | 인물/사물/개념 중 무엇을 따라가는가 | `story_anchor` | 명확해야 PASS |
| S05 | 변화 | 시작 상태 ≠ 마지막 상태 | BEFORE / AFTER | 변화 없으면 PARTIAL |
| S06 | 하몬 8단계 | YOU→NEED→GO→SEARCH→FIND→TAKE→RETURN→CHANGE | 각 단계의 실제 문장 | 8칸 전부 채워야 PASS |
| S07 | 질문→부분답→새 질문 | 설명 나열이 아니라 전진하는가 | Q1/A1/Q2 체인 | 3회 이상 |
| S08 | 마이크로 리텐션 | 30~45초마다 보상 또는 새 정보 | 타임코드 배열 | 공백 60초 초과 시 수정 |
| S09 | Research Reveal | 기억에 남는 새 사실·수치 | 해당 문단 | 1개 이상 |
| S10 | 중간 반전 | 최초 가설이 흔들리는 지점 | `reversal_text` | 있어야 강한 구조 |
| S11 | 긴장 재상승 | 답을 준 뒤 문제가 더 커짐 | payoff → complication | 존재해야 PASS |
| S12 | 인간 감정 | 목표·손실·위험·욕망 중 1개 이상 | 해당 문장 | 정보 나열만이면 PARTIAL |
| S13 | 현대 연결 | 과거→현재가 중간 메커니즘으로 이어짐 | A→B→C 문장 | 직접 점프면 FAIL |
| S14 | 경제 구조 | 돈의 흐름·병목·인프라·네트워크 중 1개 | `mechanism` | 투자 영상이면 필수 |
| S15 | 엔딩 회수 | 첫 이미지·사물·문장 중 하나 재등장 | Scene 01 ↔ Final Scene | 대응되면 PASS |
| S16 | CTA | A/B 선택 또는 판단 기준이 있는 질문 | CTA 문장 | "어떻게 생각?"만이면 PARTIAL |
| S17 | TTS 문장 | 한 문장 = 한 정보 | 긴 문장 자동 추출 | 과도하면 수정 |
| S18 | 전환 문장 | 단락 마지막이 다음 궁금증을 여는가 | 각 Beat 마지막 문장 | 70% 이상 |

---

## SC — 장면표 (Scene Table)

| ID | 요구 | 제출 증거 | 기준 |
|---|---|---|---|
| SC01 | 1 Scene = 1 Idea | `visual_purpose` | 정보 2개 이상이면 분할 |
| SC02 | 대사 ↔ 화면 1:1 | `script_line` ↔ `visual` | 내레이션의 명사가 화면에 없으면 FAIL |
| SC03 | 대형 Hero Shot | scene IDs | 8분 30초 기준 3~5개 |
| SC04 | Hero Shot의 이유 | `motion_reason` | 이야기상 이유 없으면 PARTIAL |
| SC05 | 사물 앵커 | `anchor_id` | 반복 사용 확인 |
| SC06 | 세계관 캐릭터 | character scenes | 전체의 4~8% |
| SC07 | 공간 스케일 변화 | `scale` | Macro↔Wide↔Aerial 단조로우면 수정 |
| SC08 | 카메라 리듬 | speed curve 배열 | 고속 연속이면 수정 |
| SC09 | Cutaway / X-ray | xray scene IDs | 메커니즘 영상이면 1개 이상 |
| SC10 | 장소·시간 이동 | transition scene | 갑작스러우면 수정 |
| SC11 | 전환 예약 | `transition_out` | 다음 장면과 매칭 |
| SC12 | state_out | 마지막 자세·방향·카메라 | 없으면 FAIL |
| SC13 | state_in | `previous_scene_id` | state_out과 매칭 |
| SC14 | 화면 방향 | `screen_direction` | 의도 없는 역전 수정 |
| SC15 | 캐릭터 연속성 | `continuity_id` | 동일 ID 필수 |

---

## IP — 이미지 프롬프트 (Image Prompt)

| ID | 요구 | 제출 증거 | 기준 |
|---|---|---|---|
| IP01 | 실제 장소 특정 | `location` | "도시", "사무실"만 쓰면 FAIL |
| IP02 | 주체 1개 | `subject` | 시선이 갈 곳이 하나여야 PASS |
| IP03 | 행동/상황 | `subject_action` | 정지 인물만 세워두면 PARTIAL |
| IP04 | 카메라 위치 | `camera_position` | top-down / low / OTS / eye-level 등 필수 |
| IP05 | 화각 | `shot_scale` | macro / close / medium / wide / aerial 필수 |
| IP06 | 렌즈 | `lens_mm` | 14/24/35/50/85mm 등 |
| IP07 | 깊이 | `depth_plan` (fg/mg/bg) | Hero Shot 필수 |
| IP08 | 팔레트 | `palette` | PROJECT_BIBLE의 COLOR ARC와 대조 |
| IP09 | 빛 | `lighting` | 시간대·광원·방향, 연속성 대조 |
| IP10 | 구조/소품의 목적 | `environment` | 장식만 있으면 PARTIAL |
| IP11 | 다음 컷 연결 | `next_transition_object` | 전환 예약 장면은 필수 |
| IP12 | continuity_id | `continuity_ids[]` | 반복 캐릭터·소품 없으면 FAIL |
| IP13 | visual purpose | `visual_purpose` | "왜 이 그림이 필요한가" 1줄로 설명 안 되면 수정 |

---

## VP — 영상 프롬프트 (Video Prompt)

| ID | 요구 | 제출 증거 | 기준 |
|---|---|---|---|
| VP01 | 카메라 동작 1개 | `camera_motion` | 2개 이상이면 클립 분할 |
| VP02 | 피사체 행동 1개 | `subject_motion` | 명시 필수 |
| VP03 | 시작 프레임 | `state_in` | 승인된 스틸과 일치해야 함 |
| VP04 | 종료 프레임 | `state_out` | 다음 컷으로 이어지는 상태 |
| VP05 | 경로 | `motion_path` | 직선/곡선/하강/상승/오비트 |
| VP06 | 속도 곡선 | `speed_curve` | Hero Shot은 4구간 필수 |
| VP07 | 화면 방향 | `screen_direction` | 이전 컷과 대조 |
| VP08 | 패럴랙스 | `foreground_element` | 속도감 장면 필수 |
| VP09 | 전환 행동 | `transition_action` | 차폐 전환 시 필수 |
| VP10 | 다음 컷 | `next_scene_id` | 필수 |
| VP11 | 의미 | `semantic_reason` | 대본 단어와 연결 안 되면 PARTIAL |
| VP12 | 생성 난도 | `generation_units` | 과복잡이면 A/B/C 분할, 미분할 시 FAIL |
| VP13 | 프레임 연속성 | continuity fields | 소품·빛·인물·환경 매칭 |
| VP14 | 스펙터클 빈도 | `energy_prev` / `energy_next` | 고속 피크 연속이면 수정 |

---

## G — 최종 게이트 (Gate)

| ID | 조건 |
|---|---|
| G01 | S01~S18 해결 완료 |
| G02 | SC01~SC15 치명 FAIL 0 |
| G03 | IP01~IP13 치명 FAIL 0 |
| G04 | VP01~VP14 치명 FAIL 0 |
| G05 | Script → Scene → Image → Video ID 체인 100% 매칭 |
| G06 | 위 전부 통과 시에만 `READY_TO_GENERATE = true` |
