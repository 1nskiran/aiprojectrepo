from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client=OpenAI(base_url="https://generativelanguage.googleapis.com/v1beta/")

#zero shot
SYSTEM_PROMPT="You should answer questions related to human body. Otherthan this you should say sorry"

response=client.chat.completions.create(model="gemini-2.5-flash",
                                        messages=[{"role":"system","content":SYSTEM_PROMPT},
                                                  {"role":"user","content":"what is a computer?"}
                                                ])

print(response.choices[0].message.content)