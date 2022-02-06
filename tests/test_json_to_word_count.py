from demo.pipelines.json_to_word_count import run as run_json_to_word_count

base_path = "tests/sample_data/json"


def test_processing_basic_json():
    result = run_json_to_word_count(f"{base_path}/poems.json")

    assert result["missing"]["hunted"] == 2
    assert result["missing"]["my"] == 4
    assert result["missing"]["them"] == 2

    assert result["tinkle_tinkle_little_car"]["little"] == 2
    assert result["tinkle_tinkle_little_car"]["tinkle"] == 4
    assert result["tinkle_tinkle_little_car"]["you"] == 3


def test_processing_multiline_json():
    result = run_json_to_word_count(f"{base_path}/poems_multiline.json", multiline=True)

    assert result["missing"]["hunted"] == 2
    assert result["missing"]["my"] == 4
    assert result["missing"]["them"] == 2

    assert result["tinkle_tinkle_little_car"]["little"] == 2
    assert result["tinkle_tinkle_little_car"]["tinkle"] == 4
    assert result["tinkle_tinkle_little_car"]["you"] == 3
