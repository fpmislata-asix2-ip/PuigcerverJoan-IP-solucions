import json

def process_group_line(line, user_group_dict):
    #   (0)    (1)   (2)      (3)
    # group:password:GID:user1,user2,...
    parts = line.split(":")
    group = parts[0]
    users = parts[3].split(",")

    for u in users:
        # Evitem afegir usuaris buits
        if not u:
            continue

        # Si l'usuari no està al diccionari, l'inicialitzem amb una llista buida
        if u not in user_group_dict:
            user_group_dict[u] = []

        # Afegim el grup a la llista d'aquest usuari
        user_group_dict[u].append(group)


if __name__ == "__main__":
    user_group_dict = {}

    line = input()
    while line != "":
        process_group_line(line, user_group_dict)
        line = input()

    # Utilitzem json.dumps() per mostrar el diccionari en format JSON
    print(json.dumps(user_group_dict, indent=4))