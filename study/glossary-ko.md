# 용어 대조표 — 한국어 표기 기준

`glossary/terms.md`의 83개 용어를 한국어로 어떻게 쓸지 고정한 표입니다.
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
5. **코드 · 에러 메시지 · 라이브러리 API는 절대 번역하지 않습니다.**
   `loss.backward()`는 `loss.backward()`입니다.

## 대조표

| English | 한국어 표기 | 한 줄 뜻 |
|---|---|---|
| Activation Function | 활성화 함수(activation function) | 선형 레이어 뒤에 붙어 비선형성을 넣는 함수. 없으면 층을 쌓아도 하나로 붕괴합니다 |
| Adam (Optimizer) | `Adam` | 모멘텀 + 파라미터별 적응 학습률. 튜닝 없이도 웬만하면 도는 기본값 |
| AdamW | `AdamW` | Adam에서 가중치 감쇠를 손실이 아니라 갱신 단계로 분리한 버전 |
| Agent | 에이전트(agent) | LLM이 다음에 쓸 도구를 고르고, 실행하고, 결과를 보고, 반복하는 while 루프 |
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
| CUDA | `CUDA` | NVIDIA GPU에서 행렬 연산을 수천 코어로 병렬 실행하는 플랫폼 |
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
| Function Calling | 함수 호출(function calling) | 모델이 정해진 스키마에 맞춰 호출할 함수와 인자를 JSON으로 뱉게 하는 것 |
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
| QLoRA | `QLoRA` | 4비트로 양자화한 모델 위에 LoRA를 얹어 메모리를 더 줄인 방식 |
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

## 도구 · 워크플로우 용어

`glossary/terms.md`에는 없지만 레슨 본문에서 반복되는 용어입니다. 정책은 위와 같습니다.

| English | 한국어 표기 | 한 줄 뜻 |
|---|---|---|
| Branch | 브랜치(branch) | 커밋을 가리키는 포인터. 작업하면 같이 앞으로 움직입니다 |
| Commit | 커밋(commit) | 특정 시점 프로젝트 전체의 스냅숏 |
| Fast-forward | 패스트포워드(fast-forward) | 갈라진 이력이 없어 병합 커밋 없이 포인터만 앞으로 옮기는 병합 |
| Merge | 머지(merge) | 한 브랜치의 변경을 다른 브랜치에 적용하는 것 |
| Remote | 리모트(remote) | 다른 곳에 호스팅된 저장소 사본(GitHub, GitLab) |
| Staging Area | 스테이징 영역(staging area) | 다음 커밋에 담을 변경을 모아 두는 중간 자리 |
| Working Directory | 작업 디렉터리(working directory) | 실제로 파일을 편집하는 디스크상의 공간 |

## 하드웨어 · 실행 환경 용어

마찬가지로 `glossary/terms.md`에는 없지만 GPU 관련 레슨에서 반복되는 용어입니다.
셋 다 약어·고유명사라 정책 3에 따라 영어 표기를 그대로 씁니다.

| English | 한국어 표기 | 한 줄 뜻 |
|---|---|---|
| fp16 | `fp16`(반정밀도) | 16비트 부동소수점. `fp32`의 절반 메모리를 쓰면서 정확도 손실은 대체로 미미합니다 |
| Tensor Core | `Tensor Core` | 행렬 곱에 특화된 GPU 코어. 일반 코어보다 4~8배 빠릅니다 |
| VRAM | `VRAM` | GPU에 붙은 전용 메모리. 시스템 RAM과 별개이며 올릴 수 있는 모델 크기의 상한입니다 |

## 레슨 번역 용어 (Phase 00–07)

Trailmark 한국어 번역 팩(Phase 00–07, 159레슨)을 만들며 정한 표기입니다. 정책은 위와 같습니다.
여러 번역에서 표기가 갈렸던 것은 **오른쪽 열 표기로 통일**했고, 갈렸던 다른 표기는 `(… 아님)`으로 적었습니다.

### 수학 · 통계

