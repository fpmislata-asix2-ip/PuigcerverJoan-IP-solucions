def comptar_enrere(n):
    result = ""
    for i in range(n, 0, -1):
        result += str(i)
    return result


if __name__ == "__main__":
    n = int(input())
    print(comptar_enrere(n))

