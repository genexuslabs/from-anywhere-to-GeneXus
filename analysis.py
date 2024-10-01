import requests
import json
import os
from dotenv import load_dotenv
import click
import gxeai.call_assistant
import yaml
from pathlib import Path

analysis_assistant_cobol = "1AnalysisCobol"
analysis_assistant_PLI = "1AnalysisPLI"
analysis_assistant_Generic = "1AnalysisGeneric"

def choose_assistant(lang):
    l = lang.lower()
    if l == "pli":
        return analysis_assistant_PLI
    elif l == "cobol":
        return analysis_assistant_cobol
    else:
        return analysis_assistant_Generic

def read_file(read_file_path):
    print(f"Reading {read_file_path}")
    path = Path(read_file_path)
    name = path.name
    try:
        with open(read_file_path, 'r') as read_file:
            content = read_file.read()
            print(f"content {content}")
            return name, content
    except Exception as e:
        print(f"Error reading file {path}: {e}")

def analyze_content(assistant, name, content):
    print(f"Analyzing {name}")
    try:
        spec = gxeai.call_assistant.call_assistant(assistant, name, content)
        return spec
    except Exception as e:
        print(f"Error analyzing file {name}: {e}")

def write_file(file_path, content):
    print(f"Writing {file_path}")
    try:
        with open(file_path, 'w') as file:
            file.write(content)
    except Exception as e:
        print(f"Error writing file {name}: {e}")


def analyze_repo_rec(repository, analysis_directory, assistant):
    if not os.path.exists(analysis_directory):
        os.makedirs(analysis_directory)

    if repository.is_dir():
        for read_file_path in repository.iterdir():
            print(f"Processsing {read_file_path}")
            if read_file_path.is_file():
                name, content = read_file(read_file_path)
                print("Going to analyze")
                analysis = analyze_content(assistant, name, content)
                write_file_path = os.path.join(analysis_directory, name)
                write_file(write_file_path, content)
            else:
                new_analysis_dir = os.path.join(analysis_directory, name)
                analyze_repo_rec(str(read_file_path), str(new_analysis_dir), assistant)
                #analyze_repo(repository=read_file_path, analysis=new_analysis_dir, lang=lang)
    else:
        print(f"{folder_path} is not a valid directory")

@click.command()
@click.option('--repository', help='a directory with the programs to specify')
@click.option('--analysis', "analysis_directory", help='the output directory')
@click.option('--lang',  help='the main lang of the directory', default='generic')
def analyze_repo(repository, analysis_directory, lang):
    if not os.path.exists(analysis_directory):
        os.makedirs(analysis_directory)

    assistant = choose_assistant(lang)

    repository_folder = Path(repository)
    analysis_folder = Path(repository)
    analyze_repo_rec(repository_folder, analysis_folder, assistant)

if __name__ == "__main__":
    analyze_repo()
