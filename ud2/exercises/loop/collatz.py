def collatz(n):
    if n % 2 == 0:
        return n // 2
    else:
        return n*3 + 1

if __name__ == "__main__":
    n = int(input())

    if n <= 0:
        print("ERROR: Has d'introduir un nombre positiu")
        exit(-1)

    print(f"n0: {n}")

    count = 0
    while n != 1:
        n = collatz(n)
        count += 1
        print(f"n{count}: {n}")
    print("Passos:", count)
        