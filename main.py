
import google.generativeai as genai

api_key = "paste your key here..."
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

while True:
    prompt = input("Enter your Prompt Here....")

    response = model.generate_content(prompt)
    print(response.text)
