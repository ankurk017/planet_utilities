"""
Module containing a third class.
"""

import numpy as np
from xml.dom import minidom
import pandas as pd


def check_xmlfile_type(xml_filename):
    """
    Check the type of input XML file and parse it if necessary.

    This function checks the type of the input `xml_filename` and performs parsing if required.
    It accepts either a `Document` object or a file path to the XML file in string format.

    Args:
        xml_filename (str or xml.dom.minidom.Document): The input XML filename or Document object.

    Returns:
        xml.dom.minidom.Document: The parsed XML Document object.

    Raises:
        IOError: If the input data is of the wrong type.

    Example:
        # Example 1: Input is a string representing the file path
        xml_file_path = "path/to/your/xml_file.xml"
        parsed_xml = check_xmlfile_type(xml_file_path)

        # Example 2: Input is an existing XML Document object
        from xml.dom import minidom
        xml_document = minidom.parseString("<root><element>Value</element></root>")
        parsed_xml = check_xmlfile_type(xml_document)
    """
    if isinstance(xml_filename, minidom.Document):
        # If the input is already an XML Document, no parsing is needed
        xml_parsed = xml_filename
    elif isinstance(xml_filename, str):
        # If the input is a string representing the file path, parse the XML file
        xml_parsed = minidom.parse(xml_filename)
    else:
        # If the input is of the wrong type, raise an error
        raise IOError("Wrong type of input data")
    
    return xml_parsed



def get_coeffs(xml_filename):
    """_summary_

    Args:
        xml_filename (_type_): _description_

    Returns:
        _type_: _description_
    """

    xml_filename = (
        xml_filename
        if type(xml_filename).__name__ == "Document"
        else minidom.parse(xml_filename)
    )
    nodes = xml_filename.getElementsByTagName("ps:bandSpecificMetadata")
    coeffs = {}
    for node in nodes:
        bn = node.getElementsByTagName("ps:bandNumber")[0].firstChild.data
        if bn in ["1", "2", "3", "4"]:
            i = int(bn)
            value = node.getElementsByTagName("ps:reflectanceCoefficient")[
                0
            ].firstChild.data
            coeffs[i] = float(value)
    return coeffs

def extract_element(corner):
        return [
            location[0]
            .getElementsByTagName("ps:" + corner)[0]
            .getElementsByTagName("ps:" + loc)[0]
            .firstChild.data
            for loc in np.array(("longitude", "latitude"))
        ]

def get_location(xml_filename):
    """_summary_

    Args:
        xml_filename (_type_): _description_

    Returns:
        _type_: _description_
    """

    xml_filename = (
        xml_filename
        if type(xml_filename).__name__ == "Document"
        else minidom.parse(xml_filename)
    )
    location = xml_filename.getElementsByTagName("ps:geographicLocation")


    tl = extract_element("topLeft")
    tr = extract_element("topRight")
    bl = extract_element("bottomLeft")
    br = extract_element("bottomRight")
    bounding_boxes = np.array(
        [(float(values[0]), float(values[1]))
         for values in np.array((tl, tr, bl, br))]
    )
    return pd.DataFrame(
        bounding_boxes, columns=["lon", "lat"], index=["TL", "TR", "BL", "BR"]
    )
