# 폴로 무료 모델 정책 — 절대 규칙

> **사용자 지시: 유료 모델 절대 금지. 무료 모델만 사용.**
> 생성 전 반드시 `pollo_estimate_generation_cost` 로 확인하고, **`discountCost == 0` 인 모델만** 쓴다.

---

## 비용 필드 읽는 법 (실측으로 검증됨)

`pollo_estimate_generation_cost` 는 4개 필드를 준다.

```json
{"cost":18, "singleCost":18, "discountCost":0, "discountSingleCost":18}
```

**실제로 차감되는 값은 `discountCost` 다.** `cost` 가 아니다.

| 검증 | 모델 | cost | discountCost | 실제 잔액 변화 |
|---|---|---|---|---|
| 6장 생성 | `bytedance/seedream-5-0-pro` | 4 | **2** | 8,994 → 8,982 (**−12** = 2×6) |
| 6장 생성 | `google/nano-banana-pro` | 18 | **0** | 8,982 → 8,982 (**−0**) |

`discountCost` 가 실측과 정확히 일치한다. **`cost` 를 보고 판단하면 틀린다.**

---

## 이미지 — 무료 있음

| 모델 | discountCost | 판정 |
|---|---|---|
| `google/nano-banana-pro` | **0** | ✅ **무료. 기본 선택** |
| `google/nano-banana` | **0** | ✅ 무료 |
| `bytedance/seedream-5-0-pro` | 2 | ❌ 유료 |
| `bytedance/seedream-4-5` | 0* | ⚠️ `discountSingleCost` 가 4로 불일치. 검증 전까지 사용 보류 |

**결론: 이미지는 `nano-banana-pro` 를 쓴다.** 성능도 가장 높고 무료다.

> 주의: 초기에 씨드림이 싸고(2) 나노바나나가 비싸다(18)고 판단했으나 **반대였다.**
> `cost` 필드만 보고 `discountCost` 를 놓친 탓이다. 이 문서의 존재 이유.

---

## 영상 — 무료 있음 (조건부)

### ✅ 무료 설정 — 이것만 쓴다

```
brand:      minimax
model:      minimax-h3
length:     5          <- 5초 고정. 10초는 유료
resolution: 768P       <- 768P 고정. 480p/2K 는 미검증
```

`discountCost: 0`. **이미지 입력(I2V)을 붙여도 0** 이므로 승인된 스틸을 첫 프레임으로 쓸 수 있다.

### 무료 경계 실측

| 설정 | discountCost | 판정 |
|---|---|---|
| `minimax-h3` 5초 768P | **0** | ✅ 무료 |
| `minimax-h3` 5초 768P + image (I2V) | **0** | ✅ 무료 |
| `minimax-h3` 10초 768P | 50 | ❌ 유료 |
| `minimax-h3` 1080P | — | 지원 안 함 (480p / 768p / 2K 만) |

**5초 + 768P 조합에서만 무료다.** 길이나 해상도를 바꾸면 과금된다.

### 유료 영상 모델 (참고용, 사용 금지)

| 모델 | discountCost |
|---|---|
| `bytedance/seedance-pro-fast` | 4 |
| `pollo-ai/pollo-v1-6` | 5 |
| `google/veo3-1-lite` | 8 |
| `bytedance/seedance-2-0-mini` / `pixverse-v3-5` / `pixverse-v4` / `vidu/viduq3-turbo` / `pollo-v1-5` | 10 |
| `bytedance/seedance-2-0-fast` | 12 |
| `alibaba/wan-v2-1` / `luma/luma-ray-2-flash` | 20 |
| `kling-ai/kling-v2-5-turbo` | 30 |
| `minimax/video-01` | 35 |
| `xai/grok-imagine-video` | 40 |
| `google/gemini-omni-flash` | 50 |

### ⚠️ 이 문서가 한 번 틀렸던 이유

초기 조사에서 "무료 영상 모델 없음" 이라고 결론냈다. **틀렸다.**
원인: `minimax/video-01` (35크레딧) 만 확인하고 같은 브랜드의 `minimax-h3` 를 놓쳤고,
길이·해상도 파라미터를 바꿔가며 확인하지 않았다.

**교훈: 모델 하나가 유료라고 그 브랜드 전체를 유료로 판정하지 말 것.**
같은 브랜드 안에서도 모델별로 다르고, **같은 모델도 길이·해상도 조합에 따라 무료/유료가 갈린다.**
무료 여부를 단정하기 전에 브랜드의 모든 모델 x 허용된 파라미터 조합을 확인한다.

## 생성 전 체크리스트

```
[ ] pollo_estimate_generation_cost 호출했는가
[ ] discountCost 를 확인했는가 (cost 아님)
[ ] discountCost == 0 인가
[ ] 아니면 → 생성하지 말고 사용자에게 보고
[ ] 생성 후 pollo_account_status 로 잔액이 안 움직였는지 확인
```

## 기타 운영 제약

- **동시 생성 4건 제한.** 5번째부터 `Parallel task limit reached`
- **프롬프트 길이**: 씨드림 2,000자 / 나노바나나 제한 없음 (2,800자 확인)
- **`videocdn.pollo.ai` egress 차단(403)** — 이 세션에서 결과 이미지를 내려받아 검수할 수 없다.
  링크를 사용자가 직접 열어야 한다.
