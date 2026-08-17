---
title: "GPU 확인과 클라우드 GPU — CUDA · Colab · VRAM 계산"
description: "AI 학습에 GPU가 필요해지는 시점과 로컬 GPU · Google Colab · 클라우드 GPU 세 선택지를 비교합니다. nvidia-smi와 torch.cuda.is_available()로 GPU를 확인하고, CPU 대비 행렬 곱 속도를 재고, VRAM에서 fp16 기준 최대 모델 크기를 어림하는 방법까지 정리했습니다."
date: 2026-08-17
slug: gpu-setup-cloud-cuda-colab-vram
series: "AI Engineering from Scratch 한국어 학습 노트"
phase: 0
lesson: 3
status: draft
tags: [환경설정, CUDA, PyTorch, GPU, AI엔지니어링]
keywords:
  - torch.cuda.is_available 확인
  - nvidia-smi 사용법
  - Google Colab T4 GPU 설정
  - GPU CPU 속도 차이 벤치마크
  - torch.cuda.synchronize 이유
  - VRAM 모델 크기 계산
  - fp16 파라미터당 2바이트
  - 클라우드 GPU 시간당 가격
  - PyTorch CUDA 버전 확인
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
