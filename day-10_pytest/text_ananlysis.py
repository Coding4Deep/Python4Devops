from typing import TypedDict

class TextAnalysisResult(TypedDict):
    char_count: int
    word_count: int
    line_count: int

def analyze_text(text: str) -> TextAnalysisResult:
    lines = text.splitlines()
    words = text.split()
    
    word_len_sum = sum(len(word) for word in words)
    average_word_length = (
        word_len_sum / len(words) if words else 0
    )

    unique_words = set(word.lower() for word in words)
    return TextAnalysisResult(
        char_count=len(text),
        word_count=len(words),
        line_count=len(lines),
        unique_word_count=len(unique_words),
        average_word_length=average_word_length,
    )

# print(len(("this line 01\nline 02").splitlines()))