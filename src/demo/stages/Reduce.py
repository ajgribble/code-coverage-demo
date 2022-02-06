def sum(word_tuples):
    result = dict()

    for word, count in word_tuples:
        if word in result:
            result[word] += count
        else:
            result[word] = count

    return result