| English | 한국어 표기 | 한 줄 뜻 |
|---|---|---|
| Inner / Dot Product | 내적(inner product) | 두 벡터를 원소별로 곱해 더한 값. 방향이 얼마나 같은지를 잽니다 |
| Projection | 사영(projection) | 벡터를 다른 벡터·부분공간 위로 내린 그림자 (투영 아님) |
| Linear Independence | 선형 독립(linear independence) | 어느 벡터도 나머지의 조합으로 만들 수 없는 상태 |
| Rank | 랭크(rank) | 행렬이 실제로 펼치는 독립 방향의 수 |
| Basis | 기저(basis) | 공간의 모든 벡터를 유일하게 표현하는 최소 벡터 집합 |
| Orthonormal | 정규직교(orthonormal) | 서로 직교하고 길이가 1인 벡터들 |
| Column / Null Space | 열공간 / 영공간(column / null space) | 행렬이 만들 수 있는 출력 / 0으로 보내는 입력의 모임 (열 공간 아님) |
| Eigenvalue / Eigenvector | 고윳값 / 고유벡터 | 행렬을 곱해도 방향이 안 바뀌는 벡터와 그 배율 |
| Singular Value Decomposition | 특잇값 분해(SVD) | 아무 행렬이나 회전·늘이기·회전으로 쪼개는 분해 |
| Pseudoinverse | 유사역행렬(pseudoinverse) | 역행렬이 없을 때 최소제곱 해를 주는 대용 |
| Condition Number | 조건수(condition number) | 입력 오차가 출력에서 얼마나 커지는지의 배율. 크면 악조건 |
| Normal Equations | 정규 방정식(normal equations) | 최소제곱 해를 닫힌 형태로 주는 식 (정규방정식 아님) |
| Least Squares | 최소제곱(least squares) | 오차 제곱합을 최소로 하는 해 |
| Norm | 노름(norm) | 벡터의 크기를 재는 함수(L1, L2, L∞) |
| Derivative / Partial Derivative | 도함수 / 편도함수 | 입력을 조금 바꿀 때 출력 변화율 |
| Jacobian / Hessian | 야코비 행렬 / 헤세 행렬 | 1차 / 2차 편도함수를 모은 행렬 |
| Chain Rule | 연쇄 법칙(chain rule) | 합성 함수의 미분 = 각 단계 미분의 곱. 역전파의 바탕 |
| Computational Graph | 계산 그래프(computational graph) | 연산을 노드로, 데이터 흐름을 간선으로 그린 그래프 |
| Saddle Point | 안장점(saddle point) | 한 방향으론 최소, 다른 방향으론 최대인 점 |
| Convex | 볼록(convex) | 어느 두 점을 이은 선분도 함수 위에 있는 성질. 지역 최솟값 = 전역 최솟값 |
| Likelihood | 가능도(likelihood) | 파라미터가 주어졌을 때 관측 데이터가 나올 확률 |
| Prior / Posterior | 사전 확률 / 사후 확률 | 데이터를 보기 전 / 본 뒤의 믿음 |
| MLE / MAP | 최대 가능도 추정(MLE) / 최대 사후 확률 추정(MAP) | 가능도 / 사후 확률을 최대로 하는 파라미터 추정 |
| Conjugate Prior | 켤레 사전 분포(conjugate prior) | 사후 분포가 사전 분포와 같은 꼴이 되는 사전 분포 |
| KL Divergence | KL 발산(KL divergence) | 두 분포가 얼마나 다른지 재는 비대칭 거리 |
| Mutual Information | 상호 정보량(mutual information) | 한 변수를 알면 다른 변수의 불확실성이 얼마나 주는지 |
| Central Limit Theorem | 중심 극한 정리 | 독립 표본의 평균은 정규분포에 가까워진다는 정리 |
| Markov Chain | 마르코프 체인(Markov chain) | 다음 상태가 현재 상태에만 의존하는 확률 과정 (마르코프 연쇄 아님) |
| Stationary Distribution | 정상 분포(stationary distribution) | 전이를 반복해도 바뀌지 않는 분포 |
| Rejection / Importance Sampling | 기각 / 중요도 샘플링 | 쉬운 분포로 뽑아 버리거나 가중치를 주어 어려운 분포를 흉내 내기 |
| Reparameterization Trick | 재매개변수화 트릭 | 무작위성을 입력으로 빼내 샘플링을 미분 가능하게 만드는 기법 (기법 아님) |
| Burn-in / Thinning | 번인 / 솎아내기 | MCMC 초반 표본 버리기 / 상관을 줄이려 띄엄띄엄 고르기 |
| Fourier Transform | 푸리에 변환(DFT/FFT) | 신호를 주파수 성분으로 분해 |
| Aliasing | 에일리어싱(aliasing) | 샘플링이 성겨서 높은 주파수가 낮은 주파수로 둔갑하는 현상 |
| Window Function | 윈도 함수(window function) | 신호 조각의 양 끝을 부드럽게 줄이는 함수 (창 함수 아님) |
| Bootstrap | 부트스트랩(bootstrap) | 복원 추출로 표본을 다시 뽑아 통계량의 분포를 추정 |
| Statistical Power | 검정력(power) | 실제 효과가 있을 때 그걸 잡아낼 확률 |

