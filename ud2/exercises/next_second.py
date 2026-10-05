def is_valid_time(hores, minuts, segons):
    is_valid = True
    if hores < 0 or hores > 23:
        print(f"El valor '{hores}' no és vàlid per a les hores.")
        is_valid = False
    if minuts < 0 or minuts > 59:
        print(f"El valor '{minuts}' no és vàlid per als minuts.")
        is_valid = False
    if segons < 0 or segons > 59:
        print(f"El valor '{segons}' no és vàlid per als segons.")
        is_valid = False
    return is_valid


def sumar_un_segon(hores, minuts, segons):
    segons += 1

    if segons == 60:
        minuts += 1
        segons = 0

    if minuts == 60:
        hores += 1
        minuts = 0

    if hores == 24:
        hores = 0

    return hores, minuts, segons


if __name__ == "__main__":
    hores = int(input())
    minuts = int(input())
    segons = int(input())

    is_valid = is_valid_time(hores, minuts, segons)

    if is_valid:
        hores, minuts, segons = sumar_un_segon(hores, minuts, segons)

        print(f"{hores:02d}:{minuts:02d}:{segons:02d}")