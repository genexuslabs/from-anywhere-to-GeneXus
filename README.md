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

### 4. Creating a spec file from a program of your choice

#todo

### 4. Creating a GeneXus procedure in xpz file from a spec 
After setting up the environment, you can run `script1.py` by providing a file path as an argument. Use the following command:

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
Include licensing information here if applicable.
