from validation import check_if_is_valid


def init_result(word) -> list:
    """Crée une liste de '_' de la même taille que le mot."""
    return ["_"] * len(word)


def game(word):
    """Fait tourner la partie jusqu'à la victoire ou la défaite."""
    result = init_result(word)
    deja_proposees = set()
    vie = 6
    while vie != 0:
        c = input("Lettre ? ").lower()
        if not check_if_is_valid(c):
            print("Tape une seule lettre !")
            continue
        if c in deja_proposees:
            print("Déjà proposée !")
            continue
        deja_proposees.add(c)
        if c in word:
            for i, lettre in enumerate(word):
                if lettre == c:
                    result[i] = c
            print("Bien joué !")
        else:
            vie -= 1
            print(f"Raté ! Vies : {vie}")
        print("Mot : " + " ".join(result))
        if "_" not in result:
            print(f"Gagné ! Le mot était : {word}")
            return
    print(f"Perdu ! Le mot était : {word}")
