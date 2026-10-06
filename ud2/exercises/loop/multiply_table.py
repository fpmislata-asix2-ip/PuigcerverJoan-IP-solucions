def print_multiply_table(n):
    for i in range(1, 11):
        print(f"{n} * {i} = {n * i}")

if __name__ == "__main__":
    n = int(input())
    print_multiply_table(n)
