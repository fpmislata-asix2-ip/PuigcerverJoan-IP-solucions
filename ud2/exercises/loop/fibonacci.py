def fibonacci(i):
    n0 = 0
    n1 = 1
    n = n0 + 1
    for j in range(1, i):
        n = n0 + n1
        print(n)
        n0 = n1
        n1 = n

n = int(input())
fibonacci(n)