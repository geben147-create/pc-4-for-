# 개별 컷 (16:9) — 확정 스타일

12분할 시트에서 **개별 컷으로 분리**한 단계. 각 컷이 영상의 한 장면 시작 프레임이 된다.

| 항목 | 값 |
|---|---|
| 모델 | `google/nano-banana-pro` — **무료** (`discountCost: 0`) |
| 비율 | 16:9 (영상 규격) |
| 자막존 | 하단 18% 비움 |
| 텍스트 | 원칙적으로 전면 금지. 예외는 `A` `B` `CALL` 같은 단일 단어뿐 |

## 확정된 스타일 (레퍼런스 = 사용자 승인 시트)

```
flat vector cartoon illustration.
Thick perfectly even dark-navy outlines of consistent weight.
Completely flat fill colours, no gradients, no shading, no texture.
A rounded cream-white blob character with tiny black dot eyes,
small pink oval blush cheeks and a simple line mouth.
Soft mint-green or pale blue background.
Gold, teal and coral accents. Warm wood surfaces.
Clean, minimal, deadpan, cute.
```

이 블록은 **모든 컷에 글자 그대로 복사**한다. 바꾸면 캐릭터가 달라진다.

---

## 완성된 컷

| ID | 타임코드 | 대본 | 링크 |
|---|---|---|---|
| CUT_01 | 0:00 | 매달 돈이 들어오고 | https://pollo.ai/v/cmu8lf3pi4rnf9sm2266ykxwm |
| CUT_10 | 2:45 | B는 상승 수익 일부가 제한 | https://pollo.ai/v/cmu8lfblt4rdzrtf3sx3g3j3p |
| CUT_18 | 5:05 | 커버드콜은 엔진 위에 얹는 장치 | https://pollo.ai/v/cmu8lf7k24r573fjn2txsi461 |
| CUT_24 | 8:15 | 내 목적에 맞는 ETF를 찾는 겁니다 | https://pollo.ai/v/cmu8lffcg4qwbgyk6mf9bxunq |

### 생성 중

| ID | 타임코드 | 대본 | taskId |
|---|---|---|---|
| CUT_06 | 1:28 | 콜옵션을 다른 사람에게 판다 | `cmu8lkyef4ry7czgikg8lh29o` |
| CUT_08 | 2:00 | 공짜 점심은 좀처럼 없습니다 | `cmu8ll20q4qodftrgs9kulfoc` |
| CUT_20 | 5:50 | 분배금은 고정 이자가 아닙니다 | `cmu8ll5f44rjlzlasva14j1vx` |

---

## CUT_01 ↔ CUT_24 가 이 영상의 뼈대다

같은 봉투, 같은 책상, 다른 상태.

| | CUT_01 | CUT_24 |
|---|---|---|
| 봉투 | 넘어져 열림, 금화가 쏟아짐 | 평평히 닫힘, 정지 |
| 빛 | 좌상단에서 들어오는 따뜻한 빛 | 우측에서 들어오는 새벽빛 |
| 채도 | 높음 | 낮음 |
| 검은 모듈 | (없음) | 엔진 **옆에** 내려놓임 |
| 캐릭터 | 손을 들고 놀라 쳐다봄 | 손을 모으고 차분히 바라봄 |

**검은 모듈의 위치가 결론이다.** 영상 내내 엔진 **위**(CUT_18)에 있던 장치가 마지막에 **옆**으로 내려온다.
내레이션은 이걸 한 번도 말하지 않는다. 대본의 "순서가 뒤집힌 겁니다 → 이 순서로 봐야 합니다"가 배치 변화만으로 닫힌다.

---

## 과금 실측

| 시점 | 잔액 | 비고 |
|---|---|---|
| 세션 시작 | 8,994 | |
| 씨드림 6장 후 | 8,982 | **−12** (유료, 장당 2) |
| 나노바나나 시트 6장 후 | 8,982 | −0 |
| 나노바나나 개별컷 4장 후 | 8,982 | −0 |
| **누적 나노바나나 10장** | **8,982** | **−0 확정** |

10장 연속 0차감. `nano-banana-pro` 가 이 계정에서 무료라는 것이 관측으로 확정됐다.

---

## 영상 — 생성 안 함

무료 영상 모델이 없다 (15개 전수 확인, 최저 `seedance-pro-fast` 4크레딧).
절대 무료 규칙에 따라 **영상 생성을 하지 않는다.** 근거는 `00_MASTER/POLLO_FREE_MODEL_POLICY.md`.

대안: 이 플랫 벡터 스타일은 편집 단계 모션이 오히려 적합하다.
- 켄번즈 팬/줌 — 원본이 벡터풍이라 확대해도 깨지지 않는다
- 레이어 분리 후 패럴랙스 — 전경 금화 / 중경 봉투 / 배경 봉투열
- 요소 단위 애니메이션 — 금화 낙하, 저울 기울기, 플라이휠 회전
AI 영상 특유의 형태 뭉개짐이 없고, 캐릭터 일관성 문제도 발생하지 않는다.
