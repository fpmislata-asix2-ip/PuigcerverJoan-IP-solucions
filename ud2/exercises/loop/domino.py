def domino():
    for i in range(0, 6 + 1):
        for j in range(i, 6 + 1):
            print(f"{i}|{j}", end=" ")
        print()

domino()