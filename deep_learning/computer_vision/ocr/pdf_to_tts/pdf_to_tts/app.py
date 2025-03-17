from PIL import Image, ImageOps, ImageFilter
from gtts import gTTS
import pdf2image
from tqdm import tqdm
from ocrmac import ocrmac


def extract_text_from_image(image_path):
    image = Image.open(image_path)
    # Convert to grayscale
    image = ImageOps.grayscale(image)
    # Simple noise reduction (median filter)
    image = image.filter(ImageFilter.MedianFilter(size=3))
    # Optionally, upscale image to improve OCR
    image = image.resize((image.width * 2, image.height * 2), Image.Resampling.LANCZOS)
    annotations = ocrmac.OCR(image, language_preference=["ko-KR", "en-US"]).recognize()
    text = " ".join([annotation[0] for annotation in annotations])
    return text


def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        images = pdf2image.convert_from_path(pdf_path)
        for image in tqdm(images, desc="Extracting PDF pages"):
            # Grayscale + noise removal
            image = ImageOps.grayscale(image)
            image = image.filter(ImageFilter.MedianFilter(size=3))
            # Upscale image
            image = image.resize(
                (image.width * 2, image.height * 2), Image.Resampling.LANCZOS
            )
            annotations = ocrmac.OCR(
                image, language_preference=["ko-KR", "en-US"]
            ).recognize()
            text += " ".join([annotation[0] for annotation in annotations]) + " "
        if not text.strip():
            print("Warning: no text extracted.")
            return ""
    except Exception as e:
        print(f"Error: {str(e)}")
        return ""
    return text


def preprocess_text(text):
    text = " ".join(text.split())
    return text.replace("\n", " ")


def text_to_speech(text, output_mp3_path, language="ko"):
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save(output_mp3_path)


def file_to_tts(file_path, output_mp3_path, language="ko"):
    with tqdm(total=3, desc="Overall process") as pbar:
        pbar.set_description("Extracting text")
        if file_path.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".gif")):
            text = extract_text_from_image(file_path)
        elif file_path.lower().endswith(".pdf"):
            text = extract_text_from_pdf(file_path)
        else:
            raise ValueError("Unsupported file type.")
        pbar.update(1)

        pbar.set_description("Preprocessing text")
        cleaned_text = preprocess_text(text)
        pbar.update(1)

        pbar.set_description("Converting to TTS")
        text_to_speech(cleaned_text, output_mp3_path, language)
        pbar.update(1)
        print(f"TTS saved: {output_mp3_path}")


import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python app.py <file_path>")
        sys.exit(1)
    file_path = sys.argv[1]
    output_mp3_path = "output.mp3"
    language = "ko"
    file_to_tts(file_path, output_mp3_path, language)