### ML 기초

| English | 한국어 표기 | 한 줄 뜻 |
|---|---|---|
| Feature / Feature Engineering | 특징 / 특징 공학 | 모델 입력 변수 / 그걸 만드는 일. 제품명은 '피처 스토어'처럼 음차 |
| Threshold | 임곗값(threshold) | 판정을 가르는 기준값 (임계값 아님) |
| False Positive / Negative | 위양성 / 위음성 | 아닌데 맞다고 / 맞는데 아니라고 판정 (거짓 양성 아님) |
| True Positive / Negative | 진양성 / 진음성 | 맞게 맞다고 / 맞게 아니라고 판정 |
| Precision / Recall | 정밀도 / 재현율 | 양성이라 한 것 중 진짜 비율 / 진짜 중 잡아낸 비율 |
| Confusion Matrix | 혼동 행렬 | 예측과 실제의 조합을 센 표 |
| Cross-Validation | 교차 검증(K-겹) | 데이터를 K조각으로 나눠 돌려 가며 검증 |
| Data Leakage | 데이터 누수 | 학습 때 미래·정답 정보가 새어 들어가 점수가 부풀려지는 것 |
| Bias-Variance Tradeoff | 편향-분산 트레이드오프 | 단순하면 편향, 복잡하면 분산이 커지는 균형 |
| Overparameterization | 과파라미터화 | 데이터보다 파라미터가 많은 상태 (과매개변수화 아님) |
| Double Descent | 이중 하강 | 모델이 커지면 테스트 오차가 줄었다 늘었다 다시 주는 현상 |
| Regularization / Normalization | 정규화(regularization) / 정규화 층·표준화 | 과적합 억제 / 값의 크기 맞추기. 겹칠 땐 normalization을 '정규화 층'·방법 이름(BatchNorm)으로 |
| Decision Tree / Random Forest | 결정 트리 / 랜덤 포레스트 | 질문으로 갈라 내려가는 모델 / 그 앙상블 |
| Gini Impurity / Information Gain | 지니 불순도 / 정보 이득 | 노드가 얼마나 섞였는지 / 분할로 줄어든 불확실성 |
| Gradient Boosting | 그래디언트 부스팅 | 앞 모델의 잔차를 다음 모델이 고쳐 나가는 앙상블 (그레이디언트 아님) |
| Support Vector / Margin | 서포트 벡터 / 마진 | 경계에 가장 가까운 점 / 경계까지의 거리 |
| Kernel Trick | 커널 트릭 | 고차원 사상을 직접 하지 않고 내적만 바꿔 쓰는 기법 |
| Centroid | 중심점(centroid) | 군집의 평균 위치 (센트로이드 아님) |
| Laplace Smoothing | 라플라스 스무딩 | 빈도에 1을 더해 0 확률을 막는 기법 (평활 아님) |
| Stationarity | 정상성(stationarity) | 시계열의 통계적 성질이 시간에 따라 안 바뀌는 것 |
| Drift | 드리프트(drift) | 운영 데이터 분포가 학습 때와 달라지는 것 |
| Training-Serving Skew | 학습-서빙 불일치 | 학습 때와 서빙 때 특징 계산이 달라 생기는 오차 |

### 딥러닝 · 비전

