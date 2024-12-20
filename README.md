# From Anywhere To GeneXus

## Description
Convert any code into a GeneXus procedure. Get the code of your choice, generate a spec, then use that spec to generate a GeneXus procedure inside an xpz file.

## Prerequisites
Ensure you have Python 3.x installed on your system. You can download it from [python.org](https://www.python.org/downloads/)

You will need a token to the GXEAI project. Write jmichelini at genexus for one.

## Setup

### 1. Clone the rep
 
```bash
git clone  https://github.com/genexuslabs/from-anywhere-to-GeneXus
cd from-anywhere-to-GeneXus
```

### 2. Create a Virtual Environment
To create a virtual environment and activate it, run the following commands:

```bash
# Create the virtual environment
python3 -m venv venv

# Activate the virtual environment (Linux/MacOS)
source venv/bin/activate

# Activate the virtual environment (Windows)
venv\Scripts\activate
```

### 3. Install Dependencies
Once the virtual environment is activated, install the required packages using `pip`:

```bash
pip install -r requirements.txt
```

### 4. Create a .env file
```
BASE_URL=https://api.qa.saia.ai/chat
ASSISTANT_NAME=ProcedureBaseSyntax
REVISION=18
SAIA_PROJECT_APITOKEN=<YOUR-GXEAI-ASSISTANT-TOKEN>
```

### 5. Creating a spec file from a program of your choice

```bash

python anything_to_spec.py --programs_directory ./tests/cobol/test1/ --spec_path ./outputs/spec1.yml
```

### 6. Creating a GeneXus procedure in xpz file from a spec 
After setting up the environment, you can run `script1.py` by providing a file path as an argument. Use the following command:

```bash

python spec_to_xpz.py --spec_path ./outputs/spec1.yml --output ./outputs/test1
```
You can import outputs/import_file.xml directly into GeneXus.

or

```
```bash
python spec_to_xpz.py --spec_path ./tests/testSet1.yaml --xml_path ./testSet1.xml
```
You can import the testSet1.xml file directly into GeneXus.

## Deactivating the Virtual Environment
When you're done, you can deactivate the virtual environment with:

```bash
deactivate
```

## License
```
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
