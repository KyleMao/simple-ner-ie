from nltk import data


class SentenceExtractor():
    """ A class for extracting sentences from raw files.
    """

    def __init__(self):
        self.segmenter = data.load('tokenizers/punkt/english.pickle')

    def get_text(self, raw_file):
        start_flag = ['TEXT:']
        section_flag = ['UNCLAS', '(MORE)']
        end_flag = ['(ENDALL)']

        started = False
        text = ''
        ori_indices = []
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
                    ori_indices.extend(range(prev_pos, prev_pos+len(line)+1))
                    text += (line + ' ')
        return (text, ori_indices)

    def get_sentences(self, raw_file):
        (text, ori_indices) = self.get_text(raw_file)
        sent_texts = self.segmenter.tokenize(text)
        print ori_indices

        curr_pos = 0
        for sent_text in sent_texts:
            begin = text.find(sent_text, curr_pos)
            end = begin + len(sent_text) - 1
