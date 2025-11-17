def read_words():
    words = []
    w = input("Paraula: ")
    while w: # Si w is None or '' => False
        words.append(w)
        w = input("Paraula: ")
    return words


def group_by_initial(words):
    groups = {}
    for w in words:
        w = w.lower()
        inicial = w[0]

        # Opció 1: cada cas per separat
        # if inicial not in groups:
        #     groups[inicial] = [w]
        # else:
        #     groups[inicial].append(w)

        # Opció 2: afegir la llista buida si no existex
        if inicial not in groups:
            groups[inicial] = []
        groups[inicial].append(w)

    return groups

if __name__ == "__main__":
    words = read_words()
    groups = group_by_initial(words)
    print(groups)
