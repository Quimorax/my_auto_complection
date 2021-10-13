"""Auto-complete with dynamic program method."""

__version__ = '1.0.0'

import argparse
from random import shuffle


def create_parser() -> argparse.ArgumentParser:
    """Create parser that processes command-line parameters."""
    parser = argparse.ArgumentParser(
        prog='auto-complete',
        description="""Auto-complete performed using dynamic program method with command line support.""",
        epilog=f"""auto-complete {__version__} - (C) October 2021 Quimorax"""
    )
    parser.add_argument('-w', '--word')
    return parser


def main(word: str) -> str:
    """Main function that start project. Iterate file with most common words and finding most similar words."""
    if not word.isalpha():
        raise ValueError('Word must contain only chars')
    entry_limit = 0.75
    path = r'C:\Users\User\PycharmProjects\my_auto_complection\most_common_words.txt'
    with open(path, 'r') as file:
        lines = list(map(str.strip, file))
        shuffle(lines)  # for non-alphabet iterate
        if word in lines:
            return f'{word!r} is correct word'
        for file_word in lines:
            longest_total_sequence = find_longest_total_sequence(word, file_word)
            similarity = longest_total_sequence / max((len(word), len(file_word)))
            if similarity >= entry_limit:
                return f'Maybe you mean {file_word!r} ({similarity:.2%})?'
    return f'No one word {word!r}'


def find_longest_total_sequence(user_word: str, file_word: str) -> int:
    """Find the longest total sequence with dynamic program method."""
    matrix = [[0 for _ in range(len(user_word))] for _ in range(len(file_word))]
    for i in range(len(file_word)):
        for j in range(len(user_word)):
            if file_word[i] == user_word[j]:
                matrix[i][j] = matrix[i - 1][j - 1] + 1
            else:
                matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])
    return max(similarity for list_ in matrix for similarity in list_)


if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args()
    if namespace.word is None:
        word = input('Enter some word: ')
    else:
        word = namespace.word
    print(main(word))
