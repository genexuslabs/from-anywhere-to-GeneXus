import requests
import json
import os
from dotenv import load_dotenv
import click
import gxeai.call_proc_assistant
import xpz.from_json_to_xpz
import yaml

@click.command()
@click.option('--spec_path',  help='a path to a yaml with specifications of procedures.')
@click.option('--output', help='a path to output the xml path ready to import.')
def spec_to_xpz(spec_path, output):
    procs = [] 
    if not os.path.exists(output):
        os.makedirs(output)
    xml_path = os.path.join(output, "import_file.xml")

    with open(spec_path, 'r') as yf:
        data = yaml.safe_load(yf)
        for row in data:
            try:
                name = row.get('name')
                spec = row.get('spec')
                print(f"Processing {name}")
                content = gxeai.call_proc_assistant.call_proc_assistant(name, spec)
                #save program
                program_path = os.path.join(output, name)
                with open(program_path, 'w', encoding='utf-8') as f:
                    f.write(content["Parts"]["Source"])

                procs.append(content)
            except Exception as e:
                print(f"Error: {e}")
    

    #save xpz
    xml_string = xpz.from_json_to_xpz.json_to_xml({'Procedures' : procs})
    with open(xml_path, "w") as file:
        file.write(xml_string)

if __name__ == "__main__":
    spec_to_xpz()
