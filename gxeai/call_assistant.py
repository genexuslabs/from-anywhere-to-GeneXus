import requests
import json
import os
from dotenv import load_dotenv
import click
import gxeai.clean_proc

# Load variables from the .env file
def call_assistant(assistant, name, spec):
    load_dotenv()

    BASE_URL = os.getenv('BASE_URL')
    SAIA_PROJECT_APITOKEN = os.getenv('SAIA_PROJECT_APITOKEN')

    # Define the headers
    headers = {
        "Content-Type": "application/json",
        #Authorization": f"Bearer {SAIA_PROJECT_APITOKEN}"
        "Saia-Auth": SAIA_PROJECT_APITOKEN,
        "X-Saia-Cache-Enabled": "false"
    }

    # Define the payload
    payload = {
        "model": f"saia:assistant:{assistant}",
        "messages": [
            {
                "role": "user",
                "content": spec
            }
        ],
        "stream": "false"
    }

    # Make the POST request
    response = requests.post(f"{BASE_URL}", headers=headers, json=payload)

    # Save the content to response.txt
    json_data = json.loads(response.text)
    answer = json_data['choices'][0]['message']['content']
    content = gxeai.clean_proc.parse_procedure(answer, name)
    content['description'] = spec
    return content


@click.command()
@click.option('--spec', default='use Abs function correctly by receiving and returing a number', help='spec for your proc')
def test_main(spec):
    content = call_proc_assistant(spec)
    with open("response.txt", "w") as file:
        multiline =json.dumps(content, indent=4)
        file.write(multiline)
        print("Response saved to response.txt")

if __name__ == "__main__":
    test_main()
