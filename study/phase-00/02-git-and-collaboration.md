---
title: "Git 기초와 협업 — CRLF 경고와 --no-ff 머지"
description: "AI 프로젝트에 필요한 git 명령을 정리합니다. add · commit · push의 일상 흐름과 브랜치 전략을 다루고, Windows에서 커밋마다 뜨는 LF will be replaced by CRLF 경고의 원인인 core.autocrlf 설정과 패스트포워드 머지가 브랜치 흔적을 지우는 문제까지 확인했습니다."
date: 2026-07-18
slug: git-basics-crlf-no-ff-merge
series: "AI Engineering from Scratch 한국어 학습 노트"
phase: 0
status: done
lesson: 2
tags: [환경설정, git, 버전관리, 트러블슈팅, Windows, AI엔지니어링]
keywords:
  - git 기초 명령어
  - "LF will be replaced by CRLF"
  - core.autocrlf 설정
  - git merge --no-ff 차이
  - 패스트포워드 머지란
  - gitignore 모델 체크포인트
  - git 브랜치 전략
  - gitattributes text eol lf
  - git config user.name 변경
---

# Git 기초와 협업 — CRLF 경고와 `--no-ff` 머지

> 버전 관리는 선택이 아닙니다. 모든 실험, 모든 모델, 여기서 만드는 모든 레슨이 추적됩니다.

| | |
|---|---|
| **유형** | Learn |
| **언어** | -- |
| **선수 지식** | Phase 0, Lesson 01 |
| **소요 시간** | 약 30분 |
| **원문** | [`phases/00-setup-and-tooling/02-git-and-collaboration`](../../phases/00-setup-and-tooling/02-git-and-collaboration/docs/en.md) |

## 학습 목표

- git 신원을 설정하고 add · commit · push의 일상 흐름을 사용한다
- main을 망가뜨리지 않고 실험을 격리하도록 브랜치를 만들고 병합한다
- 모델 체크포인트와 대용량 바이너리를 제외하는 `.gitignore`를 작성한다
- `git log`로 커밋 이력을 훑어 프로젝트가 어떻게 변해 왔는지 파악한다

## 왜 필요한가

앞으로 20개 Phase에 걸쳐 수백 개의 코드 파일을 작성하게 됩니다. 버전 관리가 없으면 작업을 잃고, 되돌릴 수 없는 것을 망가뜨리고, 다른 사람과 협업할 방법이 없습니다.

git이 도구이고, GitHub이 코드가 사는 곳입니다. 이 레슨은 이 과정에 필요한 만큼만 다루며, 그 이상은 다루지 않습니다.

## 개념

```
작업 디렉터리 --(git add)--> 스테이징 영역 --(git commit)--> 로컬 저장소
                                                              |
                                                    (git push) v
                                                          리모트(GitHub)
                                                              |
        작업 디렉터리 <--(git pull)-- 로컬 저장소 <--(git fetch)--
```

기억할 것은 셋입니다.

1. 자주 저장한다 (`git commit`)
2. 리모트로 밀어 올린다 (`git push`)
3. 실험은 브랜치에서 한다 (`git checkout -b experiment`)

## 구현

### 1단계 — git 설정

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

### 2단계 — 일상 작업 흐름

```bash
git status
git add file.py
git commit -m "Add perceptron implementation"
git push origin main
```

### 3단계 — 실험용 브랜치

```bash
git checkout -b experiment/new-optimizer

# ... 변경하고 커밋 ...

git checkout main
git merge experiment/new-optimizer
```

### 4단계 — 이 과정 저장소로 작업하기

```bash
git clone https://github.com/rohitg00/ai-engineering-from-scratch.git
cd ai-engineering-from-scratch

git checkout -b my-progress
# 레슨을 진행하며 코드를 커밋
git push origin my-progress
```

## 활용

이 과정에 필요한 명령은 정확히 이만큼입니다.

| 명령 | 쓰는 때 |
|---|---|
| `git clone` | 과정 저장소 받기 |
| `git add` + `git commit` | 작업 저장 |
| `git push` | GitHub에 백업 |
| `git checkout -b` | main을 건드리지 않고 시도해 보기 |
| `git log --oneline` | 한 일 돌아보기 |

여기까지입니다. 이 과정에서 rebase, cherry-pick, submodule은 필요하지 않습니다.

## 연습문제

1. 이 저장소를 클론하고 `my-progress` 브랜치를 만들어 파일을 하나 커밋한 뒤 푸시한다
2. 모델 체크포인트 파일(`.pt`, `.pth`, `.safetensors`)을 제외하는 `.gitignore`를 작성한다
3. `git log --oneline`으로 이 저장소의 커밋 이력을 보고 레슨이 어떻게 추가돼 왔는지 읽는다

## 핵심 용어

