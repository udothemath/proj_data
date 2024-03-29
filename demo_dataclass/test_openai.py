# %%
import time
import openai
import os

from dotenv import load_dotenv, find_dotenv
aa = load_dotenv(find_dotenv())
openai.api_key = os.getenv('OPENAI_API_KEY')
print(aa)
print(openai.api_key)
# %%


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,  # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


# %%
text = f"""
You should express what you want a model to do by \ 
providing instructions that are as clear and \ 
specific as you can possibly make them. \ 
This will guide the model towards the desired output, \ 
and reduce the chances of receiving irrelevant \ 
or incorrect responses. Don't confuse writing a \ 
clear prompt with writing a short prompt. \ 
In many cases, longer prompts provide more clarity \ 
and context for the model, which can lead to \ 
more detailed and relevant outputs.
"""
prompt = f"""
Summarize the text delimited by triple backticks \
into a single sentence.
\`\`\`{text}\`\`\`
"""

# prompt = f""" Greeting in 50 words"""

print(prompt)
response = get_completion(prompt)
print(response)
# %%


class C:
    def __init__(self):
        self.start = time.time()

    @property
    def age(self):
        return (time.time()-self.start)

    @age.setter
    def age(self, value):
        self.start = time.time()-value


# %%
curr = C()
print(curr.age)

# %%
print(curr.age)
# %%
print(curr.age)
# %%
curr.age = 999
print(curr.age)

# %%
