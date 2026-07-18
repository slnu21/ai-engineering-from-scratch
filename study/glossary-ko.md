# 용어 대조표 — 한국어 표기 기준

`glossary/terms.md` 의 83개 용어를 한국어로 어떻게 쓸지 고정한 표입니다.
학습 노트를 쓸 때 **여기 적힌 표기를 그대로** 씁니다. 매번 새로 번역하면
1편의 "어텐션"이 20편에서 "주의 메커니즘"이 되고, 나중에 검색이 안 됩니다.

## 표기 정책

1. **정착한 역어가 있으면 한국어.** 경사하강법 · 역전파 · 과적합 · 손실 함수 ·
   가중치 · 학습률 · 정규화 · 양자화. 교과서와 논문 번역서가 이미 쓰는 말들입니다.
2. **정착 역어가 없거나 음차가 표준이면 음차.** 어텐션 · 임베딩 · 토큰 ·
   트랜스포머 · 에포크. "주의집중"은 아무도 안 씁니다.
3. **약어 · 고유명사 · 함수명은 영어 그대로.** `LLM` · `RAG` · `MCP` · `CUDA` ·
   `ReLU` · `Adam` · `LoRA` · `GPT` · `JAX`. 억지로 풀면 오히려 못 알아봅니다.
4. **병기는 글마다 첫 등장 1회만.** 처음엔 `어텐션(attention)`, 그다음부터는
   그냥 `어텐션`. 매 문단 병기하면 읽는 리듬이 죽습니다.
5. **코드 · 에러 메시지 · 라이브러리 API 는 절대 번역하지 않습니다.**
   `loss.backward()` 는 `loss.backward()` 입니다.

## 대조표

