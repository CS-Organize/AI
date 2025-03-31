# Whisper

- [github](https://github.com/ml-explore/mlx-examples/tree/main/whisper)

<!-- `whisper <audio> --language ko --output_format srt --max_line_width 15 --model large --device mps --fp16 False` -->

```bash
mlx_whisper \
--model mlx-community/whisper-large-v3-turbo \
--output-dir ./output \
--output-format srt \
--language ko \
--task transcribe \
--condition-on-previous-text False \
--word-timestamps True \
--max-line-width 15 \
--max-line-count 1 \
<audio>
```

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

```python
# https://github.com/ml-explore/mlx-examples/blob/main/whisper/mlx_whisper/cli.py
def build_parser():
    def optional_int(string):
        return None if string == "None" else int(string)

    def optional_float(string):
        return None if string == "None" else float(string)

    def str2bool(string):
        str2val = {"True": True, "False": False}
        if string in str2val:
            return str2val[string]
        else:
            raise ValueError(f"Expected one of {set(str2val.keys())}, got {string}")

    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument("audio", nargs="+", help="Audio file(s) to transcribe")

    parser.add_argument(
        "--model",
        default="mlx-community/whisper-tiny",
        type=str,
        help="The model directory or hugging face repo",
    )
    parser.add_argument(
        "--output-name",
        type=str,
        default=None,
        help=(
            "The name of transcription/translation output files before "
            "--output-format extensions"
        ),
    )
    parser.add_argument(
        "--output-dir",
        "-o",
        type=str,
        default=".",
        help="Directory to save the outputs",
    )
    parser.add_argument(
        "--output-format",
        "-f",
        type=str,
        default="txt",
        choices=["txt", "vtt", "srt", "tsv", "json", "all"],
        help="Format of the output file",
    )
    parser.add_argument(
        "--verbose",
        type=str2bool,
        default=True,
        help="Whether to print out progress and debug messages",
    )
    parser.add_argument(
        "--task",
        type=str,
        default="transcribe",
        choices=["transcribe", "translate"],
        help="Perform speech recognition ('transcribe') or speech translation ('translate')",
    )
    parser.add_argument(
        "--language",
        type=str,
        default=None,
        choices=sorted(LANGUAGES.keys())
        + sorted([k.title() for k in TO_LANGUAGE_CODE.keys()]),
        help="Language spoken in the audio, specify None to auto-detect",
    )
    parser.add_argument(
        "--temperature", type=float, default=0, help="Temperature for sampling"
    )
    parser.add_argument(
        "--best-of",
        type=optional_int,
        default=5,
        help="Number of candidates when sampling with non-zero temperature",
    )
    parser.add_argument(
        "--patience",
        type=float,
        default=None,
        help="Optional patience value to use in beam decoding, as in https://arxiv.org/abs/2204.05424, the default (1.0) is equivalent to conventional beam search",
    )
    parser.add_argument(
        "--length-penalty",
        type=float,
        default=None,
        help="Optional token length penalty coefficient (alpha) as in https://arxiv.org/abs/1609.08144, uses simple length normalization by default.",
    )
    parser.add_argument(
        "--suppress-tokens",
        type=str,
        default="-1",
        help="Comma-separated list of token ids to suppress during sampling; '-1' will suppress most special characters except common punctuations",
    )
    parser.add_argument(
        "--initial-prompt",
        type=str,
        default=None,
        help="Optional text to provide as a prompt for the first window.",
    )
    parser.add_argument(
        "--condition-on-previous-text",
        type=str2bool,
        default=True,
        help="If True, provide the previous output of the model as a prompt for the next window; disabling may make the text inconsistent across windows, but the model becomes less prone to getting stuck in a failure loop",
    )
    parser.add_argument(
        "--fp16",
        type=str2bool,
        default=True,
        help="Whether to perform inference in fp16",
    )
    parser.add_argument(
        "--compression-ratio-threshold",
        type=optional_float,
        default=2.4,
        help="if the gzip compression ratio is higher than this value, treat the decoding as failed",
    )
    parser.add_argument(
        "--logprob-threshold",
        type=optional_float,
        default=-1.0,
        help="If the average log probability is lower than this value, treat the decoding as failed",
    )
    parser.add_argument(
        "--no-speech-threshold",
        type=optional_float,
        default=0.6,
        help="If the probability of the token is higher than this value the decoding has failed due to `logprob_threshold`, consider the segment as silence",
    )
    parser.add_argument(
        "--word-timestamps",
        type=str2bool,
        default=False,
        help="Extract word-level timestamps and refine the results based on them",
    )
    parser.add_argument(
        "--prepend-punctuations",
        type=str,
        default="\"'“¿([{-",
        help="If word-timestamps is True, merge these punctuation symbols with the next word",
    )
    parser.add_argument(
        "--append-punctuations",
        type=str,
        default="\"'.。,，!！?？:：”)]}、",
        help="If word_timestamps is True, merge these punctuation symbols with the previous word",
    )
    parser.add_argument(
        "--highlight-words",
        type=str2bool,
        default=False,
        help="(requires --word_timestamps True) underline each word as it is spoken in srt and vtt",
    )
    parser.add_argument(
        "--max-line-width",
        type=int,
        default=None,
        help="(requires --word_timestamps True) the maximum number of characters in a line before breaking the line",
    )
    parser.add_argument(
        "--max-line-count",
        type=int,
        default=None,
        help="(requires --word_timestamps True) the maximum number of lines in a segment",
    )
    parser.add_argument(
        "--max-words-per-line",
        type=int,
        default=None,
        help="(requires --word_timestamps True, no effect with --max_line_width) the maximum number of words in a segment",
    )
    parser.add_argument(
        "--hallucination-silence-threshold",
        type=optional_float,
        help="(requires --word_timestamps True) skip silent periods longer than this threshold (in seconds) when a possible hallucination is detected",
    )
    parser.add_argument(
        "--clip-timestamps",
        type=str,
        default="0",
        help="Comma-separated list start,end,start,end,... timestamps (in seconds) of clips to process, where the last end timestamp defaults to the end of the file",
    )
    return parser
```

각 인자에 대한 설명을 해드리겠습니다:

1. 기본 인자:

- `audio`: 변환할 오디오 파일 경로 (필수)

2. 모델 관련:

- `--model`: 사용할 모델 경로나 Hugging Face 저장소 (기본값: "mlx-community/whisper-tiny")
- `--fp16`: FP16 추론 사용 여부 (기본값: True)

3. 출력 관련:

- `--output-name`: 출력 파일 이름
- `--output-dir`: 출력 파일 저장 디렉토리 (기본값: 현재 디렉토리)
- `--output-format`: 출력 파일 형식 (txt/vtt/srt/tsv/json/all) (기본값: "txt")
- `--verbose`: 진행 상황 출력 여부 (기본값: True)

4. 작업 설정:

- `--task`: 작업 유형 (transcribe/translate) (기본값: "transcribe")
- `--language`: 오디오의 언어 (자동 감지는 None)

5. 생성 매개변수:

- `--temperature`: 샘플링 온도 (기본값: 0)
- `--best-of`: 비제로 온도에서의 후보 수 (기본값: 5)
- `--patience`: 빔 디코딩의 인내 값
- `--length-penalty`: 토큰 길이 페널티 계수
- `--suppress-tokens`: 샘플링 중 제외할 토큰 ID 목록
- `--initial-prompt`: 첫 번째 윈도우의 프롬프트 텍스트
- `--condition-on-previous-text`: 이전 출력을 다음 윈도우의 프롬프트로 사용 (기본값: True)

6. 품질 관련:

- `--compression-ratio-threshold`: gzip 압축 비율 임계값 (기본값: 2.4)
- `--logprob-threshold`: 평균 로그 확률 임계값 (기본값: -1.0)
- `--no-speech-threshold`: 무음 감지 임계값 (기본값: 0.6)

7. 단어 타임스탬프 관련:

- `--word-timestamps`: 단어 수준 타임스탬프 추출 (기본값: False)
- `--prepend-punctuations`: 다음 단어와 병합할 구두점
- `--append-punctuations`: 이전 단어와 병합할 구두점
- `--highlight-words`: 발화 단어 강조 표시
- `--max-line-width`: 줄당 최대 문자 수
- `--max-line-count`: 세그먼트당 최대 줄 수
- `--max-words-per-line`: 줄당 최대 단어 수
- `--hallucination-silence-threshold`: 환각 감지시 무시할 무음 기간 임계값
- `--clip-timestamps`: 처리할 클립의 시작/종료 타임스탬프

예시 명령어:

```bash
mlx_whisper \
  input.mp3 \
  --model mlx-community/whisper-large-v3 \
  --output-dir ./outputs \
  --output-format srt \
  --language ko \
  --task transcribe \
  --word-timestamps True \
  --max-line-width 15 \
  --max-line-count 2 \
  --highlight-words True \
  --temperature 0.2 \
  --best-of 5 \
  --condition-on-previous-text False \
  --fp16 True \
  --verbose True
```

## Bug

https://huggingface.co/mlx-community/whisper-large-v3-mlx/discussions/4#674de7ed37268b0dca069695
