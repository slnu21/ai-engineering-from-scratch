# study — 한국어 학습 노트

이 커리큘럼을 한국어로 공부하며 남기는 노트입니다.

**원문 레슨의 자연스러운 한국어 판 + 실제로 확인한 주의점·오류 해결**로 구성합니다.
개인적인 감상이나 학습 경험 서사는 넣지 않습니다. 내용이 중심입니다.

## 이건 순수 번역이 아닙니다

`phases/**/docs/ko.md`가 아니라 `study/`에 따로 쌓는 이유입니다.

- `docs/ko.md`는 CONTRIBUTING 상 **`en.md`의 번역** 슬롯이고, "영어판과 같은
  구조를 유지하라"는 제약이 붙습니다. 업스트림 기여를 전제한 자리입니다.
- 여기 노트는 번역에 더해 **특정 환경(Windows · RTX 2060)에서 확인한 주의점과
  오류 해결**을 덧붙입니다. 이 부분은 환경 의존적이라 업스트림에 맞지 않습니다.

순수 번역을 기여하고 싶어지면 그때 `docs/ko.md`를 따로 만듭니다. 목적이 다릅니다.

## 자리

```
study/
├── README.md          이 파일          ┐
├── glossary-ko.md     용어 표기 기준    │ 인프라 문서
├── tags-ko.md         태그 · SEO 기준   │ (발행 대상 아님)
├── PROGRESS.md        생성물           ┘
├── 00-intro.md        시리즈 소개 — 루트 글
└── phase-NN/
    └── MM-lesson-slug.md                레슨 노트
```

**발행 대상은 두 종류입니다.** `phase-NN/`의 **레슨 노트**와, 루트에 두는 **루트 글**
(시리즈 소개처럼 특정 레슨에 속하지 않는 글)입니다. 루트 글은 `phase` · `lesson`
프론트매터가 없어도 되며, 그 외 규칙은 같습니다. 위 인프라 문서 4개는 검사·발행
대상에서 제외됩니다(`study_progress.py`의 `NON_POST_FILES`).

파일명은 원문 레슨 디렉터리 슬러그를 그대로 씁니다.
`phases/00-setup-and-tooling/01-dev-environment` → `study/phase-00/01-dev-environment.md`.

**슬러그가 정확해야 진행 계산에 잡힙니다.** 어긋나면 `study_progress.py`가
"짝 없는 노트"로 잡아 줍니다.

## 진행 상태

진행 상태는 **디스크에서 파생**됩니다. 노트 파일이 있으면 그 레슨은 완료입니다.
따로 체크할 목록이 없으므로 어긋날 수가 없습니다.

```bash
python scripts/study_progress.py             # 전체 요약 + 다음 레슨
python scripts/study_progress.py --phase 0   # 한 Phase를 레슨 단위로
python scripts/study_progress.py --write     # PROGRESS.md 재생성
python scripts/study_progress.py --json      # 기계용
```

공부를 시작할 때 먼저 돌려 어디까지 왔는지 확인하고, 노트를 추가한 뒤 `--write`로
`PROGRESS.md`를 갱신합니다. `PROGRESS.md`는 생성물이라 손으로 고치지 않습니다.

## 노트 한 편의 구조

`phase-00/01-dev-environment.md`가 기준 샘플입니다.

**0부 — SEO 프론트매터 (필수)**

블로그로 나가는 글이므로 모든 노트는 프론트매터로 시작합니다. 상세 기준은
[`tags-ko.md`](tags-ko.md).

```yaml
---
title: "Git 기초와 협업 — CRLF 경고와 --no-ff 머지"   # 60자 이내, 핵심 키워드를 앞에
description: "..."          # 80~200자. 검색 결과에 뜨는 문장
date: 2026-07-18
slug: git-basics-crlf-no-ff-merge                  # 영문 kebab-case
series: "AI Engineering from Scratch 한국어 학습 노트"
phase: 0
lesson: 2
tags: [환경설정, git, 버전관리, 트러블슈팅, Windows, AI엔지니어링]   # 통제 어휘 3~6개
keywords:                    # 롱테일 5개 이상. 에러 원문을 그대로 넣습니다
  - "LF will be replaced by CRLF"
  - core.autocrlf 설정
---
```

**한국어 SERP는 30~35자에서 잘립니다.** `title`은 60자를 넘기지 않되, 핵심
키워드가 앞 30자 안에 들어오게 배치합니다.

`python scripts/study_progress.py`가 프론트매터 누락 · 길이 초과 · 태그 개수를
검사합니다. `--strict`면 위반 시 exit 1.

**1부 — 레슨 본문 (원문 구조를 따라감)**

1. 제목 · 모토 · 메타 표(유형 · 언어 · 선수 지식 · 소요 시간 · 원문 링크)
   H1은 프론트매터 `title`과 같게 씁니다(원문 제목을 그대로 옮기지 않고,
   검색어를 담은 제목으로 바꾸는 유일한 지점입니다)
2. 학습 목표
3. 왜 필요한가 (The Problem)
4. 개념 (The Concept)
5. 구현 (Build It) — 단계별
6. 활용 (Use It)
7. 산출물 (Ship It)
8. 연습문제

원문에 없는 절을 만들지 않고, 원문에 있는 절을 빼지 않습니다.

**2부 — 확인된 문제와 해결**

`---`로 구분한 뒤, 실제로 실행하며 확인한 것만 적습니다. 항목마다:

- 무엇이 어떻게 잘못 보이는가 (실제 출력)
- 왜 그런가 (원인)
- **해결** — 구체적인 명령이나 설정

**2부의 소제목이 SEO 핵심입니다.** 사람들은 에러 메시지를 그대로 검색창에
붙여넣습니다. 각 항목 제목에 **에러 원문이나 증상 문장**을 넣습니다.

- 약함 — `### 콘솔 인코딩 오류`
- 강함 — ``### `UnicodeEncodeError: 'cp949' codec can't encode character` 해결``

**인라인 주의 블록.** 본문 흐름 중간에 경고가 필요하면 그 자리에 삽입합니다.

```markdown
> **주의 (Windows) — 제목**
>
> 내용.
```

## 규칙

- **문체는 기술 문서체.** `-습니다`체, 1인칭 배제, 감상 배제. 설명과 근거 위주.
- **키워드를 본문에 억지로 심지 않습니다.** SEO는 프론트매터 · 제목 · 소제목의
  구조로 처리합니다. 본문은 정확성이 우선입니다.
- **용어 병기가 곧 SEO입니다.** `어텐션(attention)` 표기는 한국어 검색과 영어
  검색을 한 문구로 동시에 잡습니다. 병기 정책을 지키는 것만으로 이득입니다.
- **용어는 `glossary-ko.md` 표를 따릅니다.** 표에 없으면 정책대로 정하고 표에 추가.
  병기는 글마다 첫 등장 1회.
- **코드 · 명령 · 에러 메시지 · API는 번역하지 않습니다.**
- **실행 결과는 실제 출력만.** 안 돌려 봤으면 그 사실을 적습니다. 창작 금지.
- **"확인된 문제"는 재현한 것만.** 있을 법한 문제를 추측으로 적지 않습니다.

## CI에 영향 없음

`build_catalog.py`와 `audit_lessons.py`는 `phases/` 아래 `en.md`만 봅니다.
`site/build.js`도 이 폴더를 읽지 않습니다. `study/`에 무엇을 쌓아도
`catalog.json` 드리프트나 감사 실패가 발생하지 않습니다.
