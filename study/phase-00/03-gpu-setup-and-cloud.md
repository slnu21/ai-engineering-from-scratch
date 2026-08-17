---
title: "GPU 확인과 클라우드 GPU — CUDA · Colab · VRAM 계산"
description: "AI 학습에 GPU가 필요해지는 시점과 로컬 GPU · Google Colab · 클라우드 GPU를 비교합니다. uv가 Checked 3 packages만 찍었을 때 CUDA 빌드가 실제로 깔렸는지 확인하는 법, 벤치마크가 Speedup 1x로 나오는 원인, VRAM 기준 최대 모델 크기가 학습에서는 1/4로 줄어드는 이유를 실측으로 정리했습니다."
date: 2026-08-17
slug: gpu-setup-cloud-cuda-colab-vram
series: "AI Engineering from Scratch 한국어 학습 노트"
phase: 0
lesson: 3
status: done
tags: [환경설정, CUDA, PyTorch, GPU, 트러블슈팅, AI엔지니어링]
keywords:
  - torch.cuda.is_available 확인
  - "ModuleNotFoundError: No module named 'torch'"
  - "Checked 3 packages in"
  - uv venv 활성화 PowerShell
  - torch 2.6.0+cu124 확인
  - uv pip install --reinstall torch
  - GPU CPU 속도 차이 벤치마크
  - GPU Speedup 1x 원인
  - torch.cuda.synchronize 이유
  - cuBLAS 첫 호출 느림
  - VRAM 모델 크기 계산
  - fp16 파라미터당 2바이트
  - Adam 옵티마이저 메모리 4배
  - RTX 2060 6GB 학습 한계
---

# GPU 확인과 클라우드 GPU — CUDA · Colab · VRAM 계산

> CPU로 학습해도 배우는 데는 충분합니다. 제대로 학습시키려면 GPU가 필요합니다.

| | |
|---|---|
| **유형** | Build |
| **언어** | Python |
| **선수 지식** | Phase 0, Lesson 01 |
| **소요 시간** | 약 45분 |
| **원문** | [`phases/00-setup-and-tooling/03-gpu-setup-and-cloud`](../../phases/00-setup-and-tooling/03-gpu-setup-and-cloud/docs/en.md) |

## 학습 목표

- `nvidia-smi`와 PyTorch의 CUDA API로 로컬 GPU 사용 가능 여부를 확인한다
- 무료 클라우드 실험용으로 Google Colab에 T4 GPU를 설정한다
- CPU와 GPU에서 행렬 곱을 벤치마크하고 속도 차이를 측정한다
- `fp16` 어림 규칙으로 VRAM에 올릴 수 있는 최대 모델 크기를 추정한다

## 왜 필요한가

Phase 1–3의 레슨은 대부분 CPU에서 문제없이 돌아갑니다. 하지만 `CNN`·트랜스포머(transformer)·`LLM`을 학습시키기 시작하는 Phase 4 이후로는 GPU 가속이 필요합니다. CPU에서 8시간 걸리는 학습이 GPU에서는 10분입니다.

선택지는 셋입니다. 로컬 GPU, 클라우드 GPU, 그리고 무료인 Google Colab.

## 개념

```
선택지:

1. 로컬 NVIDIA GPU
   비용: $0 (이미 갖고 있음)
   설정: CUDA + cuDNN 설치
   적합: 상시 사용, 큰 데이터셋

2. Google Colab (무료 등급)
   비용: $0
   설정: 없음
   적합: 짧은 실험, 집에 GPU가 없을 때

3. 클라우드 GPU (Lambda, RunPod, Vast.ai)
   비용: 시간당 $0.20~2.00
   설정: SSH 접속 후 설치
   적합: 본격적인 학습, 대형 모델
```

세 선택지를 가르는 축은 두 가지입니다. **얼마나 오래 붙잡고 있는가**와 **VRAM이 얼마나 필요한가**입니다. 로컬 GPU는 시간당 비용이 0이므로 오래 돌릴수록 유리하지만 VRAM은 산 시점에 고정됩니다. 클라우드는 그 반대로, VRAM을 돈으로 살 수 있지만 켜 둔 시간만큼 계속 나갑니다. Colab 무료 등급은 둘 다 아니고 세션이 끊기는 제약이 있어, 결과를 남기는 학습보다 확인용 실험에 맞습니다.

