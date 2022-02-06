from demo.pipelines.text_to_word_count import run as run_text_to_word_count

base_path = "tests/sample_data/text"


def test_default_processing_valid_text():
    result = run_text_to_word_count(f"{base_path}/missing_poem.txt")

    assert result["hunted"] == 2
    assert result["my"] == 4
    assert result["them"] == 2


def test_default_processing_alt_text():
    result = run_text_to_word_count(f"{base_path}/tinkle_tinkle_little_car_poem.txt")

    assert result["little"] == 2
    assert result["tinkle"] == 4
    assert result["you"] == 3
