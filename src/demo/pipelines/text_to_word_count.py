from demo.stages import Reduce, Map, Parse

stop_words = ["a", "the", "is"]


def _is_stop_word(word):
    return word in stop_words


def run(file_path, filter_stop_words=False):
    # Parse words from text
    words = Parse.text(file_path)

    if filter_stop_words:
        words = filter(lambda w: not _is_stop_word(w))

    word_tuples = Map.to_count(words)
    result = Reduce.sum(word_tuples)

    return result
