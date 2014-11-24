import xml.etree.ElementTree as ET


def read_entity(anno_file):
    """Reads annotated entities from an annotated file.

    Args:
        anno_file: A string storing the absolute path of an annotated file.

    Returns:
        A list of Element objects containing the entity_mention elements.
    """
    tree = ET.parse(anno_file)
    root = tree.getroot()
    parent_dict = {child:parent for parent in tree.iter() for child in parent}
    return [(mention, parent_dict[mention].attrib['type'])
           for mention in root.iter('entity_mention')]
