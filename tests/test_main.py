import pytest

from main import main, find_longest_total_sequence


def test_small_words():
    user_word, word_user_mean = 'acual', 'actual'
    similarity = find_longest_total_sequence(user_word, word_user_mean) / len(word_user_mean)
    assert main(user_word) == f'Maybe you mean {word_user_mean!r} ({similarity:.2%})?'


def test_middle_len_words():
    user_word, word_user_mean = 'respomse', 'response'
    similarity = find_longest_total_sequence(user_word, word_user_mean) / len(word_user_mean)
    assert main(user_word) == f'Maybe you mean {word_user_mean!r} ({similarity:.2%})?'


def test_longest_words():
    user_word, word_user_mean = 'somisticated', 'sophisticated'
    similarity = find_longest_total_sequence(user_word, word_user_mean) / len(word_user_mean)
    assert main(user_word) == f'Maybe you mean {word_user_mean!r} ({similarity:.2%})?'


if __name__ == '__main__':
    pytest.main()
