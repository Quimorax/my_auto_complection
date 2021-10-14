"""Auto-complete with dynamic program method."""

__version__ = '1.0.0'

import argparse
import pickle


def create_parser() -> argparse.ArgumentParser:
    """Create parser that processes command-line parameters."""
    parser = argparse.ArgumentParser(
        prog='auto-complete',
        description="""Auto-complete performed using dynamic program method with command line support.""",
        epilog=f"""auto-complete {__version__} - (C) October 2021 Quimorax"""
    )
    parser.add_argument('-w', '--word', help='Contain word that will be send to main function.')
    return parser


def main(word: str) -> str:
    """Main function that start project. Iterate dictionary with most common words
    and finding most similar words. Dictionary is small, only 3000 words, so the
    function fully avoids it for maximum accuracy, but the productivity dropped a little.

    Raises:
        ValueError: If words contain not only chars.

    """
    if not word.isalpha():
        raise ValueError('Word must contain only chars')
    entry_limit = 0.70
    words = get_dict(r'C:\Users\User\PycharmProjects\my_auto_complection\words.pickle')
    for compare_word in words:
        longest_total_sequence = find_longest_total_sequence(word, compare_word)
        similarity = longest_total_sequence / max((len(word), len(compare_word)))
        if similarity >= entry_limit:
            words[compare_word] = similarity
    words = sorted(words.items(), key=lambda x: x[1], reverse=True)
    most_similar_word, similarity = words[0][0], words[0][1]
    if similarity < entry_limit:
        return f'No one word {word!r}'
    if similarity == 1:  # 100 %
        return f'{word!r} is correct word'
    return f'Maybe you mean {most_similar_word!r} ({similarity:.2%})?'


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


def save_dict(filename: str, words: dict) -> None:
    """Save dictionary with pickle."""
    with open(filename, 'wb') as file:
        pickle.dump(words, file)


def get_dict(filename: str) -> dict:
    """Get dictionary with pickle."""
    with open(filename, 'rb') as file:
        words = pickle.load(file)
    return words


if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args()
    if namespace.word is None:
        word = input('Enter some word: ')
    else:
        word = namespace.word
    print(main(word))
