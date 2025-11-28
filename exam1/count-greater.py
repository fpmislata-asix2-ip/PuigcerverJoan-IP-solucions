def read_list():
    text = input()
    list_numbers = []
    for n in text.split():
        list_numbers.append(int(n))
    return list_numbers


def count_greater(list_numbers, ref):
    list_greater = []
    for n in list_numbers:
        if n > ref:
            list_greater.append(n)
    return list_greater


if __name__ == "__main__":
    list_numbers = read_list()
    referencia = int(input())

    count = count_greater(list_numbers, referencia)
    print(len(count))
    print(count)