| 용어 | 흔한 설명 | 실제 의미 |
|---|---|---|
| 커밋(commit) | "저장" | 특정 시점 프로젝트 전체의 스냅숏 |
| 브랜치(branch) | "복사본" | 커밋을 가리키는 포인터. 작업하면 같이 앞으로 움직인다 |
| 머지(merge) | "코드 합치기" | 한 브랜치의 변경을 다른 브랜치에 적용하는 것 |
| 리모트(remote) | "클라우드" | 다른 곳에 호스팅된 저장소 사본(GitHub, GitLab) |

---

## 확인된 문제와 해결

이 레슨은 `code/` 디렉터리가 없는 **Learn 타입**이라 실행할 코드가 없습니다. 대신 레슨의 명령을 이 저장소에서 직접 확인했습니다.

### `warning: LF will be replaced by CRLF` 경고가 커밋마다 뜹니다

이 저장소에서 커밋할 때마다 반복해서 나타납니다.

```
warning: in the working copy of 'study/README.md', LF will be replaced by CRLF
the next time Git touches it
```

원인은 git 설정입니다.

```bash
$ git config core.autocrlf
true
```

Windows의 git 기본값인 `core.autocrlf=true`는 **체크아웃할 때 LF를 CRLF로, 커밋할 때 CRLF를 LF로** 변환합니다. 저장소 안에는 항상 LF로 저장되므로 협업에는 문제가 없고, 위 경고는 "지금 워킹 트리의 이 파일은 LF인데 다음에 git이 건드리면 CRLF가 된다"는 안내입니다.

**해결** — 경고 자체는 정상 동작이므로 무시해도 됩니다. 거슬리면 다음 중 하나를 씁니다.

```bash
git config core.autocrlf input   # 커밋 시 LF 변환만, 체크아웃 시 변환 안 함
git config advice.addIgnoredFile false   # 경고 억제 (동작은 그대로)
```

크로스 플랫폼 저장소라면 `.gitattributes`에 `* text=auto eol=lf`를 두어 설정에 의존하지 않게 하는 편이 낫습니다.

### `git merge`와 `git merge --no-ff`의 차이 — 패스트포워드는 브랜치 흔적을 지웁니다

레슨은 다음을 제시합니다.

```bash
git checkout main
git merge experiment/new-optimizer
```

이 형태는 갈라진 이력이 없으면 **패스트포워드**로 병합되어 브랜치가 있었다는 사실이 이력에서 사라집니다. 이 저장소는 `--no-ff`를 써서 병합 커밋을 항상 남깁니다.

```bash
git merge --no-ff develop-<slug>
```

결과를 비교하면 차이가 분명합니다.

```
$ git log --oneline --graph -6
*   735914c Merge branch 'develop-atlas-registration'
|\
| * d42dcd4 chore(atlas): Atlas 프로젝트 등록 및 ledger 기반 추적 연결
|/
*   98a9d49 Merge branch 'develop-study-progress'
|\
| * 55bd2dd feat(study): 진행 상태를 디스크에서 파생하는 study_progress.py 추가
|/
```

작업 단위가 하나의 덩어리로 남아 나중에 통째로 되돌리기 쉽습니다. 패스트포워드였다면 커밋들이 직선으로 섞여 경계가 사라집니다.

또한 레슨 2단계의 `git push origin main`은 main에 직접 커밋하는 흐름을 전제합니다. 이 저장소는 `develop-<slug>` 브랜치에서 작업하고 `--no-ff`로 병합하므로, 그대로 따르지 않습니다.

### 연습문제 2는 이미 충족돼 있습니다

`.gitignore`를 확인하면 요구 항목이 이미 들어 있습니다.

```
46:checkpoints/
49:*.pt
50:*.pth
52:*.safetensors
```

새로 작성할 필요 없이, 왜 이 확장자들이 제외 대상인지만 확인하면 됩니다. 모델 가중치는 수백 MB에서 수십 GB이고 바이너리라 diff가 무의미합니다. 한 번 커밋되면 이후 삭제해도 이력에 영원히 남아 클론이 무거워집니다.

### git 신원이 계정 규약과 어긋납니다

1단계의 `user.name` 설정과 관련해 현재 값을 확인했습니다.

```bash
$ git config user.name
sinwoo
$ git config user.email
<개인-메일주소>
```

계정 규약상 정체성은 **slnu21**이며 구 이름은 쓰지 않기로 돼 있습니다. 지금 이 저장소의 커밋은 `sinwoo` 명의로 기록되고 있습니다.

**해결** — 통일하려면 다음을 실행합니다. 이미 쌓인 커밋의 명의는 바뀌지 않으며, 이력 재작성은 비가역이므로 별도 판단이 필요합니다.

```bash
git config --global user.name "slnu21"
```
