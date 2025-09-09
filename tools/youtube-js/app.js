// https://js.langchain.com/docs/integrations/document_loaders/web_loaders/youtube/

import { YoutubeLoader } from "@langchain/community/document_loaders/web/youtube";

const loader = YoutubeLoader.createFromUrl(
  "https://www.youtube.com/watch?v=9MTqnXqS1k0",
  {
    language: "ko",
    addVideoInfo: true,
  },
);

const docs = await loader.load();

console.log(docs);

// [
//   Document {
//     pageContent: ' [MUSIC] ANNOUNCER:\n' +
//       'Please welcome AI researcher and founding member of\n' +
//       'OpenAI, Andrej Karpathy. ANDREJ KARPATHY:\n' +
//       "Hi, everyone. I'm happy to be here to tell you\n" +
//       'about the state of GPT and more generally about the rapidly growing ecosystem\n' +
//       'of large language models. I would like to partition\n' +
//       'the talk into two parts. In the first part, I would\n' +
//       "like to tell you about how we train GPT Assistance, and then in the second part, we're going to take a\n" +
//       'look at how we can use these assistants effectively\n' +
//       "for your applications. First, let's take a\n" +
//       'look at the emerging recipe for how to train these assistants and keep\n' +
//       'in mind that this is all very new and still\n' +
//       'rapidly evolving, but so far, the recipe\n' +
//       'looks something like this. Now, this is a\n' +
//       "complicated slide, I'm going to go\n" +
//       'through it piece by  piece, but roughly speaking, we have four major\n' +
//       'stages, pretraining, supervised finetuning,\n' +
//       'reward modeling, reinforcement learning, and they follow each\n' +
//       'other serially. Now, in each stage, we have a dataset that\n' +
//       'powers that stage. We have an algorithm that\n' +
//       'for our purposes will be a objective and over for\n' +
//       'training the neural network, and then we have a\n' +
//       'resulting model, and then there are some\n' +
//       'notes on the bottom. The first stage\n' +
//       "we're going to start with as the pretraining stage. Now, this stage is\n" +
//       'special in this diagram, and this diagram is\n' +
//       'not to scale because this stage is where all of the computational work\n' +
//       'basically happens. This is 99 percent\n' +
//       'of the training compute time and also flops. This is where we\n' +
//       'are dealing with Internet scale datasets\n' +
//       'with thousands of GPUs in the supercomputer and also months of\n' +
//       'training potentially. The other three\n' +
//       'stages are finetuning stages that are much more along the lines of small few number\n' +
//       "of GPUs and hours or days. Let's take a look at\n" +
//       'the pretraining stage to achieve a base model. First, we are going to gather\n' +
//       "a large amount of data.  Here's an example\n" +
//       'of what we call a data mixture that comes from this paper that was released by Meta where they released\n' +
//       'this LLaMA based model. Now, you can see roughly\n' +
//       'the datasets that enter into these collections. We have CommonCrawl, which\n' +
//       'is a web scrape, C4, which is also CommonCrawl, and then some high\n' +
//       'quality datasets as well. For example, GitHub, Wikipedia, Books, Archives, Stock\n' +
//       'Exchange and so on. These are all mixed up together, and then they are sampled according to some\n' +
//       'given proportions, and that forms the\n' +
//       'training set for the GPT. Now before we can actually\n' +
//       'train on this data, we need to go through one\n' +
//       'more preprocessing step, and that is tokenization. This is basically\n' +
//       'a translation of the raw text that we scrape\n' +
//       "from the Internet into sequences of integers because that's the native representation over which GPTs function. Now, this is a\n" +
//       'lossless translation between pieces of texts\n' +
//       'and tokens and integers, and there are a number of\n' +
//       'algorithms for the stage. Typically, for\n' +
//       'example, you could use something like\n' +
//       'byte pair encoding, which iteratively\n' +
//       "merges text chunks and groups them into tokens. Here, I'm showing some example\n" +
//       'chunks of these tokens, and then this is the\n' +
//       'raw integer sequence that will actually feed\n' +
//       "into a transformer. Now, here I'm showing  two examples for\n" +
//       'hybrid parameters that govern this stage. GPT-4, we did not release too much information about\n' +
//       "how it was trained and so on, I'm using GPT-3s numbers, but GPT-3 is of course\n" +
//       'a little bit old by now, about three years ago. But LLaMA is a fairly\n' +
//       "recent model from Meta. These are roughly the orders of magnitude that we're dealing with when we're\n" +
//       'doing pretraining. The vocabulary size is usually\n' +
//       'a couple 10,000 tokens. The context length is usually\n' +
//       'something like 2,000, 4,000, or nowadays even 100,000, and this governs the maximum\n' +
//       'number of integers that the GPT will look at\n' +
//       "when it's trying to predict the next\n" +
//       'integer in a sequence. You can see that roughly the\n' +
//       'number of parameters say, 65 billion for LLaMA. Now, even though LLaMA\n' +
//       'has only 65B parameters compared to GPP-3s 175\n' +
//       'billion parameters, LLaMA is a significantly\n' +
//       "more powerful model, and intuitively, that's because the model is trained for\n" +
//       'significantly longer. In this case, 1.4\n' +
//       "trillion tokens, instead of 300 billion tokens. You shouldn't judge the\n" +
//       'power of a model by the number of parameters\n' +
//       "that it contains. Below, I'm showing\n" +
//       'some tables of rough hyperparameters\n' +
//       'that typically go into specifying the\n' +
//       'transformer neural network, the number of heads, the dimension size,\n' +
//       "number of layers, and so on, and on the bottom I'm showing some training\n" +
//       'hyperparameters. For example, to\n' +
//       'train the 65B model, Meta used 2,000 GPUs, roughly 21 days of training and a roughly several\n' +
//       "million dollars. That's the rough orders of\n" +
//       'magnitude that you should have in mind for the\n' +
//       "pre-training stage. Now, when we're actually\n" +
//       'pre-training, what happens? Roughly speaking, we are\n' +
//       "going to take our tokens, and we're going to lay them\n" +
//       'out into data batches. We have these arrays that will feed into\n' +
//       'the transformer, and these arrays are B, the batch size and these are\n' +
//       'all independent examples stocked up in rows and B by T, T being the maximum\n' +
//       'context length. In my picture I only have\n' +
//       '10 the context lengths, so this could be\n' +
//       '2,000, 4,000, etc. These are extremely long rows. What we do is we take\n' +
//       'these documents, and we pack them into rows, and we delimit them with these special end\n' +
//       'of texts tokens, basically telling\n' +
//       'the transformer where a new document begins. Here, I have a few examples\n' +
//       'of documents and then I stretch them out\n' +
//       "into this input. Now, we're going to feed all of these numbers into transformer. Let me just focus on a\n" +
//       'single particular cell, but the same thing\n' +
//       "will happen at every cell in this diagram. Let's look at the green cell. The green cell is going to take a look at all of the\n" +
//       "tokens before it, so all of the tokens in yellow, and we're going to feed\n" +
//       'that entire context into the transforming\n' +
//       'neural network, and the transformer\n' +
//       'is going to try to predict the next token in a sequence, in this case in red. Now the transformer,\n' +
//       "I don't have too much time to, unfortunately, go into the full details of this neural network architecture is just a large blob of neural\n" +
//       "net stuff for our purposes, and it's got several, 10 billion parameters typically\n" +
//       'or something like that. Of course, as I tune\n' +
//       "these parameters, you're getting slightly different predicted\n" +
//       'distributions for every single\n' +
//       'one of these cells. For example, if our vocabulary\n' +
//       "size is 50,257 tokens, then we're going\n" +
//       'to have that many numbers because we need to specify a probability distribution for\n' +
//       'what comes next. Basically, we have\n' +
//       "a probability for whatever may follow. Now, in this specific example, for this specific cell, 513 will come next, and so we can use this as a source of supervision to update our transformers weights. We're applying this basically on every single cell\n" +
//       "in the parallel, and we keep swapping batches, and we're trying to get\n" +
//       'the transformer to make the correct\n' +
//       'predictions over what token comes next in a sequence. Let me show you more\n' +
//       'concretely what this looks like when you train\n' +
//       'one of these models. This is actually coming\n' +
//       'from the New York Times, and they trained a small\n' +
//       "GPT on Shakespeare. Here's a small snippet\n" +
//       'of Shakespeare, and they train their GPT on it. Now, in the beginning, at initialization, the GPT starts with\n' +
//       "completely random weights. You're getting completely\n" +
//       'random outputs as well. But over time, as you train\n' +
//       'the GPT longer and longer, you are getting more\n' +
//       'and more coherent and consistent samples\n' +
//       'from the model, and the way you sample\n' +
//       'from it, of course, is you predict what comes next, you sample from that\n' +
//       'distribution and you keep feeding that\n' +
//       'back into the process, and you can basically\n' +
//       'sample large sequences. By the end, you see\n' +
//       'that the transformer has learned about words and where to put spaces and where\n' +
//       "to put commas and so on. We're making more and more consistent\n" +
//       'predictions over time. These are the plots\n' +
//       "that you are looking at when you're doing\n" +
//       "model pretraining. Effectively, we're looking at the loss function over\n" +
//       'time as you train, and low loss means\n' +
//       'that our transformer is giving a higher probability to the next correct\n' +
//       'integer in the sequence. What are we going\n' +
//       "to do with model once we've trained\n" +
//       'it after a month? Well, the first thing that\n' +
//       'we noticed, we the field,  is that these models basically in the process\n' +
//       'of language modeling, learn very powerful\n' +
//       "general representations, and it's possible to very\n" +
//       'efficiently fine tune them for any arbitrary\n' +
//       "downstream tasks you might be interested in. As an example, if you're interested in sentiment\n" +
//       'classification, the approach used to be that you collect a\n' +
//       'bunch of positives and negatives and then you\n' +
//       'train some NLP model for that, but the\n' +
//       'new approach is: ignore sentiment classification,\n' +
//       'go off and do large language model pretraining, train a large transformer, and then you may only\n' +
//       'have a few examples and you can very\n' +
//       'efficiently fine tune your model for that task. This works very\n' +
//       'well in practice. The reason for this\n' +
//       'is that basically the transformer is forced to multitask a huge amount of tasks in the language\n' +
//       'modeling task, because in terms of\n' +
//       "predicting the next token, it's forced to understand a\n" +
//       'lot about the structure of the text and all the\n' +
//       'different concepts therein. That was GPT-1. Now\n' +
//       'around the time of GPT-2, people noticed that actually even better than fine tuning, you can actually prompt these\n' +
//       'models very effectively. These are language\n' +
//       'models and they want to complete documents, you can actually trick\n' +
//       'them into performing tasks by arranging\n' +
//       'these fake documents. In this example, for example, we have some passage and\n' +
//       'then we like do QA, QA, QA. This is called Few-shot\n' +
//       'prompt, and then we do Q, and then as the\n' +
//       'transformer is tried to complete the document is\n' +
//       'actually answering our question. This is an example of prompt\n' +
//       'engineering based model, making it believe\n' +
//       "that it's imitating a document and getting\n" +
//       'it to perform a task. This kicked off, I think\n' +
//       'the era of, I would s'... 33277 more characters,
//     metadata: {
//       source: 'bZQun8Y4L2A',
//       description: 'Learn about the training pipeline of GPT assistants like ChatGPT, from tokenization to pretraining, supervised finetuning, and Reinforcement Learning from Human Feedback (RLHF). Dive deeper into practical techniques and mental models for the effective use of these models, including prompting strategies, finetuning, the rapidly growing ecosystem of tools, and their future extensions.\n' +
//         '\n' +
//         '*Speakers:*\n' +
//         ' * Andrej Karpathy\n' +
//         '\n' +
//         '\n' +
//         '*Session Information:*\n' +
//         'This video is one of many sessions delivered for the Microsoft Build 2023 event. View the full session schedule and learn more about Microsoft Build at https://build.microsoft.com \n' +
//         '\n' +
//         'BRK216HFS | English (US) | AI\n' +
//         '\n' +
//         '\n' +
//         '#MSBuild',
//       title: 'State of GPT | BRK216HFS',
//       view_count: 703674,
//       author: 'Microsoft Developer'
//     },
//     id: undefined
//   }
// ]
