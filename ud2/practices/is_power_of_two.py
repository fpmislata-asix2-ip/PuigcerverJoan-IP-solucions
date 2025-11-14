def is_power_of_two(n):
    while n % 2 == 0:
        n //= 2

    return n == 1
    

if __name__ == '__main__':
    n = int(input())
    print(is_power_of_two(n))