from text_ananlysis import analyze_text

# x:int=10
# assert x == 10
# assert x == 1

# def test_assertion() -> None:
#     expected_string: str = "HELLO, WORLD!"
#     actual_string: str = ("Hello, World!").upper()
#     assert ( 
#         actual_string == expected_string
#     ), "The actual string does not match the expected string."


def test_word_count() -> None:
    sample_text: str = "Hello, World!\nThis is a test."
    empty_text: str = ""
    assert analyze_text(empty_text)["word_count"] == 0, "Empty text should have 0 words"
    assert analyze_text(sample_text)["word_count"] == 6, "Word count should be 6"

def test_line_count() -> None:
    sample_text: str = "Hello, deepak\nHow are you"
    assert analyze_text(sample_text)["line_count"] == 2, "line should be 2"

def test_unique_word_count() -> None:
    sample_text: str = "hello hello world helloworld world"
    assert analyze_text(sample_text)["unique_word_count"] == 3, "Unique word count should be 3"

    sample_text2: str = "hello Hello HELLO WORLD world"
    assert analyze_text(sample_text2)["unique_word_count"] == 2, "Unique word count should be 4"

    sample_text3: str = ""
    assert analyze_text(sample_text3)["unique_word_count"] == 0, "Unique word count should be 0"

def test_average_word_length() -> None:
    sample_text: str = "hi hello"
    assert analyze_text(sample_text)["average_word_length"] == 3.5, "Average word length should be 3.5"

    sample_text2: str = "a ab abc"
    assert analyze_text(sample_text2)["average_word_length"] == 2.0, "Average word length should be 2.0"

    sample_text3: str = ""
    assert analyze_text(sample_text3)["average_word_length"] == 0, "Average word length should be 0"