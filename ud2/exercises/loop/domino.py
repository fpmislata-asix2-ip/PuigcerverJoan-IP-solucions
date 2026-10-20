def print_domino(n):
    for i in range(n + 1):
        for j in range(i, n + 1):
            print(f"{i}|{j}", end=" ")
        print()

if __name__ == "__main__":
    print_domino(8)