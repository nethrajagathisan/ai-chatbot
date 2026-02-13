from google import genai
from google.genai import types  

client = genai.Client()

grounding_tool = types.Tool(
    google_search = types.GoogleSearch()
)
response = client.models.generate_content(
    model = 'gemini-2.5-flash',
    contents = "What won the world cup in 2026?"
    config = types.GenerateContentConfig(
        tools = [grounding_tool]
    )
)

print(response.text)    