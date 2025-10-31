def read_list():
    n = int(input("Introdueix el nombre d'elements: "))
    l = []

    for i in range(n):
        e = int(input(f"[{i}]: "))
        l.append(e)

    return l


def min(lst):
    if len(lst) == 0:
        return None

    min_e = lst[0]
    for e in lst:
        if e < min_e:
            min_e = e
    
    return min_e


def max(lst):
    if len(lst) == 0:
        return None

    max_e = lst[0]
    for e in lst:
        if e > max_e:
            max_e = e
    
    return max_e


def sum(lst):
    s = 0
    for e in lst:
        s += e
    return s


if __name__ == '__main__':
    my_list = read_list()
    print("La llista és:", my_list)
    print("Mínim:", min(my_list))
    print("Màxim:", max(my_list))
    print("Suma:", sum(my_list))