from nltk import data
from ner_ie.sentence import Sentence


class SentenceExtractor():
    """A class for extracting sentences from raw files.
    """

    def __init__(self):
        self._segmenter = data.load('tokenizers/punkt/english.pickle')

    def get_text(self, raw_file):
        """Gets text and offsets from a raw file.

        Args:
            raw_file: A absolute path of a raw file.

        Returns:
            text: A string storing the extracted text.
            offset_list: Offset of each character in the extracted text.
        """
        start_flag = ['TEXT:']
        section_flag = ['UNCLAS', '(MORE)']
        end_flag = ['(ENDALL)']

        started = False
        text = ''
        offset_list = []
        curr_pos = 0
        for ori_line in open(raw_file, 'r'):
            prev_pos = curr_pos
            curr_pos += len(ori_line)
            line = ori_line.rstrip()
            if not started:
                if line in start_flag:
                    started = True
            else:
                if line in start_flag:
                    continue
                elif line in section_flag:
                    started = False
                elif line in end_flag:
                    break
                else:
                    offset_list.extend(range(prev_pos, prev_pos+len(line)+1))
                    text += (line + ' ')
        return (text, offset_list)

    def get_sentences(self, raw_file):
        """Constructs Sentence objects from a raw file.

        Args:
            raw_file: A absolute path of a raw file.

        Returns:
            sents: A list of Sentence objects generated from the raw file.
        """
        (text, offset_list) = self.get_text(raw_file)
        sent_texts = self._segmenter.tokenize(text)

        curr_pos = 0
        sents = []
        for sent_text in sent_texts:
            begin = text.find(sent_text, curr_pos)
            end = begin + len(sent_text)
            curr_pos = end
            sents.append(Sentence(sent_text, offset_list[begin:end]))
        return sents
