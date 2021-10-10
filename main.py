"""Auto complete with dynamic program method."""

__version__ = '1.0.0'

from string import digits


def main(word: str) -> str:
    """Main function that start project. Iterate file with most common words and finding most similar words."""
    if set(digits) & set(word):
        raise TypeError('Word must contain only chars, no numbers')
    entry_limit = 0.75
    with open('most_common_words.txt', 'r') as file:
        lines = tuple(map(str.strip, file))
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
    word = input('Enter some word: ')
    print(main(word))
