# Prompt Engineering

- [Principled Instructions Are All You Need for Questioning LLaMA-1/2, GPT-3.5/4](https://arxiv.org/abs/2312.16171)
- [Prompt Engineering Guide](https://www.promptingguide.ai/kr)
- [Learn Prompting](https://learnprompting.org/ko/docs/intro)
- [dair-ai/Prompt-Engineering-Guide: 🐙 Guides, papers, lecture, notebooks and resources for prompt engineering](https://github.com/dair-ai/Prompt-Engineering-Guide)
- [f/awesome-chatgpt-prompts: This repo includes ChatGPT prompt curation to use ChatGPT better.](https://github.com/f/awesome-chatgpt-prompts)
- [linexjlin/GPTs: leaked prompts of GPTs](https://github.com/linexjlin/GPTs)

## Prompt Design

- Main Instructions - a task you want the model to perform
- Data - any input data (if necessary) 
- Output Instructions - what type of output do you want? What format?

```
### Instruction ###
<Main Instructions>:

<Output Instructions>:

<Data>:
```

### Examples

**출력 형식을 명시**
```
Extract a list of place names from the following input text

Desired Format:
Places: <comma_separated_list_of_names>
JSON array of place names

input: Alaska is a non-contiguous U.S. state on the northwest extremity of North America. It borders the Canadian province of British Columbia and the Yukon territory to the east; it shares a western maritime border in the Bering Strait with Russia's Chukotka Autonomous Okrug. The Chukchi and Beaufort Seas of the Arctic Ocean lie to the north and the Pacific Ocean lies to the south. Technically a semi-exclave of the U.S., Alaska is the largest exclave in the world.
```

**JSON 형식으로 출력**
```
Generate a list of the top 5 most populated countries in the world with their population

Desired Format: JSON object with country name as the key and population as the value
```

**변형**
```
Translate the following text to Spanish, French, and Japanese

Desired Format: 
JSON object with the language as key and text as value

Text: My favorite color is purple

JSON: 
```

**인칭, 시제 변형**
```
Transform the following text to 3rd person female in the future tence

Text: I love skiing so much. Today I went skiing with my best friends and I fell really hard and broke 34 bones. I cried for hours. Now I am almost dead.
```

**이모지**
```
Transform each movie title into an emoji

The Lion King:
```

**글 요약**
```
Summarize the following text in 2-3 sentences

Input: Psychology is the study of mind and behavior.[1] Its subject matter includes the behavior of humans and nonhumans, both conscious and unconscious phenomena, and mental processes such as thoughts, feelings, and motives. Psychology is an academic discipline of immense scope, crossing the boundaries between the natural and social sciences. Biological psychologists seek an understanding of the emergent properties of brains, linking the discipline to neuroscience. As social scientists, psychologists aim to understand the behavior of individuals and groups.[2][3]

A professional practitioner or researcher involved in the discipline is called a psychologist. Some psychologists can also be classified as behavioral or cognitive scientists. Some psychologists attempt to understand the role of mental functions in individual and social behavior. Others explore the physiological and neurobiological processes that underlie cognitive functions and behaviors.

Psychologists are involved in research on perception, cognition, attention, emotion, intelligence, subjective experiences, motivation, brain functioning, and personality. Psychologists' interests extend to interpersonal relationships, psychological resilience, family resilience, and other areas within social psychology. They also consider the unconscious mind.[4] Research psychologists employ empirical methods to infer causal and correlational relationships between psychosocial variables. Some, but not all, clinical and counseling psychologists rely on symbolic interpretation.

While psychological knowledge is often applied to the assessment and treatment of mental health problems, it is also directed towards understanding and solving problems in several spheres of human activity. By many accounts, psychology ultimately aims to benefit society.[5][6][7] Many psychologists are involved in some kind of therapeutic role, practicing psychotherapy in clinical, counseling, or school settings. Other psychologists conduct scientific research on a wide range of topics related to mental processes and behavior. Typically the latter group of psychologists work in academic settings (e.g., universities, medical schools, or hospitals). Another group of psychologists is employed in industrial and organizational settings.[8] Yet others are involved in work on human development, aging, sports, health, forensic science, education, and the media.
```

**분석**
```
Classify the following text's sentiment as positive, neutral, or negative 

Desired Format: a number -1 for negative, 0 for neutral, 1 for positive

Input:
This company is a Joke and it's not funny - Horrible Experience outlined ahead;

I was weighing 2 chatbot companies at the same time and today other chatbot App already responded to a customer service email in less than 4 hours. BotSonic took 4 days and still no solution. This is after taking 2 weeks to respond to my first email.

You guys should get your act together, it's too bad because you had what looked like a nice solution but your absolute LACK of customer service is a Huge Red Flag for me and I've decided to cancel my subscription.

You lost not only a customer but an Affiliate who has a YouTube channel of 18K subs
I hope you can solve this and become a better company but you have a long way to go!

Good luck and Good Bye!
Product Hunt should consider removing this company as they are nothing but trouble.
```

### Zero-shot Classification
- 아무런 예시나 데이터 없이 모델이 주어진 문제를 해결하는 것
- 보통 Zero-shot -> Few-shot 순으로 문제 해결

### Few-shot(One-shot) Classification
- 아주 적은 양의 데이터를 이용하여 모델이 주어진 문제를 해결하는 것
```
Extract keywords from the corresponding texts below.

Text 1: Stripe provides APIs that web developers can use to integrate payment processing into their websites and mobile applications.
Keywords 1: Stripe, payment processing, APIs, web developers, websites, mobile applications 
##

Text 2: OpenAI has trained cutting-edge language models that are very good at understanding and generating text. Our API provides access to these models and can be used to solve virtually any task that involves processing language.
Keywords 2: OpenAI, language models, text processing, API.
##

Text 3: {text} 
Keywords 3: 
```

### Chain of Thought Prompting
- [Large Language Models are Zero-Shot Reasoners](https://arxiv.org/abs/2205.11916) 논문에서 제안된 방법
- "Let's think step by step" 이라는 문구로 추론 능력을 향상시키는 방법

```
Alice is 7 years older than Beth, who is 5 years older than Erica. What is the difference between  the ages of Alice and Erica, If Erica is 30 years old?

Let's think step by step

answer: 
```