| English | 한국어 표기 | 한 줄 뜻 |
|---|---|---|
| Fine-tuning | 파인튜닝(fine-tuning) | 사전 학습 모델을 내 데이터로 더 학습 (미세 조정 아님) |
| Universal Approximation Theorem | 보편 근사 정리 | 은닉층 하나로도 연속 함수를 원하는 만큼 근사할 수 있다는 정리 |
| Vanishing / Exploding Gradient | 기울기 소실 / 폭발 | 역전파 중 기울기가 0으로 사라지거나 터지는 현상 |
| Gradient Clipping | 기울기 클리핑 | 기울기 크기를 상한으로 자르기 |
| Dead ReLU | 죽은 ReLU | 입력이 늘 음수라 출력·기울기가 0으로 굳은 뉴런 |
| Focal Loss | 포컬 손실(focal loss) | 쉬운 예제의 손실을 줄여 어려운 예제에 집중 (초점 손실 아님) |
| Triplet Loss | 트리플렛 손실(triplet loss) | 앵커를 양성엔 가깝게, 음성엔 멀게 (삼중항 손실 아님) |
| Label Smoothing | 레이블 스무딩 | 정답 확률 1을 조금 깎아 과신을 막기 |
| Early Stopping | 조기 종료 | 검증 손실이 나빠지기 시작하면 학습 중단 |
| Receptive Field | 수용 영역 | 출력 한 칸이 입력에서 보는 범위 |
| Backbone / Head | 백본 / 헤드 | 특징을 뽑는 몸통 / 과제별 출력부 |
| Non-Maximum Suppression | 비최대 억제(NMS) | 겹치는 상자 중 점수 최고만 남기기 |
| Semantic / Instance Segmentation | 의미론적 / 인스턴스 분할 | 픽셀마다 클래스 / 객체마다 마스크 |
| Dense Prediction | 밀집 예측 | 픽셀마다 출력을 내는 과제 (조밀 예측 아님) |
| Mode Collapse | 모드 붕괴 | GAN 생성기가 몇 가지 출력만 반복하는 현상 |
| Classifier-Free Guidance | 분류기 없는 가이던스(CFG) | 조건부·무조건 예측 차이로 프롬프트 반영 강도를 조절 |
| Point Cloud | 포인트 클라우드(point cloud) | 3D 점들의 집합 (점 구름 아님) |
| Radiance Field | 방사 필드(radiance field) | 위치·방향마다 색과 밀도를 주는 함수(NeRF) (복사장 아님) |
| Knowledge Distillation | 지식 증류 | 큰 모델의 출력을 작은 모델이 흉내 내게 학습 |
| Catastrophic Forgetting | 파국적 망각 | 새 과제를 배우며 이전 과제를 잊는 현상 |

### NLP · 음성 · 트랜스포머

| English | 한국어 표기 | 한 줄 뜻 |
|---|---|---|
| Coreference Resolution | 상호참조 해결 | "그"가 누구인지 같은 대상을 묶기 (해소 아님) |
| Mention | 멘션(mention) | 텍스트 안에서 개체를 가리키는 구절 |
| Entity Linking | 개체 연결 | 멘션을 지식 베이스의 항목에 잇기 |
| Natural Language Inference | 자연어 추론(NLI) | 전제가 가설을 함의·모순·중립하는지 판정 |
| Subword / Tokenizer | 서브워드 / 토크나이저 | 단어보다 작은 토큰 단위 / 텍스트를 토큰으로 자르는 도구 |
| Out-of-Vocabulary | 미등록어(OOV) | 어휘에 없는 단어 |
| Chunking | 청킹(chunking) | 긴 문서를 검색 단위로 자르기 |
| Reranker / Cross-Encoder | 리랭커 / 크로스 인코더 | 1차 검색 결과를 쿼리와 함께 다시 점수 매기는 모델 |
| Instruction Tuning | 지시 튜닝(instruction tuning) | 지시-응답 쌍으로 파인튜닝 (인스트럭션 튜닝 아님) |
| Teacher Forcing | 교사 강요(teacher forcing) | 학습 때 이전 정답 토큰을 다음 입력으로 넣기 |
| In-Context Learning | 인컨텍스트 학습 | 가중치 갱신 없이 프롬프트 예시만으로 과제 수행 |
| Speculative Decoding | 추측 디코딩 | 작은 모델이 초안을 쓰고 큰 모델이 한 번에 검증 |
| KV Cache | KV 캐시 | 이전 토큰의 키·값을 저장해 재계산을 피하기 |
| Mixture of Experts | 전문가 혼합(MoE) | 토큰마다 일부 전문가만 켜는 구조 |
| Positional Encoding | 위치 인코딩 | 순서 정보를 토큰 표현에 넣는 방법(사인파, RoPE, ALiBi) |
| Scaling Laws | 스케일링 법칙 | 모델·데이터·연산을 늘릴 때 손실이 줄어드는 거듭제곱 관계 |
| Voice Activity Detection | 음성 구간 검출(VAD) | 오디오에서 말하는 구간 찾기 (음성 활동 감지 아님) |
| Speaker Diarization | 화자 분리(diarization) | 누가 언제 말했는지 나누기 (화자 분할 아님) |
| Vocoder | 보코더(vocoder) | 음향 특징을 파형으로 바꾸는 모델 |
| Mel Spectrogram | 멜 스펙트로그램 | 사람 청각에 맞춘 주파수 축의 스펙트로그램 |
| Answer Relevance | 답변 관련성 | RAG 평가: 답이 질문에 맞는 정도 (답 관련성 아님) |

