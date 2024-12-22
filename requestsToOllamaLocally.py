# imports

import requests
from IPython.display import Markdown, display

# Constants

OLLAMA_API = "http://localhost:11434/api/chat"
HEADERS = {"Content-Type": "application/json"}
MODEL = "llama3.2"

# Create a messages list using the same format that we used for OpenAI

messages = [
    {"role":"system","content":"You are a secretary of a person. Respond only with one word: phonecall if he asks to make a phonecall or email if he asks to send an email."},
    {"role": "user", "content": "Please, Betty, call my friend Mike on the phone to tell him i can't go to the gym today!"}
]


# first approach using requests library
payload = {
    "model": MODEL,
    "messages": messages,
    "stream": False
}

response = requests.post(OLLAMA_API, json=payload, headers=HEADERS)
print(response.json()['message']['content'])

# another approach OpenAI client python library

# There's actually an alternative approach that some people might prefer
# You can use the OpenAI client python library to call Ollama:

from openai import OpenAI
ollama_via_openai = OpenAI(base_url='http://localhost:11434/v1', api_key='ollama')

response = ollama_via_openai.chat.completions.create(
    model=MODEL,
    messages=messages
)

print(response.choices[0].message.content)