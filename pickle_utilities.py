import pickle


def save_dict(filename: str, words: dict) -> None:
    """Save dictionary with pickle."""
    with open(filename, 'wb') as file:
        pickle.dump(words, file)


def get_dict(filename: str) -> dict:
    """Get dictionary with pickle."""
    with open(filename, 'rb') as file:
        words = pickle.load(file)
    return words
