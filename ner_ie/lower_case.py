def lower_case(raw_sents):
    """Lowercases raw sentences.

    Args:
        A list of strings containing the raw sentences.

    Returns:
        A list of strings containing the lowercased sentences.
    """

    return [sent.lower() for sent in raw_sents]
