import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../lib'))
from mitie import *

def ner(sents):
    """Does named entity recognition on lowercased sentences.

    Args:
        A list of lowercased sentence strings.

    """

    for sent in sents:
        tokens = tokenize(sent)
        print tokens
