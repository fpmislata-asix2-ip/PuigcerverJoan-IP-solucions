def print_powers_of_two(n):
    for i in range(n + 1):
        pow = 2 ** i
        print(f"2^{i} = {pow}")

if __name__ == '__main__':
    n = int(input())
    print_powers_of_two(n)