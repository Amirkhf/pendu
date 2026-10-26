from word import random_word
from display import print_start_game
from game import game


def main() -> int:
    """Lance une partie de pendu."""
    try:
        word = random_word()
        print_start_game(word)
        game(word)
    except (EOFError, KeyboardInterrupt):
        print("\nPartie arrêtée.")
        return 1
    return 0


if __name__ == "__main__":
    main()
