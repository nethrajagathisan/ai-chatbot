from google import genai
from google.genai import types

client = genai.Client()

prompt = input("Enter your prompt: ")

response = client.models.generate_content(
    model = 'gemini-2.5-flash',
    contents = prompt,
    config = types.GenerateContentConfig(
        system_instruction = "Respond in exactly one line",
        temperature = 0.5
    )
)

print(response.text)