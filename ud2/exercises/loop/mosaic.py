if __name__ == "__main__":
    n = int(input())

    for i in range(n):
        for j in range(n):
            c = ""
            #if (i + j) % 2 == 0:
            #    c = "A"
            #else:
            #    c = "B"

            if i == j:
                c = "X"
            elif i > j:
                c = "D"
            else:
                c = "U"

            print(f"{c}", end=" ")
        print()