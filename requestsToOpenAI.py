# imports

import os
import requests
from dotenv import load_dotenv
from IPython.display import Markdown, display
from openai import OpenAI

# Load environment variables in a file called .env

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

# Check the key

if not api_key:
    print("No API key was found - please head over to the troubleshooting notebook in this folder to identify & fix!")
elif not api_key.startswith("sk-proj-"):
    print("An API key was found, but it doesn't start sk-proj-; please check you're using the right key - see troubleshooting notebook")
elif api_key.strip() != api_key:
    print("An API key was found, but it looks like it might have space or tab characters at the start or end - please remove them - see troubleshooting notebook")


openai = OpenAI()

# FIRST WAY TO CALL OPENAI API - FUNCTIONAL

# A generic system message
system_message = "You are a helpful assistant"

# Let's wrap a call to GPT-4o-mini in a simple function
def message_gpt(prompt):
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": prompt}
      ]
    completion = openai.chat.completions.create(
        model='gpt-4o-mini',
        messages=messages,
    )
    return completion.choices[0].message.content
message_gpt("What is today's date?")
#END OF FIRST WAY TO CALL OPENAI API

# SECOND WAY TO CALL OPENAI API
# Define our system prompt - you can experiment with this later, changing the last sentence to 'Respond in markdown in Spanish."

system_prompt = "You are a secretary. You have to understand what is your boss saying. If he wants you to send an email or to make a phone call. Respond with all details of his request."
user_prompt = "Hello Betty! Please call my colleague Mike on the phone. "

# See how this function creates exactly the format above

messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]

# And now: call the OpenAI API. You will get very familiar with this!

def askOpenAI():
    response = openai.chat.completions.create(
        model = "gpt-4o-mini",
        messages = messages
    )
    return response.choices[0].message.content

def askOpenAIStream():
    response = openai.chat.completions.create(
        model = "gpt-4o-mini",
        messages = messages,
        stream = True
    )
    return response

# A function to display this nicely in the Jupyter output, using markdown

def getOpenAIResponse():
    response = askOpenAI()
    display(response)

def getOpenAIResponseStream():
    response = askOpenAIStream()
    # Return Response as Stream
    result = ""
    for chunk in response:
        result += chunk.choices[0].delta.content or ""
        yield result

getOpenAIResponse()
# OR
# getOpenAIResponseStream()