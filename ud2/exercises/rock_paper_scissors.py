def calcular_guanyar_rock_paper_scissors(eleccio1, eleccio2):
    """
    @return: 1 si guanya el jugador 1; 2 si guanya el jugador 2; 0 si hi ha empat; -1 si hi ha algun error
    """

    match eleccio1, eleccio2:
        case ("pedra", "pedra") | ("paper", "paper") | ("tisores", "tisores"):
            return 0
        case ("pedra", "tisores") | ("paper", "pedra") | ("tisores", "paper"):
            return 1
        case ("pedra", "paper") | ("paper", "tisores") | ("tisores", "pedra"):
            return 2
        case _:
            return -1

    #if eleccio1 == eleccio2:
    #    return 0
    #elif (eleccio1 == "pedra" and eleccio2 == "tisores") \
    #    or (eleccio1 == "paper" and eleccio2 == "pedra") \
    #    or (eleccio1 == "tisores" and eleccio2 == "paper"):
    #    return 1
    #elif (eleccio1 == "pedra" and eleccio2 == "paper") \
    #    or (eleccio1 == "paper" and eleccio2 == "tisores") \
    #    or (eleccio1 == "tisores" and eleccio2 == "pedra"):
    #    return 2
    #else:
    #    return -1


if __name__ == "__main__":
    eleccio1 = input("Jugador 1 (pedra/paper/tisores): ")
    eleccio2 = input("Jugador 2 (pedra/paper/tisores): ")

    guanyador = calcular_guanyar_rock_paper_scissors(eleccio1, eleccio2)

    if guanyador == 0:
        print(f"Els dos jugadors han empatat amb '{eleccio1}'.")
    elif guanyador == 1:
        print(f"Guanya el jugador 1 amb '{eleccio1}'.")
    elif guanyador == 2:
        print(f"Guanya el jugador 2 amb '{eleccio2}'.")
    else:
        print(f"Error. Les eleccions han de ser 'pedra', 'paper' o 'tisores'")