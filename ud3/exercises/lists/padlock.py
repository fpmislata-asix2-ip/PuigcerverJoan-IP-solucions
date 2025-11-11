def print_padlock(padlock):
    half = (len(padlock) + 1) // 2
    for i in range(half):
        print(f"{i + 1}: [{"X" if padlock[i] else " "}]", end=" ")
        j = i + half
        if j < len(padlock):
            print(f"{j + 1}: [{"X" if padlock[j] else " "}]")


padlock = [False] * 8
print_padlock(padlock)