import os.path as opath
from sys import path as spath
PROJECT_ROOT = opath.join(opath.dirname(__file__), '..')
spath.append(opath.join(PROJECT_ROOT, 'lib'))
from mitie import *

def ner(sents):
    """Does named entity recognition on lowercased sentences.

    Args:
        A list of lowercased sentence strings.

    """
    extractor = named_entity_extractor(
        os.path.join(PROJECT_ROOT, 'data/models/ner_model.dat'))

    return [extractor.extract_entities(tokenize(sent)) for sent in sents]
