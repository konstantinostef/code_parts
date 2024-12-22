# imports

import os
import requests
from dotenv import load_dotenv

# Load environment variables in a file called .env

load_dotenv()
google_api_key = os.getenv('GOOGLE_API_KEY')
search_engine_id = os.getenv('SEARCH_ENGINE_ID')

search_query = 'Κώστας Στεφανόπουλος'

url = 'https://www.googleapis.com/customsearch/v1'

parameters = {
    'q': search_query,
    'key': google_api_key,
    'cx': search_engine_id
}

response = requests.get(url=url, params=parameters)
results = response.json()
print(results)