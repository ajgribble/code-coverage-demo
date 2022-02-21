from json import load
import re


def _split_line(text: str):
    """
    Private utility function used to split text on new lines and spaces
    """
    return re.split("[\n ]", text.replace(".", "").replace(",", ""))


def text(fp):
    """
    Parse file as raw, unformatted text into a list of words
    """
    result = list()

    with open(fp, "r") as f:
        result = _split_line(f.read().lower())

    return result


def json(fp, multiline=False):
    """
    Parse structured JSON into a dict of word lists
    """
    result = dict()

    with open(fp, "r") as f:
        j = load(f)
        for poem_name, lines in j.items():
            # Each poem name maps to a list of lines
            if multiline:
                result[poem_name] = list()
                for line in lines:
                    result[poem_name].extend(_split_line(line.lower()))
            # Each poem name maps to the poem string
            else:
                result[poem_name] = _split_line(lines.lower())

    return result
