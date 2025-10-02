from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client=OpenAI(base_url="https://generativelanguage.googleapis.com/v1beta/")

response=client.chat.completions.create(model="gemini-2.5-flash",
                                        messages=[{"role":"system","content":"You are an expert in Quantum Computing and you should focus on topics relted to Quantum Computing only. If you need to answer questions not pertaining to Quantum Computing, just say sorry and you do not wish to go out of context"},
                                            {"role":"user","content":"What's the role of python programming language data analytics?"}])

print(response.choices[0].message.content)