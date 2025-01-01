# imports
import os
from dotenv import load_dotenv
import google.generativeai
from IPython.display import Markdown, display, update_display

load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')
anthropic_api_key = os.getenv('ANTHROPIC_API_KEY')
google_api_key = os.getenv('GOOGLE_API_KEY')

if not google_api_key:
    print("Google API Key not set")

google.generativeai.configure()
system_message = "You are a helpful assistant"
# for markdown responses system_message = "You are a helpful assistant that responds in Markdown"
def message_gemini(prompt):
    gemini = google.generativeai.GenerativeModel(
        model_name='gemini-1.5-flash',
        system_instruction=system_message
    )
    response = gemini.generate_content(prompt)
    return response.text
    # for markdown responses return return Markdown(response.text)
message_gemini("When do people named 'Vassilis' celebrate?")