## 레슨 번역 용어 (Phase 08–15)

Trailmark 번역 팩 Phase 08–15(214레슨)에서 정한 표기입니다. 위 Phase 00–07 절과 같은 방식으로, 갈렸던 표기는 `(… 아님)`으로 적었습니다.

### 생성 AI · 강화학습

| English | 한국어 표기 | 한 줄 뜻 |
|---|---|---|
| Generator / Discriminator | 생성기 / 판별기 | GAN의 두 네트워크 (생성자/판별자 아님) |
| Posterior Collapse | 사후 분포 붕괴 | VAE 인코더가 무시되고 잠재 변수가 사전 분포로 무너지는 현상 |
| Forward / Reverse Process | 순방향 / 역방향 과정 | 디퓨전에서 노이즈를 더하는 / 걷어내는 과정 |
| Flow Matching / Rectified Flow | 플로 매칭 / 정류 흐름 | 노이즈에서 데이터로 가는 속도장을 직접 학습하는 생성 방식 |
| Velocity Field | 속도장 | 각 시점·위치에서 샘플이 움직일 방향과 속도 |
| Perceptual Loss | 지각 손실 | 픽셀 대신 사전 학습 네트워크의 특징 차이로 재는 손실 |
| Reinforcement Learning | 강화학습 | 보상을 최대화하도록 행동을 배우는 학습 (강화 학습 아님 — 붙여 씀) |
| On-policy / Off-policy | 온폴리시 / 오프폴리시 | 지금 정책으로 모은 데이터로만 / 다른 정책의 데이터로도 배우는 방식 (온 폴리시 아님) |
| Return | 리턴(return) | 에피소드에서 할인해 더한 누적 보상 |
| Advantage | 어드밴티지 | 어떤 행동이 평균보다 얼마나 나은지 |
| Credit Assignment | 기여도 할당 | 늦게 온 보상을 어느 행동 덕분인지 나눠 주는 문제 (공로 할당 아님) |
| Experience Replay / Target Network | 경험 리플레이 / 타깃 네트워크 | DQN을 안정시키는 두 장치 |
| Behavior / Target Policy | 행동 정책 / 목표 정책 | 데이터를 모으는 정책 / 배우려는 정책 |
| Reward Hacking / Shaping | 보상 해킹 / 보상 셰이핑 | 보상의 허점을 파고드는 것 / 학습을 돕도록 보상을 덧붙이는 것 |
| Process / Outcome Reward Model | 과정 / 결과 보상 모델(PRM / ORM) | 풀이 단계별로 / 최종 답만 채점하는 보상 모델 |

### LLM 구축 · 엔지니어링

