import requests
import json
import os
from dotenv import load_dotenv
import click
import gxeai.call_spec_assistant
import yaml
from pathlib import Path

@click.command()
@click.option('--programs_directory', help='a directory with the programs to specify')
@click.option('--spec_path',  help='a path to output yaml with specifications of procedures.')
def anything_to_spec(programs_directory, spec_path):
    specs = [] 
    folder = Path(programs_directory)
    if folder.is_dir():
        for file_path in folder.iterdir():
            if file_path.is_file():
                path = Path(file_path)
                name = path.name
                with open(file_path, 'r') as file:
                    content = file.read()
                    try:
                        print(f"Processing {name}")
                        spec = gxeai.call_spec_assistant.call_spec_assistant(name, content)
                        specs.append(spec)
                    except Exception as e:
                        print(f"Error reading file: {e}")
                        print(name)
                        print(content)
            elif file_path.is_dir():
                print(f"Found directory: {file_path.name}")
    else:
        print(f"{folder_path} is not a valid directory")

    # Save the YAML objects to a file
    with open(spec_path, 'w') as file:
        yaml.dump(specs, file, default_flow_style=False)

if __name__ == "__main__":
    anything_to_spec()
