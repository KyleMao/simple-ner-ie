class Sentence():
    """A class for sentence metadata.

    Attributes:
        text: A string of the sentence text.
        offset_range: A xrange object storing the offset range of the sentence.
    """

    def __init__(self, text, offset_list):
        self.text = text
        self.offset_list = offset_list
