import requests
import json
import os
from dotenv import load_dotenv
import yaml

# Load variables from the .env file
def  call_spec_assistant(file_name, program):
    load_dotenv()

    BASE_URL = os.getenv('BASE_URL')
    SAIA_PROJECT_APITOKEN = os.getenv('SAIA_PROJECT_APITOKEN')
    ASSISTANT_NAME = os.getenv('SPEC_ASSISTANT_NAME')

    # Define the headers
    headers = {
        "Content-Type": "application/json",
        #Authorization": f"Bearer {SAIA_PROJECT_APITOKEN}"
        "Saia-Auth": SAIA_PROJECT_APITOKEN,
        "X-Saia-Cache-Enabled": "false"
    }

    # Define the payload
    payload = {
        "model": f"saia:assistant:{ASSISTANT_NAME}",
        "messages": [
            {
                "role": "user",
                "content": program
            }
        ],
        "stream": "false"
    }

    # Make the POST request
    response = requests.post(f"{BASE_URL}", headers=headers, json=payload)

    # Save the content to response.txt
    json_data = json.loads(response.text)
    mk_answer = json_data['choices'][0]['message']['content']
    answer = remove_first_and_last_line(mk_answer)
    print(answer)
    try:
        content = yaml.safe_load(answer)
        content['file_name'] = file_name
        return content
    except yaml.YAMLError as e:
        print(f"Error loading YAML: {e}")
        return None 

def remove_first_and_last_line(text):
    # Split the text into lines
    lines = text.splitlines()
    
    # Check if there are at least two lines to remove
    if len(lines) <= 2:
        return ""  # Return an empty string if there are two or fewer lines
    
    # Join the lines, excluding the first and last
    new_text = '\n'.join(lines[1:-1])
    
    return new_text
