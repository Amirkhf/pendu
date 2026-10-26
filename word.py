import random


def random_word() -> str:
    """Choisit un mot au hasard dans le dictionnaire."""
    ft_dict = {
        "1": "pandas",
        "2": "numpy",
    }
    ramdo_value = random.randint(0, len(ft_dict) - 1)
    for i, c in enumerate(ft_dict):
        if (i == ramdo_value):
            word = ft_dict[c]
    return word