| English | 한국어 표기 | 한 줄 뜻 |
|---|---|---|
| Pre-training / Post-training | 사전 학습 / 사후 학습 | 대규모 다음 토큰 예측 / 그 뒤의 SFT·선호 최적화 |
| Supervised Fine-tuning | 지도 파인튜닝(SFT) | 지시-응답 쌍으로 하는 파인튜닝 |
| Preferred / Rejected Response | 선호 응답 / 기각 응답 | 선호 데이터의 두 응답 (거절 응답 아님) |
| Weight Tying | 가중치 묶기 | 입력 임베딩과 출력층 가중치를 공유 (가중치 공유 아님) |
| Pre-norm / Post-norm | 프리노름 / 포스트노름 | 정규화 층을 서브층 앞 / 뒤에 두는 배치 (사전 정규화 아님) |
| Quantization | 양자화 | 가중치·활성값을 더 적은 비트로 표현 |
| Prefill / Decode | 프리필 / 디코드 | 프롬프트를 한 번에 처리하는 단계 / 토큰을 하나씩 만드는 단계 |
| Compute-bound / Memory-bound | 연산 병목 / 메모리 병목 | 연산량 / 메모리 대역폭이 속도를 정하는 상태 |
| Continuous Batching | 연속 배칭 | 끝난 요청 자리에 새 요청을 바로 넣는 서빙 방식 |
| Acceptance Rate | 수락률 | 추측 디코딩에서 초안 토큰이 받아들여지는 비율 (수용률 아님) |
| Residual Distribution | 잔여 분포 | 추측 디코딩에서 기각 후 다시 뽑는 분포 (잔차 분포 아님) |
| Ablation | 절제 실험 | 구성 요소를 하나씩 빼서 기여를 재는 실험 (어블레이션 아님) |
| Chain of Thought | 사고 사슬(CoT) | 답 전에 중간 추론을 쓰게 하는 프롬프팅 (사고의 연쇄 아님) |
| Semantic Cache | 의미 캐시 | 뜻이 비슷한 질의에 캐시된 답을 돌려주는 캐시 (시맨틱 캐시 아님) |
| Cache Hit / Hit Rate | 캐시 적중 / 적중률 | (캐시 히트·히트율 아님) |
| Rate Limiting | 속도 제한 | 단위 시간당 요청 수 상한 (호출 횟수 제한 아님) |
| Bi-encoder | 바이 인코더 | 질의와 문서를 따로 임베딩하는 검색 모델 (바이인코더 아님) |
| Eval Set | 평가 세트 | 회귀를 잡는 고정 평가 묶음 (평가 스위트 아님) |
| LLM-as-judge | LLM 심판 | LLM으로 다른 모델 출력을 채점하는 평가 |
| Data Contamination | 데이터 오염 | 평가 데이터가 학습 데이터에 섞인 것 |

### 멀티모달

| English | 한국어 표기 | 한 줄 뜻 |
|---|---|---|
| Negative Sample | 음성 샘플(negative) | 대조 학습에서 밀어내는 짝. 양성/음성은 분류와 같은 짝 표기이고, 음성(speech)과 헷갈리지 않게 레슨 첫 등장에 negative를 병기 |
| Early / Late Fusion | 초기 / 후기 융합 | 모달리티를 입력 토큰 단계에서 / 늦게 합치는 방식 |
| Bilinear | 쌍선형 | (이중선형 아님) |
| Turn-taking | 턴 테이킹 | 대화에서 말할 차례를 주고받기 (턴 교대 아님) |
| Grounding | 그라운딩 | 텍스트를 이미지 영역·시간 구간 등에 연결하기 |
| Codebook | 코드북 | 이산 토큰화에서 벡터 사전 |
| Vision-Language-Action | 비전-언어-행동(VLA) | 로봇 행동까지 출력하는 멀티모달 모델 |

### 도구 · 프로토콜 · 리버스 엔지니어링

| English | 한국어 표기 | 한 줄 뜻 |
|---|---|---|
| Discovery | 디스커버리 | MCP에서 서버 기능을 알아내는 단계 |
| Primitive | 프리미티브 | MCP의 도구·리소스·프롬프트 같은 기본 구성 단위 (에이전트 런타임 문맥에선 기본 요소) |
| Descriptor | 기술자 | 도구·타입을 설명하는 메타데이터 |
| Admission | 입점 심사 | 레지스트리가 서버를 받아들이는 검증 (승인 아님) |
| Provider | 제공자 | 모델·서비스를 제공하는 쪽 (프로바이더 아님) |
| Fail-closed | 닫힌 쪽으로 실패 | 판단이 안 서면 막는 쪽을 택하는 설계 (실패 시 닫힘 아님) |
| Circuit Breaker | 서킷 브레이커 | 연속 실패 시 호출을 잠시 끊는 장치 (회로 차단기 아님) |
| Idempotency Key | 멱등성 키 | 같은 요청이 두 번 와도 한 번만 처리하게 하는 키 |
| Backpressure | 배압 | 소비자가 느릴 때 생산자 속도를 늦추는 흐름 제어 |
| Provenance | 출처 | 데이터·도구가 어디서 왔는지의 기록 |
| Tool Poisoning | 도구 오염 | 도구 설명에 악성 지시를 숨기는 공격 |
| Progressive Disclosure | 점진적 공개 | 스킬 내용을 필요할 때만 단계적으로 읽히는 방식 |
| Disassembly / Decompilation | 디스어셈블리 / 디컴파일 | 기계어를 어셈블리로 / 고수준 코드로 되돌리기 |
| Basic Block / Dominator | 기본 블록 / 지배자 | CFG의 직선 코드 조각 / 모든 경로가 거쳐 가는 블록 |
| Lifting | 리프팅 | 기계어를 중간 표현으로 끌어올리기 |
| Calling Convention | 호출 규약 | 인자·반환값·레지스터 보존 규칙 |
| Addend | 가산값 | 재배치에서 심볼 주소에 더하는 값 (애드엔드·가수 아님 — 가수는 mantissa) |
| Immediate | 즉칫값 | 명령어에 박힌 상수 (즉치값·즉시값 아님) |
| Symbolic Execution | 기호 실행 | 입력을 기호로 두고 경로 조건을 모으는 분석 |

