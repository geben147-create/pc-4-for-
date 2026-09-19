# 24컷 생성 진행표

스타일: 확정 A (사물만) · 모델: `google/nano-banana-pro` (무료) · 16:9 · 한글 핵심 단어 좌상단

## 완료

| # | 핵심 단어 | 링크 |
|---|---|---|
| 1 | 매달 들어오는 돈 | https://pollo.ai/v/cmu8mf7ya4u1glvhpgn9yldns |
| 10 | 상승 제한 | https://pollo.ai/v/cmu8mfc394uo9czgib9gecvgo |
| 18 | 커버드콜 | https://pollo.ai/v/cmu8mf1204tqz12w9n5qumbfl |
| 2 | 은행 vs ETF | https://pollo.ai/v/cmu8n30cg4wwxsigc44ep7blb |
| 3 | 월배당 ETF | https://pollo.ai/v/cmu8n34ym4wv0gpnd7dyioe0o |
| 4 | 분배율이 크다 | https://pollo.ai/v/cmu8n39wk4v9xftrgkcsmbrfx |
| 5 | 이 돈의 출처 | https://pollo.ai/v/cmu8n3el44wvkgpndcu56rz58 |
| 18-en | COVERED CALL (영문 대조군) | https://pollo.ai/v/cmu8mf4b84trhnsq689m3whs2 |

| 6 | 콜옵션 매도 | https://pollo.ai/v/cmu8n7yd64xb1vvczdkr3q6ci |
| 7 | 옵션 프리미엄 | https://pollo.ai/v/cmu8n83go4vx6zd4lrl6zyy2u |
| 8 | 공짜 점심은 없다 | https://pollo.ai/v/cmu8n88ah4x9kgsppph0uzuqi |
| 9 | 횡보장 | https://pollo.ai/v/cmu8n8ctj4w7512w9uxzlh26b |

| 11 | 분배율과 수익률 | https://pollo.ai/v/cmu8ndeso4x25c70yqslph12v |
| 12 | 총수익률 | https://pollo.ai/v/cmu8ndixq4wmkg8eqwm4asdnc |
| 13 | 가격 변화까지 | https://pollo.ai/v/cmu8ndnno4wxt7yygpalkp4x2 |
| 14 | 얼마나 파느냐 | https://pollo.ai/v/cmu8ndswp4x1bw8iq1pfam7cu |

| 15 | 전략이 다르다 | https://pollo.ai/v/cmu8nipb84wryl0u9lf1i7gdw |
| 16 | 무엇을 포기하나 | https://pollo.ai/v/cmu8niuqj4wl313ite1m60vje |
| 17 | 기초자산 | https://pollo.ai/v/cmu8nize74wsq4okyoxxkxfop |
| 19 | 보는 순서 | https://pollo.ai/v/cmu8nj3rz4x21g8eqkqtgc0b3 |

| 20 | 고정 이자가 아니다 | https://pollo.ai/v/cmu8nob9w4xkinsq60iwfs4tw |
| 21 | 원금 감소 가능 | https://pollo.ai/v/cmu8nog1n4yj9gpndsedb5k4l |
| 22 | 목적이 다르다 | https://pollo.ai/v/cmu8nolcv4xwflvhpt131mkyk |
| 23 | 세 가지 숫자 | https://pollo.ai/v/cmu8nopug4xb5l0u9tytp0cf7 |

**23/24 완료**

## 생성 중

| 종류 | 내용 | taskId |
|---|---|---|
| 이미지 | 24번 내 목적에 맞는 ETF | `cmu8nu7794ymy14mmgcaijn2u` |
| 영상 | 1번 봉투에서 금화가 계속 쏟아짐 | `cmu8nubol4xif13it9v1korhm` |
| 영상 | 8번 저울이 더 기울고 큐브가 미끄러짐 | `cmu8nudd94yfes8bl33d7tr8j` |
| 영상 | 10번 곡선이 계속 오르고 천장에서 맥동 | `cmu8nufjb4yh53fjnipq5cf9r` |

---

# 영상화 규칙 (I2V)

| 항목 | 값 |
|---|---|
| 모델 | `minimax/minimax-h3` — **무료** |
| 설정 | `length: 5`, `resolution: 768P`, 이미지 입력 |
| 첫 프레임 | 승인된 컷 PNG 를 그대로 사용 |

## 한글 보호 지시 (필수)

화면에 한글이 박혀 있으므로 I2V 가 글자를 녹인다. **모든 영상 프롬프트에 다음 문장을 반드시 넣는다.**

```
The Korean text in the upper left remains perfectly static,
unchanged and undistorted throughout.
...
no text changing or forming.
```

## 움직임 원칙

- **피사체 동작을 문장 맨 앞에** 쓴다. 카메라부터 쓰면 피사체가 정지한다
- **카메라 동작 1개.** push-in 또는 locked-off
- **locked-off 를 전체의 30% 이상** 쓴다. 전부 움직이면 강조가 사라진다
- 움직이는 것은 컷당 하나. 금화 낙하 / 저울 기울기 / 플라이휠 회전 / 곡선 맥동

## 남은 배치

이미지 24컷 완료 후 각 컷을 `minimax-h3` 5초 768P I2V(무료)로 영상화한다.

## 운영 메모

- 폴로 동시 생성 **4건 제한**. 배치는 반드시 4개씩
- 생성 후 `pollo_account_status` 로 잔액 불변 확인 (무료 규칙 준수 증빙)
- 이미지 육안 검수 불가(`videocdn` egress 차단) — 한글 품질 판정은 사용자가 한다