## 구현

### 선택 1 — 로컬 NVIDIA GPU

GPU가 있는지 확인합니다.

```bash
nvidia-smi
```

CUDA 지원 PyTorch를 설치한 뒤 확인합니다.

```python
import torch

print(f"CUDA available: {torch.cuda.is_available()}")
print(f"CUDA version: {torch.version.cuda}")
if torch.cuda.is_available():
    print(f"GPU: {torch.cuda.get_device_name(0)}")
    print(f"Memory: {torch.cuda.get_device_properties(0).total_memory / 1e9:.1f} GB")
```

`nvidia-smi`가 보여 주는 CUDA 버전은 **드라이버가 지원하는 상한**이고, `torch.version.cuda`는 **설치된 PyTorch가 빌드된 CUDA 버전**입니다. 서로 다른 값이어도 정상이며, 드라이버 쪽이 같거나 높으면 동작합니다.

### 선택 2 — Google Colab

1. [colab.research.google.com](https://colab.research.google.com)에 접속합니다
2. 런타임 > 런타임 유형 변경 > T4 GPU
3. `!nvidia-smi`를 실행해 확인합니다

이 과정의 노트북을 그대로 Colab에 올려서 쓸 수 있습니다.

### 선택 3 — 클라우드 GPU

Lambda Labs, RunPod, Vast.ai를 쓰는 경우입니다.

```bash
ssh user@your-gpu-instance

pip install torch torchvision torchaudio
python -c "import torch; print(torch.cuda.get_device_name(0))"
```

### GPU가 없어도 괜찮습니다

대부분의 레슨은 CPU에서 동작합니다. GPU가 필요한 레슨은 그렇다고 명시하고 Colab 링크를 함께 제공합니다.

```python
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using: {device}")
```

이 한 줄을 코드 앞머리에 두고 이후 텐서(tensor)와 모델을 전부 `device`로 보내면, 같은 코드가 GPU 유무와 무관하게 돌아갑니다. 이 과정의 GPU 레슨들이 쓰는 관용구입니다.

## 구현 — GPU vs CPU 벤치마크

```python
import torch
import time

size = 5000

a_cpu = torch.randn(size, size)
b_cpu = torch.randn(size, size)

start = time.time()
c_cpu = a_cpu @ b_cpu
cpu_time = time.time() - start
print(f"CPU: {cpu_time:.3f}s")

if torch.cuda.is_available():
    a_gpu = a_cpu.to("cuda")
    b_gpu = b_cpu.to("cuda")

    torch.cuda.synchronize()
    start = time.time()
    c_gpu = a_gpu @ b_gpu
    torch.cuda.synchronize()
    gpu_time = time.time() - start
    print(f"GPU: {gpu_time:.3f}s")
    print(f"Speedup: {cpu_time / gpu_time:.0f}x")
```

`torch.cuda.synchronize()`가 앞뒤로 한 번씩 들어가는 이유가 이 코드의 핵심입니다. CUDA 커널 실행은 **비동기**라서 `a_gpu @ b_gpu`는 GPU에 작업을 넣기만 하고 곧바로 반환합니다. 동기화 없이 시간을 재면 실제 연산 시간이 아니라 작업을 큐에 넣는 시간을 재게 되고, 말이 안 되는 속도 향상 수치가 나옵니다.

레슨 디렉터리의 `code/gpu_check.py`가 위 확인 절차와 벤치마크, 그리고 VRAM 기준 모델 크기 추정까지 하나로 묶어 둔 스크립트입니다.

## 연습문제

1. 위 벤치마크를 실행해 CPU와 GPU 시간을 비교한다
2. GPU가 없다면 Google Colab에서 실행해 비교한다
3. GPU 메모리가 얼마인지 확인하고 올릴 수 있는 최대 모델 크기를 추정한다 (어림 규칙: `fp16` 기준 파라미터당 2바이트)

## 핵심 용어

| 용어 | 흔한 설명 | 실제 의미 |
|---|---|---|
| `CUDA` | "GPU 프로그래밍" | GPU에서 코드를 실행하게 해 주는 NVIDIA의 병렬 컴퓨팅 플랫폼 |
| `VRAM` | "GPU 메모리" | GPU에 붙은 전용 메모리. 시스템 RAM과 별개이며 모델 크기의 상한을 정한다 |
| `fp16` | "반정밀도" | 16비트 부동소수점. `fp32`의 절반 메모리를 쓰면서 정확도 손실은 대체로 미미하다 |
| `Tensor Core` | "행렬 연산 전용 하드웨어" | 행렬 곱에 특화된 GPU 코어. 일반 코어보다 4~8배 빠르다 |

---

## 확인된 문제와 해결

이 환경(Windows 11 · Python 3.12.13 · RTX 2060 6GB · 드라이버 591.86 · PyTorch 2.6.0+cu124)에서 실제로 실행하며 확인한 사항입니다.

### `Checked 3 packages`는 CUDA 빌드가 설치됐다는 뜻이 아닙니다

`--index-url`로 CUDA 빌드를 지정해 설치했을 때의 출력입니다.

```
> uv pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
Checked 3 packages in 1.13s
```

`uv`가 **요구 조건이 이미 충족됐다고 판단해 아무것도 하지 않았다**는 뜻입니다. 문제는 이 판단이 패키지 이름과 버전 범위만 본다는 점입니다. 이전에 CPU 전용 `torch`가 깔려 있었다면 `--index-url`은 무시되고 그대로 통과하며, 출력만 봐서는 구분되지 않습니다.

**해결** — 설치된 빌드를 직접 확인합니다. 버전 문자열의 `+cu124` 접미사가 CUDA 빌드라는 표시입니다.

```
> uv pip list
torch                     2.6.0+cu124
torchaudio                2.6.0+cu124
torchvision               0.21.0+cu124
```

접미사가 없는 `2.6.0`이면 CPU 전용 빌드입니다. 이 경우 `--reinstall`을 붙여야 실제로 교체됩니다.

```powershell
uv pip install --reinstall torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
```

### 설치는 됐는데 `ModuleNotFoundError: No module named 'torch'` — 인터프리터가 두 개입니다

`uv pip install`이 성공한 직후 PowerShell에서 `python`을 띄우면 `torch`가 없다고 나옵니다.

```
> python
Python 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] on win32
>>> import torch
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'torch'
```

**`uv pip install`은 가상 환경을 활성화하지 않아도 현재 디렉터리의 `.venv`를 자동으로 찾아 거기에 설치합니다.** 활성화 단계를 건너뛰어도 설치가 성공하기 때문에, 셸의 `python`은 계속 시스템 인터프리터를 가리키는 상태로 남습니다.

버전 숫자가 결정적인 단서입니다.

```
> (Get-Command python).Source
C:\Users\<사용자명>\AppData\Local\Programs\Python\Python312\python.exe
> python -c "import sys; print(sys.version.split()[0])"
3.12.10
> .\.venv\Scripts\python.exe -c "import sys; print(sys.version.split()[0])"
3.12.13
```

`uv venv`가 만든 환경은 시스템 Python을 재사용하지 않고 **uv가 관리하는 별도 Python**을 씁니다. 그래서 마이너 버전까지 다릅니다. `3.12.10`이 보이면 시스템 쪽, `3.12.13`이 보이면 `.venv` 쪽입니다.

**해결** — 셋 중 하나를 씁니다.

```powershell
.\.venv\Scripts\activate                  # 활성화. 프롬프트 앞에 (.venv)가 붙습니다
uv run python phases/.../gpu_check.py     # 활성화 없이 그때그때
.\.venv\Scripts\python.exe script.py      # 경로를 직접 지정
```

> **주의 (Windows) — PowerShell에서 `activate.bat`은 조용히 실패합니다**
>
> 확장자 없는 `.\.venv\Scripts\activate`는 PowerShell이 `activate.ps1`로 해석하므로 정상 동작합니다. 하지만 `.bat`을 명시하면 별도 `cmd` 프로세스에서 실행되고 끝나, **오류 없이 활성화도 되지 않습니다.**
>
> ```
> > .\.venv\Scripts\activate.bat
> > python -c "import sys; print(sys.version.split()[0])"
> 3.12.10        # 그대로입니다
> ```
>
> 실패 신호가 전혀 없다는 점이 위험합니다. 활성화 여부는 프롬프트의 `(.venv)` 표시나 버전 숫자로 확인합니다.

### `Speedup: 1x` — GPU가 CPU보다 전혀 빠르지 않게 나옵니다

`gpu_check.py`를 설치 후 처음 실행한 결과입니다.

```
CPU matrix multiply (4000x4000): 0.297s
GPU matrix multiply (4000x4000): 0.285s
Speedup: 1x
```

GPU는 정상적으로 잡혀 있는데(`CUDA available: True`) 속도 이득이 없습니다. 그런데 같은 스크립트를 그대로 다시 돌리면 값이 달라집니다.

```
--- run 1 ---   GPU matrix multiply (4000x4000): 0.062s   Speedup: 4x
--- run 2 ---   GPU matrix multiply (4000x4000): 0.065s   Speedup: 3x
```

즉 `1x`는 **설치 후 첫 실행에서만** 나오고 재현되지 않습니다. 첫 실행에는 프로세스 밖에 남는 일회성 초기화 비용(드라이버 수준의 커널 캐시 생성)이 얹히기 때문입니다. 벤치마크 결과로 읽으면 안 되는 값입니다.

**해결** — 스크립트를 한 번 더 실행한 값을 씁니다. 첫 실행 결과는 버립니다.

### `torch.cuda.synchronize()`를 넣었는데도 첫 호출이 느립니다

위에서 재현된 `3~4x`도 이 GPU의 실제 성능은 아닙니다. 워밍업을 넣고 여러 번 측정하면 값이 다시 갈립니다.

```
CPU                     : 0.328s
GPU (first call)        : 0.061s   speedup 5.4x
GPU (warmed, 10-run avg): 0.027s   speedup 12.4x
```

레슨 코드는 동기화를 올바르게 넣었으므로 큐잉 시간을 재는 실수는 없습니다. 남은 원인은 **프로세스마다 첫 GEMM 호출에 붙는 비용**입니다. cuBLAS 핸들 생성과 커널 모듈 지연 로딩이 첫 행렬 곱 안에서 함께 일어나고, 이것이 연산 자체보다 큽니다. 측정값의 절반 이상이 초기화입니다.

**해결** — 측정 전에 같은 연산을 몇 번 버리고, 여러 번의 평균을 씁니다.

```python
for _ in range(3):
    _ = a_gpu @ b_gpu
torch.cuda.synchronize()

times = []
for _ in range(10):
    start = time.time()
    _ = a_gpu @ b_gpu
    torch.cuda.synchronize()
    times.append(time.time() - start)
print(f"{sum(times) / len(times):.3f}s")
```

레슨의 `1x`·`3x`·`12x`가 모두 같은 하드웨어에서 나온 값입니다. **벤치마크 수치는 측정 방법이 만든다**는 것이 이 레슨에서 실제로 확인되는 부분입니다.

### `Estimated max model size (fp16): ~3B parameters`는 학습에 쓸 수 없는 숫자입니다

`gpu_check.py`의 마지막 줄은 VRAM을 파라미터당 2바이트로 나눈 값입니다.

```python
params_fp16 = vram_gb * 1e9 / 2
```

이 계산에는 **가중치밖에 들어 있지 않습니다.** 학습에는 기울기와 옵티마이저 상태가 추가로 올라갑니다. `fp32` 파라미터 100M짜리 모델로 단계별 실측한 값입니다.

```
parameters              : 100.0M (fp32)
1) weights only         :   384.1 MB
2) + gradients          :   785.6 MB
3) + Adam states        :  1553.8 MB

peak allocated          :  1937.9 MB
multiplier vs weights   : 4.0x
```

`Adam`은 파라미터마다 1차·2차 모멘트를 각각 저장하므로, 가중치 1배 + 기울기 1배 + 옵티마이저 상태 2배 = **4배**가 됩니다. 여기에 활성값(activation)이 배치 크기에 비례해 더 붙습니다(위 실측에서 peak가 최종 할당량보다 384MB 높은 부분).

**해결** — 용도에 따라 나눠 읽습니다. 6GB 기준으로 `~3B`는 추론 상한에 가까운 값이고, `Adam`으로 학습한다면 그 1/4인 **7억 파라미터 수준**이 출발점입니다. 활성값과 단편화를 감안하면 더 내려갑니다. 이 격차를 줄이는 수단이 양자화(quantization) · `LoRA` · 혼합 정밀도(mixed precision) · 배치 크기 축소이며, Phase 10 이후에서 다룹니다.
