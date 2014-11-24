def prepare(sents, mentions):
    """Adds each entity mention to its corresponding sentence.

    Args:
        sents: A list of Sentence objects containing the sentences from a file.
        mentions: A list of Element objects containing the entity mentions.
    """
    for mention, entity_type in mentions:
        begin = int(mention.attrib['offset'])
        end = begin + int(mention.attrib['length']) - 1
        for sent in sents:
            if begin >= sent.get_begin() and end <= sent.get_end():
                sent.add_mention(mention, entity_type)
                break
