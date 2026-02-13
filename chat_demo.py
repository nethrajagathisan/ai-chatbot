from google import genai
from google.genai import types

client = genai.Client()

print("chat starts here...type 'endchat' to close")
chat = []

userinput = input("User : ")

while userinput != "endchat": 
    chat.append("User : " +userinput)
    systemoutput = client.models.generate_content(
        contents = chat,
        model = 'gemini-2.5-flash',
        config = types.GenerateContentConfig(
            system_instruction = "Respond in one line, within 20 characters",
        )
    )
    chat.append("Chatbot : " +systemoutput.text)
    print("Chatbot : " + systemoutput.text)
    userinput = input("User : ")