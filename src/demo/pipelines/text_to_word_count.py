from demo.stages import Reduce, Map, Parse

stop_words = ["a", "the", "is"]


def _is_stop_word(word):
    """Private method for verifying whether or not a word is considered a stop word"""
    return word in stop_words


def run(file_path, filter_stop_words=False):
    """
    Create a dict of word counts from a raw text file

        Parameters:
            file_path (str): Path on disk to the text file to parse
            filter_stop_words (bool): Flag, that when True, filters out known stop words (defaults to False)
    """
    # Parse words from text
    words = Parse.text(file_path)

    if filter_stop_words:
        words = filter(lambda w: not _is_stop_word(w))

    word_tuples = Map.to_count(words)
    result = Reduce.sum(word_tuples)

    return result
