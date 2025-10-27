def print_multiply_table(n):
    for i in range(1, 11):
        m = n * i
        print(f"{n} * {i:2d} = {m}")


if __name__ == '__main__':
    n = int(input())
    print_multiply_table(n)