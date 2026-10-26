def print_start_game(word):
    """Affiche le mot caché au début de la partie."""
    i = 0
    line = ""
    while i < len(word):
        if (i == 0):
            line += "Mot : "
        line += "- "
        i += 1
    print(line)
