import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = "/opt/homebrew/bin/tesseract"

a = Image.open("영수증.jpg")
result = pytesseract.image_to_string(a, lang="kor")

print(result)
