from demo.stages import Reduce, Map, Parse


def run(file_path, **kwargs):
    """
    Create a dict of word counts from a structure JSON file in the form of:
    {
        "text_name": "text_content"
    }
    """
    poems = Parse.json(file_path, *kwargs)

    result = dict()
    for poem_name, poem in poems.items():
        word_tuples = Map.to_count(poem)
        result[poem_name] = Reduce.sum(word_tuples)

    return result
