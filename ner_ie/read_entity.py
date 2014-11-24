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
    return [entity_mention for entity_mention in root.iter('entity_mention')]
