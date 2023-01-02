"""
Module containing a third class.
"""

import numpy as np
from xml.dom import minidom
import pandas as pd

def check_xmlfile_type(xml_filename):
    """_summary_

    Args:
        xml_filename (_type_): _description_

    Returns:
        _type_: _description_
    """
    
    if type(xml_filename).__name__ == "Document":
        xml_filename = xml_filename
    elif type(xml_filename).__name__ == "str":
        xml_filename = minidom.parse(xml_filename)
    else:
        IOError("Wrong type of input data")
    return xml_filename


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

    def extract_element(corner):
        return [
            location[0]
            .getElementsByTagName("ps:" + corner)[0]
            .getElementsByTagName("ps:" + loc)[0]
            .firstChild.data
            for loc in np.array(("longitude", "latitude"))
        ]

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