import math

def calculate_area_circle(r):
    return math.pi * r ** 2

def calculate_area_rectangle(a, b):
    return a * b

def calculate_price_for_area(price, area):
    return price / area

price_circle = int(input())
diameter = int(input())
price_rectangle = int(input())
a = int(input())
b = int(input())

r = diameter / 2
area_circle = calculate_area_circle(r)
area_rectangle = calculate_area_rectangle(a, b)

preu_area_circle = calculate_price_for_area(price_circle, area_circle)
preu_area_rectangle = calculate_price_for_area(price_rectangle, area_rectangle)

if preu_area_circle < preu_area_rectangle:
    print(f"La pizza redona és més rentable: {preu_area_circle:.3f} €/cm²")
else:
    print(f"La pizza rectangular és més rentable: {preu_area_rectangle:.3f} €/cm²")