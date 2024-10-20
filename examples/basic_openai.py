from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "system",
               "content": "Você é um assistente de conta na exchange bitypreco", },
              {"role": "user",
               "content": "Olá!"
               }
              ],
)

content = response.choices[0].message.content
print(content)
