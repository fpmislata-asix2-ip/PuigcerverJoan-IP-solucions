dia = input("Introdueix un dia de la setmana: ").lower()

match dia:
    case "dilluns":
        print("Inici de la setmana.")
    case "dimarts":
        print("Segon dia de la setmana.")
    case "dimecres":
        print("Mitjà de la setmana.")
    case "dijous":
        print("Quasi divendres.")
    case "divendres":
        print("Final de la setmana laboral.")
    case "dissabte" | "diumenge":
        print("Cap de setmana!")
    case _:
        print("No és un dia vàlid.")