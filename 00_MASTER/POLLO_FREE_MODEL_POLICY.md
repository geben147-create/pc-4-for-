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

## 영상 — 무료 없음 (15개 모델 전수 확인)

| 모델 | discountCost |
|---|---|
| `bytedance/seedance-pro-fast` | 4 |
| `pollo-ai/pollo-v1-6` | 5 |
| `google/veo3-1-lite` | 8 |
| `bytedance/seedance-2-0-mini` | 10 |
| `pixverse/pixverse-v3-5` | 10 |
| `pixverse/pixverse-v4` | 10 |
| `vidu/viduq3-turbo` | 10 |
| `pollo-ai/pollo-v1-5` | 10 |
| `bytedance/seedance-2-0-fast` | 12 |
| `alibaba/wan-v2-1` | 20 |
| `luma/luma-ray-2-flash` | 20 |
| `kling-ai/kling-v2-5-turbo` | 30 |
| `minimax/video-01` | 35 |
| `xai/grok-imagine-video` | 40 |
| `google/gemini-omni-flash` | 50 |

**`discountCost == 0` 인 영상 모델은 하나도 없다.**

따라서 **절대 무료 규칙 하에서 영상 생성은 불가능하다.** 최저가도 4크레딧이다.

### 영상이 필요해지면 선택지

1. **규칙 유지 → 영상 생성 안 함.** 이미지만 만들고 움직임은 편집 단계에서 처리
   (Ken Burns 팬/줌, 레이어 패럴랙스, After Effects). 플랫 벡터 스타일은 이 방식이 오히려 자연스럽다.
2. **사용자가 규칙을 명시적으로 푸는 경우에만** `seedance-pro-fast` (4크레딧) 부터 검토.
   현재 잔액 8,982 기준 약 2,245클립 분량이지만, **사용자 승인 없이는 쓰지 않는다.**

---

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