### 에이전트 · 자율 시스템

| English | 한국어 표기 | 한 줄 뜻 |
|---|---|---|
| Workbench | 워크벤치 | 에이전트가 일하는 저장소·도구·규칙 묶음 (작업대 아님) |
| Supervisor-Worker | 슈퍼바이저-워커 | 관리 에이전트가 작업자 에이전트에 일을 나누는 구조 (감독자 아님) |
| Conditional Edge / Subgraph | 조건부 엣지 / 하위 그래프 | LangGraph 용어 (조건부 간선·서브그래프 아님) |
| Handoff | 핸드오프 / 인계 | SDK 개념은 핸드오프, 사람·세션 간 넘겨주기는 인계 |
| Dead-letter Queue | 데드레터 큐 | 처리 실패 메시지를 모아 두는 큐 (붙여 씀) |
| Sleep-time Compute | 슬립 타임 연산 | 대기 시간에 메모리를 정리하는 연산 (띄어 씀) |
| Durable Execution | 내구성 있는 실행 | 장애 후에도 이어서 실행되는 워크플로 (내구 실행 아님) |
| Scope Contract / Definition of Done | 범위 계약 / 완료 정의 | 에이전트 작업 범위와 끝의 기준 |
| Propose-then-commit | 제안 후 커밋 | 행동을 먼저 제안하고 승인 뒤 실행 (제안 후 확정 아님) |
| Canary Token | 카나리 토큰 | 유출·오용을 감지하는 미끼 토큰 (카나리아 토큰 아님) |
| Kill Switch | 킬 스위치 | 자율 에이전트를 즉시 멈추는 장치 |
| Cost Governor | 비용 거버너 | 지출 상한·속도를 감시하는 장치 (비용 관리자 아님) |
| Blast Radius | 피해 반경 | 잘못됐을 때 영향이 미치는 범위 (영향 반경 아님) |
| Alignment Faking | 정렬 위장 | 평가 중에만 정렬된 척하는 행동 |
| Sandbagging | 샌드배깅 | 평가에서 일부러 능력을 낮춰 보이기 |

## 레슨 번역 용어 (Phase 16–19)

Trailmark 번역 팩 Phase 16–19(169레슨)에서 정한 표기입니다. 표기 방식은 위 절들과 같습니다.

### 다중 에이전트 · 스웜

| English | 한국어 표기 | 한 줄 뜻 |
|---|---|---|
| Planner | 플래너 | 계획을 세우는 에이전트·구성 요소 (계획자 아님) |
| Verifier (agent role) / Verifier (component) | 검증자 / 검증기 | 역할로서의 에이전트는 검증자, 부품·함수는 검증기 |
| Monoculture | 모노컬처 | 같은 모델·프롬프트만 써서 오류가 함께 나는 상태 (단일 문화 아님) |
| Frontier Model | 프런티어 모델 | 가장 앞선 성능의 모델 (최전선 모델 아님) |
| Contract Net | 계약망 | 관리자가 작업을 공고하고 입찰로 맡기는 프로토콜 |
| Blackboard | 블랙보드 | 에이전트들이 공유 공간에 읽고 쓰며 협업하는 구조 |
| Byzantine Fault Tolerance | 비잔틴 장애 허용(BFT) | 일부 참여자가 거짓말해도 합의가 깨지지 않는 성질 |
| Credit Attribution | 기여도 배분 | 공동 결과를 참여자별로 나누는 일 (기여도 할당 = credit assignment과 구분) |
| Communicative Dehallucination | 대화형 환각 제거 | 에이전트끼리 질문을 주고받아 환각을 줄이는 기법 (소통형 아님) |
| Decentralized Identifier | 탈중앙화 식별자(DID) | 중앙 기관 없이 검증 가능한 식별자 (탈중앙 식별자 아님) |
| Rainbow Deployment | 레인보 배포 | 여러 버전을 동시에 띄워 두고 서서히 옮기는 배포 (레인보우 아님) |
| Groupthink | 집단 사고 | 다수 의견에 휩쓸려 오류를 못 잡는 현상 |

