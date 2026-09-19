# 스토리보드 시트 — 씨드림 5.0 Pro 생성 기록

| 항목 | 값 |
|---|---|
| 모델 | `bytedance / seedream-5-0-pro` (text2image) |
| 비용 | 장당 4크레딧 → **할인가 2크레딧**. 6장 = 12크레딧 |
| 계정 | Ultra 연간 구독 활성 (2027-08-31까지), 생성 시점 잔액 8,994크레딧 |
| 비율 | 4:3 (16:9 패널 3열 × 4행 그리드에 맞춘 시트 비율) |
| 구성 | 스타일 3종 × 2장 = **6장**, 시트당 12패널, 스타일당 24패널 |

> **주의:** `videocdn.pollo.ai` 가 조직 egress 정책으로 차단(403)되어 이 세션에서 이미지를 내려받지 못했다.
> 따라서 아래 시트들은 **생성 성공까지만 확인**했고, 화면 품질은 검수되지 않았다. 사용자가 직접 열어 확인해야 한다.

---

## 스타일 3종

| # | 이름 | 근거 | 프롬프트 스타일 블록 |
|---|---|---|---|
| 1 | 일본 심플 플랫 카툰 | **첨부 레퍼런스 5장 실측** (そろ谷のアニメっち 계열) | flat Japanese web-cartoon, thick even dark-navy outlines, flat fill colors, no gradients, no shading, rounded blob characters with tiny dot eyes and pink oval cheeks, pale cream bodies, pastel mint and sky backgrounds |
| 2 | 건축사전 | **폴더명 추론** (`A건축사전style` 접근 불가) | architectural encyclopedia plate, precise technical cutaway and cross-section drawing, fine uniform ink linework, isometric and orthographic projection, subtle cross-hatching, thin leader lines, cream drafting paper / slate grey / brick ochre / dusty teal |
| 3 | Avox지식 | **폴더명 추론** (`Avox지식style` 접근 불가) | flat vector infographic knowledge-explainer, bold geometric shapes, no outlines, saturated deep navy / gold / teal / coral, faceless silhouette figures, large clean icons, generous white space |

스타일 2·3은 레퍼런스 이미지를 보지 못하고 이름만으로 추론했다. 원본 폴더 이미지를 채팅에 올리면 재생성한다.

---

## 패널 24개 ↔ 대본 매핑

### 시트 A — 전반부 (0:00–3:55)

| # | 타임코드 | 대본 근거 | 화면 |
|---|---|---|---|
| 1 | 0:00 | 매달 돈이 들어오고 | 봉투가 기울며 금화가 호를 그리며 쏟아짐 |
| 2 | 0:12 | 은행에 넣어둘 이유가 있나 | 막대 2개 — 짧은 회색 vs 높은 골드 |
| 3 | 0:35 | 배당주·미국지수·채권·커버드콜 | 선반 위 ETF 상자 4개, 하나만 골드 |
| 4 | 0:55 | 월 분배율 1% 넘는 커버드콜 | 골드 막대 하나가 작은 막대 3개를 압도 |
| 5 | 1:10 | 그 돈은 어디에서 나오는가 | 물음표 + 떠 있는 금화 |
| 6 | 1:28 | 콜옵션을 다른 사람에게 판다 | 주식 종이 → 화살표 → 콜옵션 티켓 |
| 7 | 1:48 | 그 대가로 돈을 받는다 | 곡선 화살표를 타고 금화가 봉투로 |
| 8 | 2:00 | 공짜 점심은 없다 | 저울이 기움 — 금화 vs 떠오르는 틸 큐브 |
| 9 | 2:25 | 시장이 옆으로 움직인다면 | 횡보 라인그래프, A·B 두 점 |
| 10 | 2:45 | B는 상승 수익 일부가 제한 | 급등 그래프, A는 상승 B는 유리천장에 막힘 |
| 11 | 3:00 | 분배율과 수익률은 다르다 | 골드·틸 원 2개 사이에 굵은 X |
| 12 | 3:30 | 총수익률을 본다 | 수평을 이룬 저울 — 금화 vs 틸 블록 |

### 시트 B — 후반부 (3:55–8:30)

