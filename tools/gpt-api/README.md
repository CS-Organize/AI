# GPT(Generative Pre-trained Transformer)
GPT-3.5: GPT-3를 [Fine-tuning](https://kr.appen.com/blog/fine-tuning/)한 모델

## API
[Overview - OpenAI API](https://platform.openai.com/docs/overview) 
- Completion API: 문장을 입력하면 완성된 문장을 출력해주는 API
- Chat API: 대화형으로 대답을 해주는 API

### [Pricing](https://openai.com/pricing#language-models)
GPT-4가 GPT-3.5보다 20배 비싸다고 함

### Token
[OpenAI Tokenizer](https://platform.openai.com/tokenizer)

### Prompt
[Prompt engineering - OpenAI API](https://platform.openai.com/docs/guides/prompt-engineering)

### Important Arguments

#### Temperature
0.0 ~ 2.0 사이의 값 (기본값: 1.0)이다.

작을 수록 가장 결정론적인 답을 도출 즉, 같은 입력에 대해 거의 동일한 출력을 생성하고 높을 수록 가장 무작위한 출력을 생성

- `logit`: 다음에 나올 단어의 확률을 나타내는 값
- `logit / temperature`에 `softmax`를 취하면 다음 단어의 확률을 얻을 수 있음 즉, `temperature`가 높을 수록 확률 분포가 더 균등해짐
