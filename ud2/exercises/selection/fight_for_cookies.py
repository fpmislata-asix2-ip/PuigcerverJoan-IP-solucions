def es_poden_repartir(persones, galletes):
    return galletes % persones == 0 # True o False

if __name__ == "__main__":
    persones = int(input())
    galletes = int(input())

    if es_poden_repartir(persones, galletes):
        print("Let's eat!")
    else:
        print("Let's fight!")