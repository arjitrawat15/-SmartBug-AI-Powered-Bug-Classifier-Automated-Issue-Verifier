def test_clean_text():
    from utils.preprocess import clean_text
    assert clean_text("   Hello, WORLD! ") == "hello world"