### 인프라 · 프로덕션

| English | 한국어 표기 | 한 줄 뜻 |
|---|---|---|
| Failover | 장애 조치 | 장애 시 다른 경로·서버로 넘기기 (페일오버 아님) |
| Data Residency | 데이터 레지던시 | 데이터가 저장·처리되는 지역 요건 (데이터 상주 요건 아님) |
| Disaggregated Serving | 분리 서빙 | 프리필과 디코드를 다른 장비에서 처리 (분리형 서빙 아님) |
| Chunked Prefill | 청크 프리필 | 긴 프롬프트를 조각내 디코드와 섞어 처리 (청크 단위 프리필 아님) |
| Cache-aware Routing | 캐시 인식 라우팅 | 프리픽스 캐시가 있는 서버로 보내기 (캐시 인지 아님) |
| Goodput | 굿풋 | SLO를 지킨 요청만 센 처리량 |
| Error Budget | 오류 예산 | SLO가 허용하는 실패 여유분 |
| On-call / Runbook / Postmortem | 온콜 / 런북 / 사후 분석 | 운영 대응 용어 |
| Cost Attribution | 비용 귀속 | 사용자·작업·테넌트별로 비용을 나눠 붙이기 |

### 윤리 · 안전 · 정렬

| English | 한국어 표기 | 한 줄 뜻 |
|---|---|---|
| Safety Case | 안전성 논증 | 시스템이 안전하다는 구조화된 근거 (안전성 사례·안전 사례 아님) |
| Uplift | 역량 증강 | 모델이 위험 작업 능력을 키워 주는 정도 (역량 강화 아님) |
| Model Organism | 모델 생물 | 위험 행동을 일부러 심어 연구하는 모델 (모델 유기체 아님) |
| Mesa-optimizer | 메사 최적화기 | 학습된 모델 안에 생긴 최적화기 (메사 옵티마이저 아님) |
| Scheming | 계략 | 숨은 목표를 위해 감독을 속이는 행동 |
| Alignment Tax | 정렬세 | 정렬 때문에 생기는 성능·비용 손해 (정렬 세금 아님) |
| Homoglyph | 동형 문자 | 모양이 같은 다른 문자로 필터를 우회 (호모글리프 아님) |
| Zero-click | 제로클릭 | 사용자 조작 없이 일어나는 공격 (붙여 씀) |
| Red Team | 레드팀 | 공격자 입장에서 약점을 찾는 팀·활동 (붙여 씀) |
| Over-refusal | 과잉 거부 | 무해한 요청까지 거절하는 것 |

### 캡스톤

| English | 한국어 표기 | 한 줄 뜻 |
|---|---|---|
| Capstone / Deliverable | 캡스톤 / 결과물 | 종합 프로젝트 / 그 산출 |
| Near-miss | 니어 미스 | 사고 직전에 잡힌 일 (아차 사고 아님) |
| Approval Gate | 승인 게이트 | 사람 승인을 받아야 넘어가는 지점 (승인 관문 아님) |
| Golden Set | 골든 세트 | 정답이 확정된 평가 묶음 (골드셋 아님) |
| Brevity Penalty | 짧은 길이 벌점 | BLEU에서 너무 짧은 출력에 주는 벌점 |
| Shape Contract | 형태 계약 | 텐서 모양을 함수 경계에서 보장하는 약속 (모양 계약 아님) |
| Unshard | 언샤드 | 나뉜 파라미터를 다시 모으기 (샤드 복원 아님) |
| Activation Checkpointing | 활성값 체크포인팅 | 활성값을 버리고 역전파 때 다시 계산 (활성화 체크포인팅 아님) |
| Mock LLM | 모의 LLM | 테스트용 가짜 모델 (목·가짜 LLM 아님) |
| Prefix Injection | 프리픽스 인젝션 | 응답 앞머리를 강제해 탈옥하는 공격 (프롬프트 인젝션과 같은 표기) |

## 표에 없는 용어를 만나면

노트를 쓰다 표에 없는 용어가 나오면 **위 정책 1~3으로 판단해 표에 한 줄 추가**하고
씁니다. 그 자리에서 정하고 넘어가면 다음 노트에서 또 흔들립니다.
