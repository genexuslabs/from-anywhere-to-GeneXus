import json
import os
import xml.etree.ElementTree as ET
from string import Template
import xpz.Objects.Procedure.from_json

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
    
    for key, value in json_obj.items():
        property_element = ET.SubElement(properties, "Property")
        
        name_element = ET.SubElement(property_element, "Name")
        name_element.text = key
        
        value_element = ET.SubElement(property_element, "Value")
        value_element.text = str(value)
    
    return ET.tostring(properties, encoding='unicode')

def json_to_xml(data):


    objects_list = []
    for proc in data["Procedures"]:
        objects_list.append(xpz.Objects.Procedure.from_json.json_to_xml(proc))

    # Load the root template from file
    root_template = load_template("KB")
    root_xml_str = root_template.substitute(objects=" ".join(objects_list))

    # Parse the XML string into an ElementTree object (optional)
    root_xml = ET.ElementTree(ET.fromstring(root_xml_str))

    # Pretty print the XML (optional)
    ET.indent(root_xml, space="  ")

    # Convert the ElementTree to a string for display
    final_xml_str = ET.tostring(root_xml.getroot(), encoding='unicode')

    return final_xml_str
