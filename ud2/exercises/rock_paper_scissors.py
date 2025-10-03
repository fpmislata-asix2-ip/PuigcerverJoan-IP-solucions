def calculate_winner(j1, j2):
    """
    Calcula el guanyador del joc pedra, paper, tisores.

    Args:
        j1 (str): Elecció del jugador 1 ("pedra", "paper" o "tisores").
        j2 (str): Elecció del jugador 2 ("pedra", "paper" o "tisores").

    Returns:
        int: -1 is la jugada és invàlida, 0 si hi ha empat, 1 si guanya el jugador 1, 2 si guanya el jugador 2.
    """

    if j1 == j2:
        return 0
    elif (j1 == "pedra" and j2 == "tisores") \
            or (j1 == "paper" and j2 == "pedra") \
            or (j1 == "tisores" and j2 == "paper"):
        return 1
    else:
        return 2


def print_winner(j1, j2, winner):
    # Mostrar missatges
    jugada_guanyadora = j1 if winner == 1 else j2
    if winner == -1:
        print("La jugada és invàlida.")
    elif winner == 0:
        print(f"Els dos jugadors han empatat amb '{jugada_guanyadora}'.")
    else:
        print(f"Guanya el jugador {winner} amb '{jugada_guanyadora}'.")


j1 = input()
j2 = input()

winner = calculate_winner(j1, j2)
print_winner(j1, j2, winner)