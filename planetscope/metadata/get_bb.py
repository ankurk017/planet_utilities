"""
check_xmlfile_type function
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
        The following examples illustrate how to use the `check_xmlfile_type` function:

        1. Input is a string representing the file path:
        
        .. code-block:: python
        
            xml_file_path = "path/to/your/xml_file.xml"
            parsed_xml = check_xmlfile_type(xml_file_path)

        2. Input is an existing XML Document object:

        .. code-block:: python

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




