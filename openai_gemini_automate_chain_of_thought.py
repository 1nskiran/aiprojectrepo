from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client=OpenAI(base_url="https://generativelanguage.googleapis.com/v1beta/")

SYSTEM_PROMPT="""Your name is Jai. You should work in chain of thought manner.
              You work on START, PLAN and OUTPUT steps
              You should first plan what needs to be done. The PLAN can have multiple steps.
              Once PLAN is done, finally you should give an OUTPUT

              Rules:
              1. Follow given JSON output format
              2. Run one step at a time
              3. The sequence of steps is START (accept input from user), PLAN (That can go multiple times) and then OUTPUT (show final output to user)

              output JSON format:
              { "step" :"START" | "PLAN" | "OUTPUT", "content::"string }

              Example:
                START: Hi Jai, give me sample while loop in python
                PLAN: {'step":"PLAN":"content":"it appears that user is not aware of python language at all"}
                PLAN: {"step":"PLAN":"content":"Let me check in my knowledge base for python computer language"}
                PLAN: {"step":"PLAN":"content":"Yes, I found python computer language details in my knowledge base"}
                PLAN:{"step":"PLAN":"content":"first search for while loop syntax in python and prepare sample code for while loop"}
                OUTPUT: {"step":"OUTPUT":"content":"while i<5:\n    print(i)\n    i += 1"}
"""
print("\n\n")
message_history=[{"role":"system","content":SYSTEM_PROMPT}]

user_query=input("Hi Jai")
message_history.append({"role":"user","content":user_query})
 

import json

while True: 
    print()
    response=client.chat.completions.create(model="gemini-2.5-flash", 
                                            response_format={"type":"json_object"},
                                            messages=message_history) 
    print()
    assistant_result=response.choices[0].message.content
    message_history.append({"role":"assistant","content":assistant_result})
    parsed_result=json.loads(assistant_result)

    if parsed_result.get("step") == "START":
        print("Starting..",parsed_result.get("content"))
        continue
    
    if parsed_result.get("step") == "PLAN":
        print('Planning..',parsed_result.get("content"))
        continue
    
    if parsed_result.get("step") == "OUTPUT":
        print("Final output..",parsed_result.get("content"))
        break

print("\n\n")