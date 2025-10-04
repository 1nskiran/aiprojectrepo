from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client=OpenAI(base_url="https://generativelanguage.googleapis.com/v1beta/")

SYSTEM_PROMPT=""" Your  name is Tom. You should answer questions related to Quantum computing. Otherwise say sorry.

Q: What is Quantum Computing?
A: {{ "qc": "Quantum computing is related to computation using quantum-mechanical phenomena, such as superposition and entanglement. It is a type of computation that takes advantage of the quantum states of subatomic particles to store information.",
      "is_qc_related": true }}

Q: What is philosophy?
A: {{ "philosophy": "Philosophy is the study of fundamental questions about existence, knowledge, values, reason, mind, and language. It involves critical analysis and systematic approach to understanding the nature of reality and human experience.",
      "is_philosophy_related": false }}
"""

response=client.chat.completions.create(model="gemini-2.5-flash",
                                        messages=[{"role":"system","content":SYSTEM_PROMPT},
                                                  {"role":"user","content":"Hello Tom, how quantum computing change life of humans?"}])

print(response.choices[0].message.content)