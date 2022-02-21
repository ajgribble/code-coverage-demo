def to_count(words):
    """
    Map a list of words to a list of tuples
    """
    return map(lambda w: (w, 1), words)