| English | 한국어 표기 | 한 줄 뜻 |
|---|---|---|
| Activation Function | 활성화 함수(activation function) | 선형 레이어 뒤에 붙어 비선형성을 넣는 함수. 없으면 층을 쌓아도 하나로 붕괴합니다 |
| Adam (Optimizer) | `Adam` | 모멘텀 + 파라미터별 적응 학습률. 튜닝 없이도 웬만하면 도는 기본값 |
| AdamW | `AdamW` | Adam 에서 가중치 감쇠를 손실이 아니라 갱신 단계로 분리한 버전 |
| Agent | 에이전트(agent) | LLM 이 다음에 쓸 도구를 고르고, 실행하고, 결과를 보고, 반복하는 while 루프 |
| Alignment | 정렬(alignment) | 시스템의 행동을 사람의 의도·가치에 맞추는 문제. 예상 못 한 경우까지 포함해서 |
| Attention | 어텐션(attention) | 모든 토큰이 다른 모든 토큰의 값을 가중합하는 방식. 가중치는 쿼리·키의 내적 |
| Autograd | 자동 미분(autograd) | 순전파를 기록해 두고 역방향으로 기울기를 자동 계산하는 장치 |
| Autoregressive | 자기회귀(autoregressive) | 앞의 토큰들에 조건부로 다음 토큰을 예측하고, 그 예측을 다시 입력으로 넣는 방식 |
| Backpropagation | 역전파(backpropagation) | 연쇄 법칙으로 출력의 오차를 각 가중치의 기울기로 되돌려 계산하는 것 |
| Batch Size | 배치 크기(batch size) | 가중치를 한 번 갱신하기 전에 통과시키는 샘플 개수 |
| Chain of Thought (CoT) | 사고 사슬(chain of thought, CoT) | 답만 내지 말고 중간 추론 단계를 뱉게 시키는 프롬프트 기법 |
| Chunking | 청킹(chunking) | 긴 문서를 임베딩·검색 단위로 자르는 것. 자르는 방식이 검색 품질을 좌우합니다 |
| CNN (Convolutional Neural Network) | `CNN`(합성곱 신경망) | 작은 필터를 이미지 전체에 미끄러뜨려 지역 패턴을 잡는 신경망 |
| Context Window | 컨텍스트 윈도(context window) | 모델이 한 번에 볼 수 있는 토큰 수의 상한 |
| Contrastive Learning | 대조 학습(contrastive learning) | 비슷한 쌍은 가깝게, 다른 쌍은 멀게 임베딩을 밀고 당기며 배우는 방식 |
| Cosine Similarity | 코사인 유사도(cosine similarity) | 두 벡터의 각도로 재는 유사도. 크기는 무시하고 방향만 봅니다 |
| Cross-Entropy | 교차 엔트로피(cross-entropy) | 예측 분포가 정답 분포와 얼마나 다른지 재는 손실. 분류의 기본값 |
| CUDA | `CUDA` | NVIDIA GPU 에서 행렬 연산을 수천 코어로 병렬 실행하는 플랫폼 |
| Data Augmentation | 데이터 증강(data augmentation) | 원본을 뒤집고 자르고 흔들어 학습 데이터를 인위적으로 불리는 것 |
| Decoder | 디코더(decoder) | 표현을 받아 출력 시퀀스를 하나씩 만들어 내는 쪽 |
| Diffusion Model | 디퓨전 모델(diffusion model) | 노이즈를 조금씩 걷어내는 과정을 학습해 이미지를 생성하는 모델 |
| DPO (Direct Preference Optimization) | `DPO` | 보상 모델 없이 선호 쌍으로 정책을 직접 최적화하는 정렬 기법 |
| Dropout | 드롭아웃(dropout) | 학습 중 뉴런 일부를 무작위로 꺼서 특정 경로 의존을 막는 정규화 |
| Eigenvalue | 고윳값(eigenvalue) | 어떤 변환이 그 방향의 벡터를 얼마나 늘이거나 줄이는지를 나타내는 배율 |
| Embedding | 임베딩(embedding) | 의미가 위치로 표현되도록 대상을 벡터 공간에 심은 것 |
| Encoder | 인코더(encoder) | 입력을 압축된 표현으로 바꾸는 쪽 |
| Epoch | 에포크(epoch) | 학습 데이터 전체를 한 번 통과시킨 것 |
| Feature | 특징(feature) | 모델이 입력으로 받는 측정 가능한 성질 하나 |
| Few-Shot | 퓨샷(few-shot) | 프롬프트 안에 예시 몇 개를 넣어 형식을 잡아 주는 것 |
| Fine-tuning | 파인튜닝(fine-tuning) | 사전 학습된 모델을 특정 작업 데이터로 이어서 학습시키는 것 |
| Function Calling | 함수 호출(function calling) | 모델이 정해진 스키마에 맞춰 호출할 함수와 인자를 JSON 으로 뱉게 하는 것 |
| GAN (Generative Adversarial Network) | `GAN`(생성적 적대 신경망) | 생성기와 판별기를 맞붙여 서로 속이고 잡아내며 학습시키는 구조 |
| GPT | `GPT` | Generative Pre-trained Transformer. 자기회귀 디코더 전용 트랜스포머 계열 |
| Gradient | 기울기(gradient) | 각 파라미터를 조금 흔들었을 때 손실이 얼마나 변하는지의 벡터 |
| Gradient Descent | 경사하강법(gradient descent) | 기울기의 반대 방향으로 조금씩 파라미터를 옮겨 손실을 줄이는 것 |
| Guardrails | 가드레일(guardrails) | 모델 입출력에 거는 검증·차단 장치 |
| Hallucination | 환각(hallucination) | 그럴듯하지만 사실이 아닌 출력. 모델은 사실이 아니라 다음 토큰을 예측할 뿐입니다 |
| Hyperparameter | 하이퍼파라미터(hyperparameter) | 학습으로 배우는 게 아니라 사람이 정해 주는 설정값 |
| Inductive Bias | 귀납 편향(inductive bias) | 모델 구조 자체에 박혀 있는 "세상은 이럴 것이다"라는 가정 |
| Inference | 추론(inference) | 학습이 끝난 모델을 실제로 돌려 출력을 얻는 것 |
| JAX | `JAX` | 컴파일·자동미분·벡터화를 함수형으로 묶은 수치 계산 라이브러리 |
| KV Cache | `KV` 캐시(KV cache) | 이미 계산한 키·값을 저장해 토큰 생성마다 다시 계산하지 않게 하는 것 |
| Latent Space | 잠재 공간(latent space) | 데이터의 압축된 표현이 사는 공간 |
| Learning Rate | 학습률(learning rate) | 한 번의 갱신에서 파라미터를 얼마나 크게 옮길지 |
| LLM (Large Language Model) | `LLM` | 대규모 텍스트로 다음 토큰 예측을 학습한 대형 언어 모델 |
| LoRA (Low-Rank Adaptation) | `LoRA` | 원본 가중치는 얼리고 작은 저랭크 행렬만 학습하는 경량 파인튜닝 |
| Loss Function | 손실 함수(loss function) | 예측이 정답에서 얼마나 틀렸는지를 하나의 숫자로 만드는 함수 |
| MCP (Model Context Protocol) | `MCP` | 모델에 도구·데이터 소스를 붙이는 표준 프로토콜 |
| Mixed Precision | 혼합 정밀도(mixed precision) | 대부분을 16비트로 계산하고 민감한 부분만 32비트로 유지해 속도·메모리를 버는 것 |
| MoE (Mixture of Experts) | `MoE`(전문가 혼합) | 토큰마다 일부 전문가 네트워크만 골라 켜서 파라미터는 늘리되 연산은 아끼는 구조 |
| NaN (Not a Number) | `NaN` | 계산이 터졌다는 신호. 한 번 생기면 이후 연산 전체를 오염시킵니다 |
| Normalization | 정규화(normalization) | 값의 분포를 일정한 범위·통계로 맞추는 것 |
| Optimizer | 옵티마이저(optimizer) | 기울기를 받아 실제로 파라미터를 어떻게 갱신할지 정하는 규칙 |
| Overfitting | 과적합(overfitting) | 학습 데이터의 잡음까지 외워서 새 데이터에서 무너지는 상태 |
| Parameter | 파라미터(parameter) | 학습으로 값이 정해지는 모델 내부의 수. 가중치와 편향 |
| Perplexity | 퍼플렉시티(perplexity) | 모델이 다음 토큰을 얼마나 헷갈려 하는지. 낮을수록 좋습니다 |
| Precision & Recall | 정밀도 · 재현율(precision & recall) | 맞다고 한 것 중 진짜 비율 · 진짜 중 잡아낸 비율 |
| Prompt Engineering | 프롬프트 엔지니어링(prompt engineering) | 원하는 출력이 나오도록 입력을 설계하는 일 |
| Prompt Injection | 프롬프트 인젝션(prompt injection) | 데이터인 척 들어온 텍스트가 모델의 지시를 가로채는 공격 |
| QLoRA | `QLoRA` | 4비트로 양자화한 모델 위에 LoRA 를 얹어 메모리를 더 줄인 방식 |
| Quantization | 양자화(quantization) | 가중치를 낮은 비트 수로 표현해 모델을 가볍게 만드는 것 |
| RAG (Retrieval-Augmented Generation) | `RAG` | 답을 만들기 전에 관련 문서를 검색해 프롬프트에 끼워 넣는 구조 |
| ReLU | `ReLU` | 음수는 0, 양수는 그대로. 가장 흔한 활성화 함수 |
| RLHF (Reinforcement Learning from Human Feedback) | `RLHF` | 사람의 선호로 보상 모델을 만들고 그 보상으로 정책을 강화학습시키는 정렬 기법 |
| ROUGE | `ROUGE` | 생성 요약과 정답 요약의 n-gram 겹침으로 재는 지표 |
| Self-Attention | 셀프 어텐션(self-attention) | 같은 시퀀스 안에서 토큰들이 서로를 참조하는 어텐션 |
| Semantic Search | 의미 검색(semantic search) | 단어가 아니라 임베딩 거리로 찾는 검색 |
| SFT (Supervised Fine-Tuning) | `SFT` | 정답 응답 데이터로 지도 학습해 모델의 응답 형식을 잡는 단계 |
| Softmax | 소프트맥스(softmax) | 임의의 실수 벡터를 합이 1인 확률 분포로 바꾸는 함수 |
| Streaming | 스트리밍(streaming) | 생성이 끝나기를 기다리지 않고 토큰을 나오는 대로 흘려보내는 것 |
| Swarm | 스웜(swarm) | 여러 에이전트가 중앙 지휘 없이 상호작용해 결과를 내는 구성 |
| System Prompt | 시스템 프롬프트(system prompt) | 대화 앞에 고정으로 붙어 역할·규칙을 정하는 지시문 |
| Temperature | 온도(temperature) | 샘플링 분포를 얼마나 평평하게 만들지. 높을수록 무작위해집니다 |
| Tensor | 텐서(tensor) | 임의 차원의 숫자 배열. 스칼라·벡터·행렬의 일반화 |
| Token | 토큰(token) | 모델이 다루는 최소 단위. 단어보다 대체로 작습니다 |
| Transfer Learning | 전이 학습(transfer learning) | 한 작업에서 배운 표현을 다른 작업에 가져다 쓰는 것 |
| Transformer | 트랜스포머(transformer) | 순환 없이 어텐션만으로 시퀀스를 처리하는 구조 |
| Underfitting | 과소적합(underfitting) | 모델이 데이터의 패턴조차 못 잡은 상태 |
| VAE (Variational Autoencoder) | `VAE` | 잠재 공간을 확률 분포로 학습해 샘플링이 가능하게 만든 오토인코더 |
| Vector Database | 벡터 데이터베이스(vector database) | 임베딩을 저장하고 최근접 이웃을 빠르게 찾아 주는 저장소 |
| Weight | 가중치(weight) | 입력에 곱해지는 학습 대상 계수 |
| Weight Decay | 가중치 감쇠(weight decay) | 가중치가 커지지 않도록 갱신마다 조금씩 줄이는 정규화 |
| Zero-Shot | 제로샷(zero-shot) | 예시 없이 지시만으로 시키는 것 |

## 표에 없는 용어를 만나면

노트를 쓰다 표에 없는 용어가 나오면 **위 정책 1~3으로 판단해 표에 한 줄 추가**하고
씁니다. 그 자리에서 정하고 넘어가면 다음 노트에서 또 흔들립니다.
