import pytest
from demo.pipelines.text_to_word_count import (
    _is_stop_word,
    run as run_text_to_word_count,
)

base_path = "tests/sample_data/text"
json_path = "tests/sample_data/json"


def test_default_processing_valid_text():
    result = run_text_to_word_count(f"{base_path}/missing_poem.txt")

    assert result["hunted"] == 2
    assert result["in"] == 2
    assert result["my"] == 4
    assert result["them"] == 2


def test_default_processing_alt_text():
    result = run_text_to_word_count(f"{base_path}/tinkle_tinkle_little_car_poem.txt")

    assert result["little"] == 2
    assert result["tinkle"] == 4
    assert result["you"] == 3


def test_default_processing_valid_text_sans_stop_words():
    result = run_text_to_word_count(
        f"{base_path}/missing_poem.txt", filter_stop_words=True
    )

    assert result["hunted"] == 2
    assert result["my"] == 4
    assert result["them"] == 2
    assert "in" not in result


def test_is_stop_word():
    """
    This test is superfluous and may result in false positives that a block of code is actually run
    """
    assert _is_stop_word("the") is True
    assert _is_stop_word("is") is True
    assert _is_stop_word("something") is False


def test_file_extension_exceptions():
    with pytest.raises(ValueError):
        run_text_to_word_count(f"{json_path}/poems.json")
