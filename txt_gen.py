from google import genai
from google.genai import types
from PIL import Image

client = genai.Client()

prompt = input("Enter your prompt: ")
image = Image.open("img/cat.jpg")

response = client.models.generate_content_stream(
    model = 'gemini-2.5-flash',
    contents = [image, prompt],
    config = types.GenerateContentConfig(
        system_instruction = "Response in a funny way",
        temperature = 0.5
    )
)

for chunk in response:
    print(chunk.text, end="---\n---")

# print(response.text)