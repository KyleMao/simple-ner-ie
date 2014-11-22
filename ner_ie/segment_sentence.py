from nltk import data


def segment_sentence(text):
    sent_segmenter = data.load('tokenizers/punkt/english.pickle')
    sents = sent_segmenter.tokenize(text)
    return sents
