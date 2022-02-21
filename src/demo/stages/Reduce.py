def sum(word_tuples):
    """
    Build a dict of word counts from a list of tuples
    """
    result = dict()

    for word, count in word_tuples:
        if word in result:
            result[word] += count
        else:
            result[word] = count

    return result
