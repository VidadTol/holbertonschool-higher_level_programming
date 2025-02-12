#!/usr/bin/env python3
"""
This module defines a function serialize_to_xml that serializes a dictionary to an XML file.
"""


import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a dictionary to an XML file.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        item = ET.SubElement(root, key)
        item.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)

def deserialize_from_xml(filename):
    """
    Deserialize an XML file to a dictionary.
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    dict = {}
    for item in root:
        dict[item.tag] = item.text
    return dict
