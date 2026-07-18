# 개발 환경

> 도구가 사고의 틀을 만듭니다. 한 번 세팅하되, 제대로 세팅합니다.

| | |
|---|---|
| **유형** | Build |
| **언어** | Python, Node.js, Rust |
| **선수 지식** | 없음 |
| **소요 시간** | 약 45분 |
| **원문** | [`phases/00-setup-and-tooling/01-dev-environment`](../../phases/00-setup-and-tooling/01-dev-environment/docs/en.md) |

## 학습 목표

- Python 3.11+, Node.js 20+, Rust 툴체인을 처음부터 설치한다
- 재현 가능한 빌드를 위해 가상 환경과 패키지 매니저를 구성한다
- CUDA/MPS로 GPU 접근을 검증하고 테스트 텐서 연산을 돌린다
- 시스템·패키지·런타임·AI 라이브러리의 네 층 구조를 이해한다

## 왜 필요한가

앞으로 Python, TypeScript, Rust, Julia를 넘나들며 200개가 넘는 레슨을 지나가게 됩니다. 환경이 깨져 있으면 **모든 레슨이 개념 학습이 아니라 툴링과의 싸움**이 됩니다.

대부분은 환경 설정을 건너뜁니다. 그리고 import 오류, 버전 충돌, 없는 CUDA 드라이버를 디버깅하는 데 몇 시간을 씁니다. 이 비용은 레슨 수만큼 곱해지므로, 한 번에 제대로 치르는 편이 쌉니다.

## 개념 — 네 개의 층

AI 개발 환경은 네 층으로 이루어집니다.

```
4. AI/ML 라이브러리   PyTorch, JAX, transformers
3. 언어 런타임        Python 3.11+, Node 20+, Rust, Julia
2. 패키지 매니저      uv, pnpm, cargo, juliaup
1. 시스템 기반        OS, 셸, git, 에디터, GPU 드라이버
```

각 층은 아래 층에 의존합니다. 그래서 **설치는 아래에서 위로** 진행합니다.

이 구조가 실전에서 갖는 의미는 진단 순서입니다. 증상은 대개 위층에서 나타나지만 원인은 아래층에 있습니다. `torch`가 설치되지 않는 문제의 실제 원인이 1층의 GPU 드라이버이거나 3층의 Python 버전인 경우가 흔합니다. 4층만 반복해서 건드리면 해결되지 않습니다.

## 구현

### 1단계 — 시스템 기반

```bash
# macOS
xcode-select --install
brew install git curl wget

# Ubuntu/Debian
sudo apt update && sudo apt install -y build-essential git curl wget

# Windows
wsl --install -d Ubuntu-24.04
```

> **주의 (Windows) — WSL2가 필수는 아닙니다**
>
> 원문은 Windows에서 WSL2를 전제하지만, git·Node.js·Rust는 네이티브 Windows에서도 정상 동작합니다. 실제로 이 환경에서 네이티브로 `git 2.54.0` · `Node v24.15.0` · `cargo 1.96.1`이 모두 확인됐습니다.
>
> 판단 기준은 이렇습니다. **네이티브 Windows**는 GPU를 드라이버 그대로 쓰고 설정이 단순하지만, 레슨의 셸 스크립트(`curl | sh` 형태)가 그대로 돌지 않아 손으로 옮겨야 합니다. **WSL2**는 레슨 명령을 그대로 쓸 수 있지만 GPU 패스스루 설정이 한 겹 더 붙습니다.
>
> 대부분의 레슨은 Python 코드라 네이티브로 충분합니다. Phase 17(인프라·프로덕션)의 컨테이너·배포 레슨에서 WSL2가 필요해질 수 있습니다.

### 2단계 — uv로 Python 설치

`pip` 대신 `uv`를 씁니다. 가상 환경 생성과 패키지 설치를 한 도구가 처리하고, 속도가 `pip`의 10~100배입니다.

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh

uv python install 3.12
uv venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate

uv pip install numpy matplotlib jupyter
```

검증:

```python
import sys
print(f"Python {sys.version}")

import numpy as np
print(f"NumPy {np.__version__}")
a = np.array([1, 2, 3])
print(f"Vector: {a}, dot product with itself: {np.dot(a, a)}")
```

> **주의 (Windows) — `curl | sh` 설치 스크립트**
>
> 위 설치 줄은 POSIX 셸용입니다. PowerShell에서는 다음을 씁니다.
>
> ```powershell
> powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
> ```
>
> `winget install --id=astral-sh.uv`도 동작합니다.

### 3단계 — pnpm으로 Node.js 설치

TypeScript 레슨(에이전트, MCP 서버, 웹 앱)에 필요합니다.

```bash
curl -fsSL https://fnm.vercel.app/install | bash
fnm install 22
fnm use 22

npm install -g pnpm
node -e "console.log('Node', process.version)"
```

### 4단계 — Rust 설치

성능이 중요한 레슨(추론, 시스템)에 쓰입니다.

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

rustc --version
cargo --version
```

### 5단계 — Julia (선택)

수학 비중이 큰 레슨용입니다. Phase 1에서만 쓰이므로 나중에 설치해도 됩니다.

```bash
curl -fsSL https://install.julialang.org | sh
julia -e 'println("Julia ", VERSION)'
```

### 6단계 — GPU 설정

```bash
nvidia-smi

uv pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
```

