from nltk import data


def segment_sentence(text):
    """Segments raw text into sentences

    Args:
        text: A string containing the raw text.

    Returns:
        A list of sentences.
    """

    sent_segmenter = data.load('tokenizers/punkt/english.pickle')
    return sent_segmenter.tokenize(text)
