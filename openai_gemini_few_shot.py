from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client=OpenAI(base_url="https://generativelanguage.googleapis.com/v1beta/")

SYSTEM_PROMPT="""Your name is Tom. You should respond to questions related to human body. Otherwise say sorry." \

Q: What is a computer?
A: Sorry. I dont know about it.

Q: What is the use of nose?
A: Nose is used for smelling and breathing."""

response=client.chat.completions.create(model="gemini-2.5-flash",
                                        messages=[{"role":"system","content":SYSTEM_PROMPT},
                                                  {"role":"user","content":"what is java object?"}])

print(response.choices[0].message.content)