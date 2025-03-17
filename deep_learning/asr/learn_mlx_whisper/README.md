# Whisper

- [github](https://github.com/openai/whisper)

`whisper <audio> --language ko --output_format srt --max_line_width 15 --model large --device mps --fp16 False`
`mlx_whisper --language ko --output-format srt --word-timestamps True --max-line-width 15 --model mlx-community/whisper-large-v3-turbo --output-dir output --condition-on-previous-text False <audio>`

## Usage

```bash
usage: mlx_whisper [-h] [--model MODEL] [--output-name OUTPUT_NAME]
                   [--output-dir OUTPUT_DIR]
                   [--output-format {txt,vtt,srt,tsv,json,all}]
                   [--verbose VERBOSE] [--task {transcribe,translate}]
                   [--language {af,am,ar,as,az,ba,be,bg,bn,bo,br,bs,ca,cs,cy,da,de,el,en,es,et,eu,fa,fi,fo,fr,gl,gu,ha,haw,he,hi,hr,ht,hu,hy,id,is,it,ja,jw,ka,kk,km,kn,ko,la,lb,ln,lo,lt,lv,mg,mi,mk,ml,mn,mr,ms,mt,my,ne,nl,nn,no,oc,pa,pl,ps,pt,ro,ru,sa,sd,si,sk,sl,sn,so,sq,sr,su,sv,sw,ta,te,tg,th,tk,tl,tr,tt,uk,ur,uz,vi,yi,yo,yue,zh,Afrikaans,Albanian,Amharic,Arabic,Armenian,Assamese,Azerbaijani,Bashkir,Basque,Belarusian,Bengali,Bosnian,Breton,Bulgarian,Burmese,Cantonese,Castilian,Catalan,Chinese,Croatian,Czech,Danish,Dutch,English,Estonian,Faroese,Finnish,Flemish,French,Galician,Georgian,German,Greek,Gujarati,Haitian,Haitian Creole,Hausa,Hawaiian,Hebrew,Hindi,Hungarian,Icelandic,Indonesian,Italian,Japanese,Javanese,Kannada,Kazakh,Khmer,Korean,Lao,Latin,Latvian,Letzeburgesch,Lingala,Lithuanian,Luxembourgish,Macedonian,Malagasy,Malay,Malayalam,Maltese,Mandarin,Maori,Marathi,Moldavian,Moldovan,Mongolian,Myanmar,Nepali,Norwegian,Nynorsk,Occitan,Panjabi,Pashto,Persian,Polish,Portuguese,Punjabi,Pushto,Romanian,Russian,Sanskrit,Serbian,Shona,Sindhi,Sinhala,Sinhalese,Slovak,Slovenian,Somali,Spanish,Sundanese,Swahili,Swedish,Tagalog,Tajik,Tamil,Tatar,Telugu,Thai,Tibetan,Turkish,Turkmen,Ukrainian,Urdu,Uzbek,Valencian,Vietnamese,Welsh,Yiddish,Yoruba}]
                   [--temperature TEMPERATURE] [--best-of BEST_OF]
                   [--patience PATIENCE] [--length-penalty LENGTH_PENALTY]
                   [--suppress-tokens SUPPRESS_TOKENS]
                   [--initial-prompt INITIAL_PROMPT]
                   [--condition-on-previous-text CONDITION_ON_PREVIOUS_TEXT]
                   [--fp16 FP16]
                   [--compression-ratio-threshold COMPRESSION_RATIO_THRESHOLD]
                   [--logprob-threshold LOGPROB_THRESHOLD]
                   [--no-speech-threshold NO_SPEECH_THRESHOLD]
                   [--word-timestamps WORD_TIMESTAMPS]
                   [--prepend-punctuations PREPEND_PUNCTUATIONS]
                   [--append-punctuations APPEND_PUNCTUATIONS]
                   [--highlight-words HIGHLIGHT_WORDS]
                   [--max-line-width MAX_LINE_WIDTH]
                   [--max-line-count MAX_LINE_COUNT]
                   [--max-words-per-line MAX_WORDS_PER_LINE]
                   [--hallucination-silence-threshold HALLUCINATION_SILENCE_THRESHOLD]
                   [--clip-timestamps CLIP_TIMESTAMPS]
                   audio [audio ...]
mlx_whisper: error: the following arguments are required: audio
```

## Bug

https://huggingface.co/mlx-community/whisper-large-v3-mlx/discussions/4#674de7ed37268b0dca069695
