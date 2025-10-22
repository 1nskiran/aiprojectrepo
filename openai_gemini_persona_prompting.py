from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client=OpenAI(base_url="https://generativelanguage.googleapis.com/v1beta/")

SYSTEM_PROMPT="""
    Your name is James. You are working on behalf of a company with name SoleEnergy,which is into solar energy solutions.
    Company has multiple personas like sales, support, technical, management etc.
    Based on the user query, you should identify the correct persona and respond accordingly.
"""

response=client.chat.completions.create(model="gemini-2.5-flash",
                                        messages=[{"role":"system","content":SYSTEM_PROMPT},
                                                  {"role":"user","content":"Hi James"}])

print(response.choices[0].message.content)