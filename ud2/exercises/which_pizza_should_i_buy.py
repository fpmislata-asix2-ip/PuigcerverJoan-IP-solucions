import math

def calcular_area_cercle(radi):
    return math.pi * (radi ** 2)

def calcular_area_rectangle(base, altura):
    return base * altura

def calcular_preu_area(preu, area):
    return preu / area


if __name__ == "__main__":
    preu_redona = float(input("Preu redona: "))
    diametre_redona = float(input("Diametre redona: "))

    preu_rectangular = float(input("Preu rectangular: "))
    amplada_rectangular = float(input("Amplària rectangular: "))
    alcada_rectangular = float(input("Alçada rectangular: "))

    radi = diametre_redona / 2
    area_redona = calcular_area_cercle(radi)
    area_rectangular = calcular_area_rectangle(amplada_rectangular, alcada_rectangular)

    preu_per_cm2_redona = calcular_preu_area(preu_redona, area_redona)
    preu_per_cm2_rectangular = calcular_preu_area(preu_rectangular, area_rectangular)

    if preu_per_cm2_redona < preu_per_cm2_rectangular:
        print("La pizza redona és més rentable:", round(preu_per_cm2_redona, 3), "€/cm²")
    else:
        print("La pizza rectangular és més rentable:", round(preu_per_cm2_rectangular, 3), "€/cm²")