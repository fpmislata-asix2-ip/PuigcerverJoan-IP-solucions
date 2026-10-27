def read_list():
    n = int(input("Introdueix el nombre d'elements: "))

    l = []
    for i in range(n):
        e = int(input(f"[{i}]: "))
        l.append(e)

    return l


def min(l):
    if len(l) == 0:
        return None

    e_min = l[0]
    for i in range(1, len(l)):
        if l[i] < e_min:
            e_min = l[i]
    return e_min


def max(l):
    if len(l) == 0:
        return None

    e_max = l[0]
    for i in range(1, len(l)):
        if l[i] > e_max:
            e_max = l[i]
    return e_max

def sum(l):
    s = 0
    for e in l:
        s += e
    return s

if __name__ == "__main__":
    my_list = read_list()
    print("La llista és:", my_list)
    print("Mínim:", min(my_list))
    print("Màxim:", max(my_list))
    print("Suma:", sum(my_list))