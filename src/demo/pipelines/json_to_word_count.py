from demo.stages import Reduce, Map, Parse


def run(file_path, **kwargs):
    # Parse words from json
    poems = Parse.json(file_path, *kwargs)

    result = dict()
    for poem_name, poem in poems.items():
        word_tuples = Map.to_count(poem)
        result[poem_name] = Reduce.sum(word_tuples)

    return result
