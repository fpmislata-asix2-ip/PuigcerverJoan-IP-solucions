def premer_boto(padlock, boto):
    i = boto - 1
    if i >= 0 and i < len(padlock):
        padlock[i] = not padlock[i]
    else:
        print(f"ERROR: El bolot {boto} està fora del rang.")

def padlock_repr(padlock):
    r = ""
    for i, e in enumerate(padlock):
        m = "X" if e else " "
        r += f"{i + 1}:[{m}] "
    return r

if __name__ == "__main__":
    padlock = [False] * 8

    n = int(input("> "))
    while n != 0:
        premer_boto(padlock, n)
        print(padlock_repr(padlock))

        n = int(input("> "))
