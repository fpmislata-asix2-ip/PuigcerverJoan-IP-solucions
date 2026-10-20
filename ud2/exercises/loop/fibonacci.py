if __name__ == "__main__":
    n = int(input())

    f0 = 0
    f1 = 1

    if n >= 1:
        print(f0)

    if n >= 2:
        print(f1)

    for i in range(n - 2):
        fn = f0 + f1
        f0 = f1
        f1 = fn
        print(fn)
