def es_poden_repartir(persones, galletes):
    # Càlculs....
    return False # True o False

print(__name__)

if __name__ == "__main__":
    persones = int(input())
    galletes = int(input())

    if es_poden_repartir(persones, galletes):
        print("Let's eat!")
    else:
        print("Let's fight!")