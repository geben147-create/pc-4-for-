# 스타일 변형 3종 + 무료 영상 실증

피드백: **"너무 귀여운 느낌"**. 40~60대 투자자 대상 설명 영상에 블롭 캐릭터는 톤이 맞지 않는다.
`PROJECT_BIBLE` 에 "다큐멘터리형 설명, 흥분한 주식 유튜브 톤 아님" 이라고 적어놓고 그림이 그걸 따르지 않았다.

말로 정하지 않고 **같은 장면(CUT_18 엔진 위 장치)을 귀여움 단계별로 3개** 생성해 비교한다.

| 변형 | 방향 | 링크 |
|---|---|---|
| **기존** | 블롭 캐릭터, 점눈, 볼터치 — 너무 귀여움 | https://pollo.ai/v/cmu8lf7k24r573fjn2txsi461 |
| **A** | 캐릭터 완전 제거. 사물만. 신문 경제면 일러스트 | https://pollo.ai/v/cmu8m618a4u1agpnd57ynauq6 |
| **B** | 얼굴 없는 성인 실루엣 1명. 성인 비율 | https://pollo.ai/v/cmu8m658m4sufd8fi4uolotz3 |
| **C** | 정밀 아이소메트릭. 엔지니어링 도해 | https://pollo.ai/v/cmu8m6akh4tyngsppzs65hb7o |

## 권장

**A 또는 C.**

이 영상은 사물 비유(엔진·봉투·저울·유리천장·다이얼)만으로 전 구간이 설명되게 설계돼 있다.
캐릭터가 서사를 지고 있지 않으므로 없어도 성립한다. 오히려 캐릭터가 있으면
시선이 사물에서 분산되고, 컷마다 캐릭터 일관성을 유지하는 비용이 붙는다.

B의 실루엣은 **사람이 반드시 필요한 컷에만** 쓰는 것이 낫다.
해당 컷은 사실상 하나다 — 6:45 "30대 직장인 vs 은퇴를 앞둔 투자자".

---

# 무료 영상 파이프라인 실증 완료

| 항목 | 값 |
|---|---|
| 모델 | `minimax/minimax-h3` |
| 설정 | length 5, resolution 768P, **I2V (이미지 입력)** |
| 입력 스틸 | CUT_18 (엔진 위 장치) |
| 결과 | https://pollo.ai/v/cmu8m5vux4t0zmjhntauhayli |
| MP4 | https://videocdn.pollo.ai/web-cdn/pollo/production/cmf20asu60gslb2k5fhlac2gn/ori/cmu8m5vux4t0zmjhntauhayli-0-efcd6e95e5cbd49a.mp4 |
| 비용 | **0크레딧** (잔액 8,982 → 8,982 불변) |

사용한 영상 프롬프트 (`VIDEO_PROMPT_AGENT` 규칙대로 피사체 동작 우선, 카메라 1개):

```
The large flywheel on the brass engine rotates slowly and steadily, and the thin
stream of gold light venting downward from the valve into the envelope below
pulses gently as it flows. Camera: a slow push-in straight along the optical axis,
easing to a full stop. Lighting and colour remain exactly as they are.
Single continuous take, no cuts, no scene change, no new objects, no text appearing.
```

**이미지 → 영상 전 구간이 무료로 돌아간다는 것이 확인됐다.**

---

## 과금 누적 실측

| 시점 | 잔액 | 증감 |
|---|---|---|
| 세션 시작 | 8,994 | |
| 씨드림 이미지 6장 | 8,982 | **−12** (유료) |
| 나노바나나 이미지 누적 17장 | 8,982 | −0 |
| minimax-h3 영상 1개 | 8,982 | −0 |

유료로 쓴 것은 **초기 씨드림 6장(12크레딧)뿐**이다. 이후 전부 무료.

---

## 보류된 컷

CUT_06 / CUT_08 / CUT_20 은 기존(귀여운) 스타일로 이미 생성됐으나
스타일 변경이 확정되면 **폐기하고 새 스타일로 재생성**한다. 링크를 남기지 않는다.