| # | 타임코드 | 대본 근거 | 화면 |
|---|---|---|---|
| 13 | 3:10 | 15% 받았는데 가격이 10% 떨어지면 | 상승 골드 막대 + 하락 틸 막대 + 작은 순액 막대 |
| 14 | 3:55 | 옵션을 얼마나 파느냐 | 눈금 없는 호 위의 다이얼 포인터 |
| 15 | 4:15 | 데일리·위클리·타겟프리미엄 | 전략 카드 3장 |
| 16 | 4:35 | 무엇을 포기하고 있는가 | 갈림길 — 금화 길 vs 상승 화살표 길 |
| 17 | 4:50 | 기술주·배당주·대형주·채권 | 서로 다른 엔진 4기 |
| 18 | 5:05 | **커버드콜은 엔진 위에 얹는 장치** | 엔진 위에 볼트로 고정된 검은 모듈, 골드 빛이 아래로 |
| 19 | 5:20 | 무엇에 투자 → 상승 여력 → 분배 | 번호 붙은 3단계 |
| 20 | 5:50 | 분배금은 고정 이자가 아니다 | 들쭉날쭉한 월별 막대그래프 |
| 21 | 6:05 | 이익 초과 분배 시 원금 감소 | 줄어드는 금화 더미 + 하향 화살표 + 경고 삼각형 |
| 22 | 6:45 | 30대 직장인 vs 은퇴 투자자 | 등을 맞댄 두 인물 — 새싹 / 봉투 |
| 23 | 7:00 | 세 줄 정리 | 체크 3개짜리 체크리스트 카드 |
| 24 | 8:15 | 다음 편 5가지 비교축 + 회수 | 아이콘 5개 + **닫힌 봉투** (1번 회수) |

---

## 검증 관점

- **S15 엔딩 회수**: 패널 1(열린 봉투, 쏟아짐) ↔ 패널 24(닫힌 봉투, 정지) — 시각적으로 성립
- **앵커 규칙**: 패널 18에서 장치가 엔진 **위**에 고정. PROJECT_BIBLE 규칙 준수
- **금지사항**: 전 패널 영문 짧은 단어만 허용, 한글·일본어·문장·로고 금지로 지시
- **미해결**: 패널 18의 "장치를 엔진 옆에 내려놓는" 엔딩 변형은 24패널 안에 넣지 못했다. 실제 장면표에서 `SC_28` / `SC_52`로 분리해 처리한다

---

## 생성 결과 (2026-09-19, 6/6 succeed)

`CDN` 은 원본 PNG, `뷰어` 는 폴로 상세 페이지. 둘 다 사용자 브라우저에서 열어야 한다.

### 스타일 1 — 일본 심플 플랫 카툰

**시트 A (패널 1–12)**
- CDN: https://videocdn.pollo.ai/web-cdn/pollo/production/cmf20asu60gslb2k5fhlac2gn/ori/cmu8jkmu54kznzlasqrq81yf5-0-c1f21a3998e91bf3.png
- 뷰어: https://pollo.ai/v/cmu8jkmu54kznzlasqrq81yf5

**시트 B (패널 13–24)**
- CDN: https://videocdn.pollo.ai/web-cdn/pollo/production/cmf20asu60gslb2k5fhlac2gn/ori/cmu8jl5lv4kzwjmpm415ydm08-0-604b1780f93d6cb3.png
- 뷰어: https://pollo.ai/v/cmu8jl5lv4kzwjmpm415ydm08

### 스타일 2 — 건축사전 (추론)

**시트 A (패널 1–12)**
- CDN: https://videocdn.pollo.ai/web-cdn/pollo/production/cmf20asu60gslb2k5fhlac2gn/ori/cmu8jlbmt4l4rcha8oc4j4ot2-0-81e589de9f88f4f9.png
- 뷰어: https://pollo.ai/v/cmu8jlbmt4l4rcha8oc4j4ot2

**시트 B (패널 13–24)**
- CDN: https://videocdn.pollo.ai/web-cdn/pollo/production/cmf20asu60gslb2k5fhlac2gn/ori/cmu8jlgyf4k8kftrguy66plp7-0-ca8c99a401af223a.png
- 뷰어: https://pollo.ai/v/cmu8jlgyf4k8kftrguy66plp7

### 스타일 3 — Avox지식 (추론)

**시트 A (패널 1–12)**
- CDN: https://videocdn.pollo.ai/web-cdn/pollo/production/cmf20asu60gslb2k5fhlac2gn/ori/cmu8jlmg44l127yygw1ttv20r-0-92a86028c87458d3.png
- 뷰어: https://pollo.ai/v/cmu8jlmg44l127yygw1ttv20r

**시트 B (패널 13–24)**
- CDN: https://videocdn.pollo.ai/web-cdn/pollo/production/cmf20asu60gslb2k5fhlac2gn/ori/cmu8jlqq14kvsnsq66eezbry5-0-19aca03663e08733.png
- 뷰어: https://pollo.ai/v/cmu8jlqq14kvsnsq66eezbry5

### 재생성용 taskId

| 시트 | taskId |
|---|---|
| S1-A | `cmu8jkmtd4kzmzlaswhvlnfe3` |
| S1-B | `cmu8jl5lp4kzvjmpmnm7u56h6` |
| S2-A | `cmu8jlbml4l4qcha8j35vgjqv` |
| S2-B | `cmu8jlgya4k8jftrgs9hnbncw` |
| S3-A | `cmu8jlmfp4l107yyg2p4hxxxh` |
| S3-B | `cmu8jlqpu4kvrnsq6bmwayqov` |

전체 프롬프트 원문은 각 taskId 로 `pollo_get_generation_status` 를 호출하면 그대로 회수된다.
