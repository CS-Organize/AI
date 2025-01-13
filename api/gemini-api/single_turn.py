import google.generativeai as genai
from dotenv import dotenv_values

config = dotenv_values(".env")

genai.configure(api_key=config["GOOGLE_API_KEY"])
model = genai.GenerativeModel("gemini-pro")
response = model.generate_content("인공지능에 대해 한 문장으로 설명하세요.")

print(response.text)
