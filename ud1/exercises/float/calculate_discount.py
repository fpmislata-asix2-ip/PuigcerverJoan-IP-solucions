def calcular_descompte(preu, descompte):
    return preu * (1 - (descompte / 100))

preu_total = float(input())
descompte = float(input())

print(calcular_descompte(preu_total, descompte))