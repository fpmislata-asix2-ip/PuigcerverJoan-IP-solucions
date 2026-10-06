def valor_absolut(n):
    if n < 0:
        return -n
    return n

if __name__ == "__main__":
    n = int(input())
    print(valor_absolut(n))