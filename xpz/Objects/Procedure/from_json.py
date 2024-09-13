import json
import os
import xml.etree.ElementTree as ET
from string import Template

def load_file(file_path):
    """Utility function to load content from a file."""
    with open(file_path, 'r') as file:
        return file.read()

def load_template(part_name):
    """Loads the template for a given part name from the script's directory."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    template_path = os.path.join(script_dir, f"{part_name}.xml")
    return Template(load_file(template_path))

def json_to_xml_properties(json_obj):
    properties = ET.Element("Properties")
    
    for varname, dict in json_obj.items():
        var_element = ET.SubElement(properties, "Variables")
        var_element.set("Name", varname)
        for key, value in dict:
            property_element = ET.SubElement(var_elem, "Property")
            
            name_element = ET.SubElement(property_element, "Name")
            name_element.text = key
            
            value_element = ET.SubElement(property_element, "Value")
            value_element.text = str(value)
    
    return ET.tostring(properties, encoding='unicode')

def json_to_xml(data):


    # Load the rules template from file
    rules = ""
    if "Parts" in data and "Rules" in data["Parts"]:
        rules = data['Parts']['Rules']
    rules_template = load_template("Rules")
    rules_xml_str = rules_template.substitute(rules=rules)

    # Load the source template from file
    source = ""
    if "Parts" in data and "Source" in data["Parts"]:
        source = data['Parts']['Source']
    source_template = load_template("Source")
    source_xml_str = source_template.substitute(source=source)

    # Load the source template from file
    variables = "<Properties></Properties>"
    if "Parts" in data and "Variables" in data["Parts"]:
        variables = json_to_xml_properties(data['Parts']['Variables'])
    variables_template = load_template("Variables")
    variables_xml_str = variables_template.substitute(variables=variables)

    # Load the root template from file
    root_template = load_template("Object")
    root_xml_str = root_template.substitute(name=data['name'],
                                            description=data['description'],
                                            guid=data['guid'],
                                            rules_part=rules_xml_str,
                                            source_part=source_xml_str,
                                            variables_part=variables_xml_str)

    # Parse the XML string into an ElementTree object (optional)
    root_xml = ET.ElementTree(ET.fromstring(root_xml_str))

    # Pretty print the XML (optional)
    ET.indent(root_xml, space="  ")

    # Convert the ElementTree to a string for display
    final_xml_str = ET.tostring(root_xml.getroot(), encoding='unicode')

    return final_xml_str
