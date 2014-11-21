START_FLAG = ['TEXT:']
END_FLAG = ['UNCLAS', '(MORE)', '(ENDALL)']


def extract_text(raw_file):
    started = False
    text = ''
    for line in open(raw_file, 'r'):
        line = line.strip()
        if not started:
            if line in START_FLAG:
                started = True
        else:
            if line in START_FLAG:
                continue
            elif line in END_FLAG:
                started = False
            else:
                text += (line + ' ')
    print text
    print
