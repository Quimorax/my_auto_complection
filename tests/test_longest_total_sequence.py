import pytest

from main import find_longest_total_sequence


def test_with_small_words():
    words = ('how', 'wow')
    assert find_longest_total_sequence(*words) == 2


def test_middle_len_words():
    words = ('accurate', 'accountant')
    assert find_longest_total_sequence(*words) == 7


def test_biggest_words():
    words = ('prescription', 'psychological')
    assert find_longest_total_sequence(*words) == 4


if __name__ == '__main__':
    pytest.main()
