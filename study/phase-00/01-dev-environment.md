# 환경 설정을 건너뛰면, 나중에 두 배로 갚습니다

> Phase 0 · Lesson 01 — 개발 환경. 435개 레슨을 버틸 바닥을 까는 일.

**원문** [`phases/00-setup-and-tooling/01-dev-environment`](../../phases/00-setup-and-tooling/01-dev-environment/docs/en.md) · **공부한 날** 2026-07-18

---

환경 설정 레슨은 누구나 건너뜁니다. 저도 그랬습니다. "일단 코드부터 돌려 보고
안 되면 그때 깔지" — 그렇게 시작하면 정작 배우려던 개념 대신 `ModuleNotFoundError`
와 CUDA 버전 충돌을 붙잡고 저녁을 다 씁니다. 배운 건 없고 짜증만 남습니다.

이 레슨은 그 시간을 앞으로 당겨서 한 번에 치르자고 말합니다. 435개 레슨을 지나갈
거라면, 바닥이 흔들릴 때 드는 비용이 435배로 곱해지니까요.

## 네 개의 층 — 아래에서 위로

레슨이 제일 먼저 하는 건 기술 나열이 아니라 **구조 그리기**입니다. AI 개발 환경을
네 층으로 봅니다.

```
4. AI/ML 라이브러리   PyTorch, JAX, transformers
3. 언어 런타임        Python 3.11+, Node 20+, Rust, Julia
2. 패키지 매니저      uv, pnpm, cargo, juliaup
1. 시스템 기반        OS, 셸, git, 에디터, GPU 드라이버
```

**위 층은 아래 층에 전부 의존합니다.** 그래서 설치는 반드시 아래에서 위로.
이게 왜 중요하냐면 — 사람들이 환경을 고칠 때 대개 4층부터 건드리기 때문입니다.
`torch` 가 안 깔린다고 `pip install torch` 를 열 번 반복하는데, 진짜 원인은 1층의
드라이버이거나 3층의 파이썬 버전인 경우가 많습니다. **증상은 위에서 나고 원인은
아래에 있습니다.**

## `pip` 대신 `uv` — 10배가 아니라 100배

레슨은 `pip` 대신 `uv` 를 씁니다. 가상 환경 생성과 패키지 설치를 한 도구가
처리하고, 속도가 `pip` 의 10~100배라는 게 이유입니다.

```bash
uv python install 3.12
uv venv
uv pip install numpy matplotlib jupyter
```

솔직히 처음엔 "패키지 매니저 하나 바꾼다고 뭐가 달라지나" 싶었는데, 435개 레슨을
돌면서 환경을 몇 번이고 새로 만들 걸 생각하면 — 매번 몇 분씩 기다리는 게 결국
몇 시간이 됩니다. 도구 선택이 곧 시간 예산입니다.

## 직접 돌려 본 결과 — 4/7

레슨이 마지막에 주는 `verify.py` 를 제 PC 에서 그대로 돌렸습니다.

```bash
python phases/00-setup-and-tooling/01-dev-environment/code/verify.py
```

```
Core:
  [PASS] Python 3.10+ (Python 3.12.10)
  [FAIL] NumPy
  [FAIL] Matplotlib
  [FAIL] Jupyter
  [PASS] Git
  [PASS] Node.js
  [PASS] Rust (cargo)

GPU (optional):
  [FAIL] PyTorch
  [FAIL] CUDA

Result: 4/7 core checks passed
```

**4/7.** 시스템 층(git · Node 24.15 · cargo 1.96)은 이미 서 있는데, 정작 파이썬
과학 스택이 통째로 비어 있었습니다. 3층은 있는데 4층이 없는 상태 — 딱 레슨이
말한 그 그림입니다.

## 스크립트가 거짓말을 한 지점 — CUDA

여기서 걸린 게 있습니다. `verify.py` 는 CUDA 를 `[FAIL]` 로 찍었습니다. 그래서
"내 PC 엔 GPU 가 없나 보다" 하고 넘어갈 뻔했는데, 직접 확인해 보니 —

```
NVIDIA GeForce RTX 2060, 드라이버 591.86, 6144 MiB
```

**GPU 는 멀쩡히 있었습니다.** `verify.py` 의 CUDA 검사는 `torch.cuda.is_available()`
을 호출하는데, `torch` 자체가 안 깔려 있으니 `import` 에서 터지고, 그 예외를
그대로 삼켜서 `[FAIL]` 로 찍은 것이었습니다. 즉 이 스크립트에서 **"CUDA 실패"는
"GPU 없음"이 아니라 "PyTorch 없음"일 수도 있습니다.**

검증 스크립트를 읽지 않고 결과만 믿었으면 GPU 를 놀릴 뻔했습니다. 도구가 주는
빨간 글씨를 그대로 받아들이지 말 것 — 첫 레슨에서 배운 게 환경 설정이 아니라
이거였습니다.

## 6GB 라는 천장

다만 RTX 2060 의 VRAM 은 **6GB** 입니다. Phase 1~9 정도의 학습용 모델은 충분히
돌지만, Phase 10(LLM 밑바닥부터) 이후로 가면 이 숫자가 벽이 됩니다. 그때는
양자화(quantization)나 `LoRA` 같은 경량화, 아니면 Colab · 클라우드 GPU 로
우회해야 합니다. **지금 알아 두는 것과 Phase 10 에서 터진 뒤에 아는 건 다릅니다.**

## 윈도우에서 걸린 것 — cp949

레슨에 없지만 제 환경에서 실제로 터진 문제입니다. 이 레포의 파이썬 스크립트들은
출력에 em-dash(`—`)를 쓰는데, 윈도우 콘솔 기본 인코딩이 `cp949` 라 그대로 돌리면
터집니다.

```
UnicodeEncodeError: 'cp949' codec can't encode character '—'
```

해결은 환경 변수 하나입니다.

```bash
PYTHONIOENCODING=utf-8 python scripts/audit_lessons.py
```

`python3` 가 아니라 `python` 을 써야 하는 것도 같은 결입니다 — 윈도우에서
`python3` 는 Microsoft Store 스텁이라 엉뚱한 데로 갑니다. **레슨은 macOS · 리눅스를
기준으로 쓰였고, 그 간극은 제가 메워 가며 읽어야 합니다.**

## 다음에 할 일

- `uv` 설치 → `uv venv` → `numpy` · `matplotlib` · `jupyter`
- CUDA 12.4 빌드로 `torch` 설치 후 `verify.py` 재실행, **7/7** 확인
- 그 다음 Lesson 02

---

건너뛰고 싶었던 레슨에서 정작 건진 건 설치 명령어가 아니라, **빨간 `[FAIL]` 이
항상 진실은 아니라는 것**이었습니다. 바닥을 까는 일은 원래 이렇게 재미없고, 이렇게
자주 뒤통수를 칩니다.