```python
import torch
print(f"CUDA available: {torch.cuda.is_available()}")
if torch.cuda.is_available():
    print(f"GPU: {torch.cuda.get_device_name(0)}")
```

GPU가 없어도 대부분의 레슨은 CPU에서 동작합니다. 학습 비중이 큰 레슨은 Google Colab이나 클라우드 GPU를 씁니다.

### 7단계 — 전체 검증

```bash
python phases/00-setup-and-tooling/01-dev-environment/code/verify.py
```

## 활용

설치한 환경이 각 Phase에서 어떻게 쓰이는지입니다.

| 언어 | 사용처 | 패키지 매니저 |
|---|---|---|
| Python | Phase 1–12 (ML, DL, NLP, 비전, 오디오, LLM) | uv |
| TypeScript | Phase 13–17 (도구, 에이전트, 스웜, 인프라) | pnpm |
| Rust | Phase 12, 15–17 (성능이 중요한 시스템) | cargo |
| Julia | Phase 1 (수학 기초) | Pkg |

## 산출물

이 레슨은 누구나 돌려서 자기 환경을 점검할 수 있는 검증 스크립트를 만듭니다. `outputs/prompt-env-check.md`에는 AI 어시스턴트가 환경 문제를 진단하도록 돕는 프롬프트가 들어 있습니다.

## 연습문제

1. 검증 스크립트를 실행하고 실패한 항목을 고친다
2. 이 과정을 위한 Python 가상 환경을 만들고 PyTorch를 설치한다
3. 네 개 언어 각각으로 "hello world"를 작성하고 실행한다

---

## 확인된 문제와 해결

이 환경(Windows 11 · Python 3.12.10 · RTX 2060)에서 실제로 실행하며 확인한 사항입니다.

### `python3`는 스크립트를 실행하지 않고 종료 코드 0을 냅니다

가장 위험한 함정입니다. 원문과 CI는 `python3`를 쓰지만, Windows에서 `python3`는 Microsoft Store 앱 실행 별칭(`WindowsApps/python3`)으로 연결됩니다.

```bash
$ python3 scripts/audit_lessons.py
Python
(exit=0)
```

스크립트가 **실행되지 않았는데 종료 코드는 0**입니다. 검사를 통과한 것으로 오인하기 쉽습니다.

```bash
$ which python3
/c/Users/raltl/AppData/Local/Microsoft/WindowsApps/python3   # 스텁
$ which python
/c/Users/raltl/AppData/Local/Programs/Python/Python312/python   # 실제 인터프리터
```

**해결** — Windows에서는 `python`을 씁니다. 별칭을 아예 끄려면 `설정 → 앱 → 고급 앱 설정 → 앱 실행 별칭`에서 `python3.exe`를 해제합니다.

### 콘솔 인코딩 오류 — `cp949`

이 레포의 Python 스크립트는 출력에 em-dash(`—`)를 씁니다. Windows 콘솔 기본 인코딩이 `cp949`라 그대로 실행하면 실패합니다.

```
UnicodeEncodeError: 'cp949' codec can't encode character '—'
```

**해결** — 환경 변수로 표준 출력 인코딩을 지정합니다.

```bash
PYTHONIOENCODING=utf-8 python scripts/audit_lessons.py
```

PowerShell에서는 `$env:PYTHONIOENCODING = "utf-8"`, 또는 콘솔 코드 페이지를 `chcp 65001`로 바꿉니다.

### `verify.py`의 CUDA `[FAIL]`은 GPU 없음을 뜻하지 않습니다

검증 스크립트 실행 결과입니다.

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

CUDA가 `[FAIL]`이지만 GPU는 존재합니다.

```
$ nvidia-smi --query-gpu=name,driver_version,memory.total --format=csv
NVIDIA GeForce RTX 2060, 591.86, 6144 MiB
```

원인은 `verify.py`의 검사 구조입니다.

```python
GPU_CHECKS = [
    ("PyTorch", lambda: __import__("torch"), None),
    ("CUDA", lambda: __import__("torch").cuda.is_available(), ...),
]
```

`run_check`가 `except Exception`으로 감싸므로, `torch`가 없을 때 발생하는 `ModuleNotFoundError`가 그대로 삼켜져 `[FAIL]`로 표시됩니다. 즉 이 스크립트에서 **CUDA 실패는 "GPU 없음"이 아니라 "PyTorch 미설치"일 수 있습니다.**

**해결** — GPU 존재 여부는 `nvidia-smi`로 직접 확인합니다. `torch` 설치 후 재실행하면 정확한 값이 나옵니다.

### VRAM 6GB는 Phase 10 이후의 제약이 됩니다

RTX 2060의 VRAM은 6GB입니다. Phase 1–9의 학습용 소형 모델은 문제없지만, Phase 10(LLM 밑바닥부터) 이후로는 이 용량이 상한이 됩니다.

**대응** — 양자화(quantization), `LoRA` 계열 경량 파인튜닝, 배치 크기 축소, 또는 Colab·클라우드 GPU로 우회합니다. Phase 10에 도달하기 전에 알아 두면 모델 선택이 달라집니다.

### 이 환경에서 남은 작업

- `uv` 미설치 → 설치 후 `uv venv`
- `numpy` · `matplotlib` · `jupyter` 미설치
- `torch` 미설치 → CUDA 12.4 빌드로 설치
- 이후 `verify.py` 재실행하여 **7/7** 확인
