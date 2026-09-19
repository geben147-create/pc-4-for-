# 스토리보드 시트 2차 — 나노 바나나 프로

1차(씨드림 5.0 Pro)가 **디테일이 부족하다**는 피드백을 받아 모델과 프롬프트를 둘 다 교체했다.

## 무엇을 바꿨나

| 항목 | 1차 (Seedream 5.0 Pro) | 2차 (Nano Banana Pro) |
|---|---|---|
| 모델 | `bytedance/seedream-5-0-pro` | `google/nano-banana-pro` |
| 장당 비용 | 2크레딧 (할인가) | **18크레딧** (할인 없음) |
| 6장 합계 | 12크레딧 | **108크레딧** |
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
| S3-A | Avox지식 | 1–12 | (병렬 제한으로 대기 후 제출) |
| S3-B | Avox지식 | 13–24 | (병렬 제한으로 대기 후 제출) |

## 미해결

- **스타일 2·3은 여전히 이름 추론.** `A건축사전style` / `Avox지식style` 폴더가 로컬 Windows 경로라 이 세션에서 열 수 없다.
  해당 폴더 이미지를 채팅에 직접 올리면 레퍼런스 기반으로 다시 뽑는다. 지금 결과는 "이름으로 상상한 버전"이다.
- **이미지 육안 검수 불가.** `videocdn.pollo.ai` egress 차단(403)으로 컨테이너에 내려받지 못한다. 링크를 열어 확인해야 한다.
