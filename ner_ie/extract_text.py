def extract_text(raw_file):
    START_FLAG = ['TEXT:']
    SECTION_FLAG = ['UNCLAS', '(MORE)']
    END_FLAG = ['(ENDALL)']

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
            elif line in SECTION_FLAG:
                started = False
            elif line in END_FLAG:
                break
            else:
                text += (line + ' ')
    return text
