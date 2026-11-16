# import openai

# # Set OpenAI API key
# openai.api_key = ""

# try:
#     # Generate text using GPT-3.5 Turbo
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role":"system","content":"You are a helpful assistant."},
#             {"role":"user","content":"Write a short story about a robot learning to cook."}
#         ],
#         max_tokens=150,
#         temperature=0.7
#     )

#     print("Generated Text:\n", response["choices"][0]["message"]["content"].strip())

# except Exception as e:
#     print(f"An error occured: {e}")


import os
from dotenv import load_dotenv
from openai import OpenAI

# Load OPENAI_API_KEY from your local .env file
load_dotenv()

# Initialize the modern OpenAI client (automatically reads OPENAI_API_KEY from environment)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

try:
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # Faster, cheaper, and newer replacement for gpt-3.5-turbo
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Write a short story about a robot learning to cook."},
        ],
        max_tokens=150,
        temperature=0.7,
    )

    # Access response attributes with dot notation instead of dictionary keys
    print("Generated Text:\n", response.choices[0].message.content.strip())

except Exception as e:
    print(f"An error occurred: {e}")