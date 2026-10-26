def check_if_is_valid(caractere) -> bool:
    """Vérifie que la saisie est une seule lettre."""
    return len(caractere) == 1 and caractere.isalpha()
