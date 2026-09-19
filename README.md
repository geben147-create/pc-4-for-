# 영상 제작 프롬프트 시스템 (Prompt-First Pipeline)

이미지·영상을 **생성하기 전에**, 글(프롬프트) 단계에서 오류를 전부 잡아내는 시스템.
생성 비용이 들어가기 전 단계에서 싸게 고치는 것이 목적이다.

## 파이프라인

```
대본 → [S 검사] → 장면표 → [SC 검사] → 이미지 프롬프트 → [IP 검사]
                                                    ↓
                                          영상 프롬프트 → [VP 검사]
                                                    ↓
                                    ████ READY_TO_GENERATE ████
                                                    ↓
                                          실제 이미지 → 실제 영상 → 편집 → QC
```

**생성하는 에이전트와 검사하는 에이전트를 분리한다.** 생성자는 자기 결과를 좋게 평가하는 편향이 있다.

## 파일 구조

| 경로 | 역할 |
|---|---|
| `00_MASTER/MASTER_CHECKLIST.md` | 전 단계 1:1 체크리스트 (S / SC / IP / VP / G) — 모든 에이전트가 참조하는 단일 기준 |
| `00_MASTER/PROJECT_BIBLE.md` | 이 영상의 비주얼 바이블 (팔레트·앵커 사물·인물 ID·금지사항) |
| `10_AGENTS/IMAGE_PROMPT_AGENT.md` | **이미지 프롬프트를 쓰는 프롬프트** |
| `10_AGENTS/IMAGE_PROMPT_VALIDATOR.md` | IP01~IP13 검사 프롬프트 |
| `10_AGENTS/VIDEO_PROMPT_AGENT.md` | **영상 프롬프트를 쓰는 프롬프트** |
| `10_AGENTS/VIDEO_PROMPT_VALIDATOR.md` | VP01~VP14 검사 프롬프트 |
| `20_SCHEMA/*.json` | 출력 JSON 스키마 (기계 검증용) |
| `30_PROJECTS/2026-10_wolbaedang-etf/` | 2026년 10월 월배당 ETF 영상 (대본 + 적용 예시) |

## 사용 순서

1. `PROJECT_BIBLE.md`를 영상별로 먼저 채운다. (팔레트·앵커·인물 ID가 없으면 연속성 검사가 전부 무의미해진다)
2. 장면표(Scene Table)를 `IMAGE_PROMPT_AGENT`에 넣는다 → 이미지 프롬프트 JSON 산출
3. 같은 JSON을 `IMAGE_PROMPT_VALIDATOR`에 넣는다 → FAIL/PARTIAL만 수정
4. 통과한 이미지 프롬프트를 `VIDEO_PROMPT_AGENT`에 넣는다 → 영상 프롬프트 JSON 산출
5. `VIDEO_PROMPT_VALIDATOR` 통과
6. `READY_TO_GENERATE = true` 일 때만 실제 생성 시작

## 통과 기준

```
FAIL    = 0
PARTIAL = 0
PASS-B  ≤ 전체 항목의 20%
```

## Obsidian / GraphRAG는 나중

규칙이 실전 3~5편으로 굳은 뒤에 붙인다. 아직 굳지 않은 규칙을 예쁘게 연결해두면 수정 비용만 커진다.
