def max(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2

a = int(input())
b = int(input())

resultat = max(n1=a, n2=b)
print("El nombre més gran es", resultat)