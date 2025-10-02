from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client=OpenAI(api_key="",
              base_url="https://generativelanguage.googleapis.com/v1beta/")

response=client.chat.completions.create(model="gemini-2.5-flash",
                                        messages=[{"role":"user",
                                                   "content":"I am x! Nice to meet you. Who are you?"}])

print(response.choices[0].message.content)