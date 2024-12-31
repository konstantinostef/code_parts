import os
from dotenv import load_dotenv
import anthropic
from IPython.display import Markdown, display, update_display

# Load environment variables in a file called .env
# Print the key prefixes to help with any debugging

load_dotenv()
anthropic_api_key = os.getenv('ANTHROPIC_API_KEY')

# Connect to Anthropics API

claude = anthropic.Anthropic()

system_message = "You are an assistant that is great at python."
user_prompt = """Can you explain what is this code doing: 
with result as stream:
    for text in stream.text_stream:
            print(text, end="", flush=True)."""

# Claude 3.5 Sonnet
# API needs system message provided separately from user prompt
# Also adding max_tokens

# And now: call the Anthropics API.

def askClaude():
    response = claude.messages.create(
    model="claude-3-5-sonnet-20240620",
    max_tokens=200,
    temperature=0.7,
    system=system_message,
    messages=[
        {"role": "user", "content": user_prompt},
    ],
    )
    return response.content[0].text

def askClaudeStream():
    response = claude.messages.stream(
    model="claude-3-5-sonnet-20240620",
    max_tokens=200,
    temperature=0.7,
    system=system_message,
    messages=[
        {"role": "user", "content": user_prompt},
    ],
    )
    return response

# A function to display this nicely in the Jupyter output, using markdown

def getClaudeResponse():
    response = askClaude()
    display(response.content[0].text)

def getClaudeResponseStream():
    response = askClaudeStream()
    # Return Response as Stream
    with response as stream:
        for text in stream.text_stream:
            print(text, end="", flush=True)
getClaudeResponse()
# OR
#getClaudeResponseStream()