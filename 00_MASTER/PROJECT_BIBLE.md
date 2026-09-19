# PROJECT BIBLE — 2026년 10월 / 월배당 ETF 3가지 숫자

> 이미지·영상 프롬프트 에이전트는 **매 장면마다 이 문서를 먼저 읽고** `palette` / `continuity_ids` / `lighting`을 여기서 인용한다.
> 여기에 정의되지 않은 색·인물·사물을 새로 만들면 그 자체로 `FAIL`.

---

## 0. 영상 기본 사양

| 항목 | 값 |
|---|---|
| 길이 | 8분 30초 |
| 종횡비 | 16:9 / 1920×1080 (생성은 1920×1080 또는 2048×1152) |
| 자막 세이프존 | 하단 18% — 이 영역에 주요 피사체·디테일 배치 금지 |
| 상단 세이프존 | 상단 10% |
| 톤 | 다큐멘터리형 설명. 흥분한 주식 유튜브 톤 아님 |
| 렌더 스타일 | `photoreal cinematic 3D render, physically based materials, shallow depth of field, soft studio key light, subtle film grain, tabletop miniature scale` |

---

## 1. COLOR ARC (S05 변화 ↔ IP08 팔레트 대조 기준)

색이 대본의 감정 곡선을 따라간다. **골드 = 분배금(현금흐름), 틸 = 자산가치(총수익률)** 로 끝까지 분리한다.

| 막 | 타임코드 | 이름 | 팔레트 | 의미 |
|---|---|---|---|---|
| A1 | 0:00–1:20 | `PAL_LURE` | deep navy `#0B1526` + oversaturated gold `#F5B72E` + hot specular | 유혹. 숫자가 너무 예뻐 보이는 구간 |
| A2 | 1:20–3:55 | `PAL_DISSECT` | cold teal `#1E5F6B` + bone white `#E8E4DA` + gold 채도 40% 낮춤 | 해부. 구조를 뜯어보는 구간 |
| A3 | 3:55–5:35 | `PAL_STRUCTURE` | slate grey `#2B3038` + gold/teal 동일 비중 대비 | 선택. 무엇을 포기하는가 |
| A4 | 5:35–7:00 | `PAL_REALITY` | desaturated grey-amber `#6B5E4A`, 저채도 | 경고. 약속된 월급이 아니다 |
| A5 | 7:00–8:30 | `PAL_RESOLVE` | warm amber `#C9902F` + navy, **A1보다 채도 낮음** | 정리. 같은 따뜻함이지만 성숙해진 색 |

> A5가 A1과 같은 계열이되 채도가 낮은 것이 **S15 엔딩 회수**의 시각적 증거다. 검증자는 이걸 확인한다.

---

## 2. 앵커 사물 (SC05 / IP12)

| continuity_id | 사물 | 고정 묘사 | 등장 규칙 |
|---|---|---|---|
| `ANC_ENVELOPE` | 월분배금 봉투 | kraft paper envelope, slightly worn edge, no text, warm gold light leaking from the opening | **첫 장면 + 마지막 장면 필수** (S15 회수) |
| `ANC_ENGINE` | 기초자산 = 엔진 | exposed brass-and-steel mechanical engine, visible flywheel, warm interior glow | 기초자산 언급 시 |
| `ANC_DEVICE` | 커버드콜 = 얹는 장치 | matte black bolt-on module with a single brass valve, clamped ON TOP of `ANC_ENGINE` | 반드시 `ANC_ENGINE` 위에만. 단독 등장 금지 |
| `ANC_CEILING` | 상승 제한 = 유리 천장 | thick frosted glass plate suspended horizontally, faint teal refraction | 상승 여력 포기 언급 시 |
| `ANC_SCALE` | 총수익률 = 양팔 저울 | brass balance scale, 왼쪽 접시=gold coins(분배금), 오른쪽 접시=teal glass block(가격 변화) | 총수익률 언급 시 |
| `ANC_DIAL` | 옵션 매도 비중 = 다이얼 | knurled brass dial with an unmarked arc, no numerals | 전략 차이 언급 시 |
| `ANC_SPROUT` | 자산 성장 | single sapling in dark soil, teal-lit leaves | 성장 vs 현금흐름 대비 시 |

**장치는 엔진 위에만 올라간다.** 이 규칙 하나가 "커버드콜은 엔진 위에 얹는 장치"라는 대본 논리를 화면에서 유지시킨다.

---

## 3. 인물 (SC15 / IP12)

정면 얼굴 클로즈업은 **영상 전체 3컷 이하**. 나머지는 뒷모습·측면·손·어깨 너머로 처리한다.
(AI 생성에서 같은 얼굴을 반복 유지하는 비용이 크고, I2V에서 입이 제멋대로 움직인다)

| continuity_id | 인물 | 고정 묘사 |
|---|---|---|
| `CHR_WORKER` | 자산을 키우는 단계의 30대 직장인 | East Asian person in their 30s, charcoal knit sweater, plain silver watch, short dark hair, seen from behind or in profile |
| `CHR_RETIREE` | 은퇴를 앞둔 투자자 | East Asian person in their 60s, warm beige cardigan, reading glasses on a cord, silver-grey hair, hands often in frame |

---

## 4. 절대 금지 (위반 시 즉시 FAIL)

1. **화면에 읽히는 글자·숫자 금지.** 한글·영문·숫자·티커·축 라벨 전부. 모든 수치는 편집 단계 오버레이로 넣는다. → 프롬프트에 `no legible text, no numerals, no labels` 필수.
2. **실제 상품명·운용사·로고·티커 금지.** 특정 상품 추천으로 오인될 수 있고 상표 문제가 된다.
3. **차트는 형태만.** 우상향 / 횡보 / 급등 / 계단형 같은 **기하 형태**만 지시한다. 눈금·범례·정확한 수치는 지시하지 않는다.
4. **한국식 등락 색(빨강 상승/파랑 하락) 사용 금지.** 글로벌 관행과 충돌한다. 이 영상에서 색은 **골드=현금흐름 / 틸=자산가치** 축으로만 쓴다.
5. **자막 세이프존(하단 18%)에 핵심 피사체 배치 금지.**
6. **말하는 인물 정면 클로즈업 금지.** 내레이션 영상이므로 립싱크가 맞지 않는다.
7. **스톡사진식 미소 금지.** 카메라 보고 웃는 사람, 엄지 척, 돈다발 부채질.

---

## 5. 대본 ↔ 앵커 매핑 (SC02 검증용)

| 타임코드 | 대본 핵심어 | 필수 앵커 |
|---|---|---|
| 0:00–0:35 | 매달 돈이 들어오고 | `ANC_ENVELOPE` |
| 1:20–2:15 | 콜옵션을 판다 / 공짜 점심 | `ANC_ENGINE` + `ANC_DEVICE` |
| 2:15–3:05 | A와 B / 상승 수익 일부 제한 | `ANC_CEILING` |
| 3:05–3:55 | 총수익률 | `ANC_SCALE` |
| 3:55–4:45 | 옵션을 얼마나 파느냐 | `ANC_DIAL` |
| 4:45–5:35 | 엔진 자체가 무엇인가 | `ANC_ENGINE` (장치 제거 상태 포함) |
| 5:35–6:20 | 약속된 월급이 아니다 | `ANC_ENVELOPE` (두께가 달라진 상태) |
| 6:20–7:00 | 30대 vs 은퇴 | `CHR_WORKER` / `CHR_RETIREE` |
| 8:15–8:30 | 다음 편 예고 | `ANC_ENVELOPE` 회수 |
