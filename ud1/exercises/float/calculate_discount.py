preu_producte = float(input())
descompte = float(input())

preu_actual = preu_producte * (1 - (descompte / 100))

print(preu_actual)