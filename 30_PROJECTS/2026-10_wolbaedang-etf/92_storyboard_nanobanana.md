# 스토리보드 시트 2차 — 나노 바나나 프로

1차(씨드림 5.0 Pro)가 **디테일이 부족하다**는 피드백을 받아 모델과 프롬프트를 둘 다 교체했다.

## 무엇을 바꿨나

| 항목 | 1차 (Seedream 5.0 Pro) | 2차 (Nano Banana Pro) |
|---|---|---|
| 모델 | `bytedance/seedream-5-0-pro` | `google/nano-banana-pro` |
| 장당 비용 | 2크레딧 (할인가) | **18크레딧** (할인 없음) |
| 6장 합계 | 12크레딧 (실측 차감 확인) | 견적 108크레딧, **실제 차감 0** (아래 참조) |
| 프롬프트 길이 상한 | 2,000자 | 제한 없음 (2,800자 사용 확인) |
| 패널 묘사 | 한 줄 요약 (~70자) | **전경·중경·배경 + 인물 반응 + 소품**까지 (~180자) |
| 완성도 지시 | 없음 | `fully finished illustration, no rough sketches, no empty panels, no blank space` 명시 |
| 병렬 제한 | — | **동시 4건**. 5번째부터 `Parallel task limit reached` |

## 프롬프트 보강 원칙

디테일이 떨어졌던 원인은 모델보다 **프롬프트가 비어 있던 것**이 컸다.
`"두 개의 막대그래프"` 같은 지시는 모델에게 나머지를 전부 위임하는 것과 같다. 2차에서는 패널마다 다음을 강제했다.

1. **깊이 3층** — 무엇이 앞에, 가운데, 뒤에 있는가
2. **인물의 반응** — 블롭이 올려다보는지, 놀라는지, 자로 재는지
3. **소품의 상태** — 봉투가 기울어 있는지 닫혀 있는지, 다이얼을 손이 돌리고 있는지
4. **스타일별 고유 어휘**
   - 건축사전 → `leader lines with small dots`, `dimension arrows with end ticks`, `cross-hatching to indicate cut material`, `scale bar`, `enlarged inset detail`
   - Avox지식 → `hairline outlines`, `dashed average line`, `soft drop shadow`, `confident negative space`, `precise alignment`

건축사전 스타일은 이 대본과 특히 잘 맞는다. **단면도(cutaway)** 가 "커버드콜은 엔진 위에 얹는 장치"를 설명하는 가장 정확한 도해 형식이기 때문이다.
패널 18에서 엔진 단면 + 상단 볼트 체결 모듈 + 하향 배출 덕트 + 클램프 확대 인서트까지 지시한 것이 그 이유다.

## taskId (2차)

| 시트 | 스타일 | 패널 | taskId |
|---|---|---|---|
| S1-A | 일본 플랫 카툰 | 1–12 | `cmu8jphvg4lturtf3662g5eop` |
| S1-B | 일본 플랫 카툰 | 13–24 | `cmu8jpxli4ljdq8j1mlz5aszi` |
| S2-A | 건축사전 | 1–12 | `cmu8jq8iy4kd7sc8qgpz4wssi` |
| S2-B | 건축사전 | 13–24 | `cmu8jqhtp4ly9htdgk5r47zwx` |
| S3-A | Avox지식 | 1–12 | `cmu8jwjh74lq6mjhnazth8sye` |
| S3-B | Avox지식 | 13–24 | `cmu8jwqqp4m8s10von0j07cec` |

## 미해결

- **스타일 2·3은 여전히 이름 추론.** `A건축사전style` / `Avox지식style` 폴더가 로컬 Windows 경로라 이 세션에서 열 수 없다.
  해당 폴더 이미지를 채팅에 직접 올리면 레퍼런스 기반으로 다시 뽑는다. 지금 결과는 "이름으로 상상한 버전"이다.
- **이미지 육안 검수 불가.** `videocdn.pollo.ai` egress 차단(403)으로 컨테이너에 내려받지 못한다. 링크를 열어 확인해야 한다.

---

## 생성 결과 (2차, Nano Banana Pro)

### 스타일 1 — 일본 심플 플랫 카툰
- 시트 A (1–12): https://pollo.ai/v/cmu8jphvo4ltvrtf31at4p2cb
  - PNG: https://videocdn.pollo.ai/web-cdn/pollo/production/cmf20asu60gslb2k5fhlac2gn/ori/cmu8jphvo4ltvrtf31at4p2cb-0-3f7011e6dbb24fc0.png
- 시트 B (13–24): https://pollo.ai/v/cmu8jpxlp4ljeq8j1ls1df5of
  - PNG: https://videocdn.pollo.ai/web-cdn/pollo/production/cmf20asu60gslb2k5fhlac2gn/ori/cmu8jpxlp4ljeq8j1ls1df5of-0-20c3e81f957a0160.png

