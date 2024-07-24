
import google.generativeai as genai

api_key = "AIzaSyASy8RA397eN5yFSD2EfuKDgDZ64b5IawA"
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

while True:
    prompt = input("Enter your Prompt Here....")

    response = model.generate_content(prompt)
    print(response.text)
