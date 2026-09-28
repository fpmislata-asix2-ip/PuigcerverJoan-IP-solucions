import math

preu_redona = float(input("Preu redona: "))
diametre_redona = float(input("Diametre redona: "))

preu_rectangular = float(input("Preu rectangular: "))
amplaria_rectangular = float(input("Amplària rectangular: "))
alcada_rectangular = float(input("Alçada rectangular: "))

area_redona = math.pi * (diametre_redona / 2) ** 2
area_rectangular = amplaria_rectangular * alcada_rectangular

preu_per_cm2_redona = preu_redona / area_redona
preu_per_cm2_rectangular = preu_rectangular / area_rectangular

es_redona_mes_rentable = preu_per_cm2_redona < preu_per_cm2_rectangular
print(es_redona_mes_rentable)