### 스타일 2 — 건축사전 (추론)
- 시트 A (1–12): https://pollo.ai/v/cmu8jq8j44kd8sc8qqi31hn4k
  - PNG: https://videocdn.pollo.ai/web-cdn/pollo/production/cmf20asu60gslb2k5fhlac2gn/ori/cmu8jq8j44kd8sc8qqi31hn4k-0-2f10e4b32a179fd4.png
- 시트 B (13–24): https://pollo.ai/v/cmu8jqhtt4lyahtdgmrawiw28
  - PNG: https://videocdn.pollo.ai/web-cdn/pollo/production/cmf20asu60gslb2k5fhlac2gn/ori/cmu8jqhtt4lyahtdgmrawiw28-0-454dcfafba43ff6a.png

### 스타일 3 — Avox지식 (추론)
- 시트 A (1–12): https://pollo.ai/v/cmu8jwjhd4lq7mjhntxtjsvzl
  - PNG: https://videocdn.pollo.ai/web-cdn/pollo/production/cmf20asu60gslb2k5fhlac2gn/ori/cmu8jwjhd4lq7mjhntxtjsvzl-0-ac92440ed7cbb20d.png
- 시트 B (13–24): https://pollo.ai/v/cmu8jwqqv4m8t10voqgsumihg
  - PNG: https://videocdn.pollo.ai/web-cdn/pollo/production/cmf20asu60gslb2k5fhlac2gn/ori/cmu8jwqqv4m8t10voqgsumihg-0-ea7905f9433cbe42.png

## 1차 대 2차 비교용 (같은 내용, 같은 패널 순서)

| 스타일 | 패널 | 1차 씨드림 (2크레딧) | 2차 나노바나나 (18크레딧) |
|---|---|---|---|
| 1 | 1–12 | https://pollo.ai/v/cmu8jkmu54kznzlasqrq81yf5 | https://pollo.ai/v/cmu8jphvo4ltvrtf31at4p2cb |
| 1 | 13–24 | https://pollo.ai/v/cmu8jl5lv4kzwjmpm415ydm08 | https://pollo.ai/v/cmu8jpxlp4ljeq8j1ls1df5of |
| 2 | 1–12 | https://pollo.ai/v/cmu8jlbmt4l4rcha8oc4j4ot2 | https://pollo.ai/v/cmu8jq8j44kd8sc8qqi31hn4k |
| 2 | 13–24 | https://pollo.ai/v/cmu8jlgyf4k8kftrguy66plp7 | https://pollo.ai/v/cmu8jqhtt4lyahtdgmrawiw28 |
| 3 | 1–12 | https://pollo.ai/v/cmu8jlmg44l127yygw1ttv20r | https://pollo.ai/v/cmu8jwjhd4lq7mjhntxtjsvzl |
| 3 | 13–24 | https://pollo.ai/v/cmu8jlqq14kvsnsq66eezbry5 | https://pollo.ai/v/cmu8jwqqv4m8t10voqgsumihg |

> 2차는 모델과 프롬프트를 **동시에** 바꿨으므로, 이 비교만으로는 개선이 모델 덕인지 프롬프트 덕인지 분리되지 않는다.
> 비용 차이가 9배이므로, 다음 라운드에서 **2차 프롬프트 + 씨드림** 조합을 한 장 뽑아보면 그 구분이 가능하다.

## 다음 라운드에 확인할 것 (대조 실험)

2차에서 모델과 프롬프트를 동시에 바꿨기 때문에 개선 원인이 분리되지 않았다.
비용 차가 9배(18 vs 2크레딧)이므로 이 구분은 실용적으로 중요하다.

| 조건 | 모델 | 프롬프트 | 비용 | 상태 |
|---|---|---|---|---|
| A (1차) | 씨드림 5.0 Pro | 간략 (~70자/패널) | 2 | 완료 |
| B (2차) | 나노바나나 Pro | 촘촘 (~180자/패널) | 18 | 완료 |
| **C (대조군)** | **씨드림 5.0 Pro** | **촘촘 (2차와 동일)** | **2** | **미실행** |

C가 B에 근접하면 → 앞으로 씨드림 + 촘촘한 프롬프트로 간다 (9배 절약).
C가 A에 가까우면 → 모델 차이가 실제이므로 나노바나나 비용을 지불할 가치가 있다.

한 장(2크레딧)이면 판정 가능하다.

## 실제 과금 관측 (주의)

| 시점 | 잔액 |
|---|---|
| 작업 시작 | 8,994 |
| 씨드림 6장 후 | 8,982 (**-12**, 견적과 일치) |
| 나노바나나 6장 후 | 8,982 (**-0**, 견적 108과 불일치) |

`pollo_estimate_generation_cost` 는 nano-banana-pro 를 장당 18크레딧으로 보고했으나
6장 생성 후 잔액이 움직이지 않았다. Ultra 구독이 이 모델을 커버하거나, 과금이 지연 반영되는 것으로 보인다.

**이것을 "무료 확정"으로 받아들이지 말 것.** 한 번의 관측이고 지연 과금 가능성이 남아 있다.
다음 세션에서 잔액을 다시 확인해 -108이 뒤늦게 반영됐는지 검증해야 한다.
