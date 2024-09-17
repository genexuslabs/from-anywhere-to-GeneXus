import re
import uuid
def parse_procedure(gx_string, name):
    # Regular expression to match the procedure name and content
    match = re.search(r'Procedure\s+(\w+)\s*{(.*)}', gx_string, re.DOTALL)
    dict = {} 
    if match:
        dict['name'] = match.group(1).strip()
        dict['guid'] = custom_uuid(dict['name'])
        content = match.group(2).strip()
        sections = parse_sections(content)
        sections["Variables"] = parse_variables((sections["Variables"]))
        dict["Parts"] = sections 
        if name:
            dict['name'] = sanitize_name(name)
    return dict

def parse_sections(input_string):
    sections = {}
    
    # Regular expression to find sections and their content
    section_pattern = re.compile(r'#(\w+)\s*(.*?)\s*#(?:End|)', re.DOTALL)

    # Find all sections
    matches = section_pattern.findall(input_string)
    
    for name, content in matches:
        sections[name] = content.strip()
    
    # Remove matched sections from the original string to find "Source" content
    cleaned_string = section_pattern.sub('', input_string).strip()

    if cleaned_string:
        sections['Source'] = cleaned_string.strip()
    
    return sections 

def parse_variables(input_string):
    # Regular expression to match the main names and their attributes
    item_pattern = re.compile(r'\s*(\w+)\s*(\[(.*?)\])?', re.DOTALL)
    attribute_pattern = re.compile(r"(\w+)\s*=\s*'([^']*)'")
    
    items = {}
    
    # Finding all items and their attributes
    matches = item_pattern.findall(input_string)
    
    for name, _, attributes in matches:
        attr_list = {}
        
        if attributes:
            # Find all attribute name-value pairs within the brackets
            attr_matches = attribute_pattern.findall(attributes)
            attr_list = {attr_name: attr_value for attr_name, attr_value in attr_matches}
        
        # Append the name and its attribute list to the result
        attr_list['Name'] = name
        clean_variable_datatype(attr_list)        
        items[name] = attr_list
    
    return items

def clean_variable_datatype(dict):
    # Regular expression to capture the type and number
    if 'DataType' in dict:
        input_string = dict['DataType']
        dict.pop('DataType')
    else:
        input_string = "Numeric(11,1)"
    # Split the string at the parentheses
    if '(' in input_string:
        data_type, number = input_string.split('(')
        # Remove the closing parenthesis and any extra spaces
        number = number.rstrip(')')
        dict['ATTCUSTOMTYPE'] = 'bas:'+data_type
        dict['Length'] = number
        dict['AttMaxLen'] = number
    else:
        dict['ATTCUSTOMTYPE'] = 'bas:'+input_string
    
def custom_uuid(name):
    # Create a UUID based on the given string using a namespace
    base_uuid = uuid.uuid5(uuid.NAMESPACE_DNS, name)
    
    # Convert the UUID to a string and modify the first 8 characters to "00000000"
    custom_uuid_str = f"00000000{str(base_uuid)[8:]}"
    
    return custom_uuid_str

def sanitize_name(name):
    # Replace invalid characters with an underscore
    sanitized = re.sub(r'[^a-zA-Z0-9_]', '_', name)
    
    # Ensure the name starts with a letter
    if sanitized and not sanitized[0].isalpha():
        sanitized = 'a' + sanitized

    return sanitized
