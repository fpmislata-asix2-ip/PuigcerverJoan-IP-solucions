nom = "Carla"        # `str`
edat = 30            # `int`
altura = 1.65        # `float`
es_estudiant = True  # `bool`

print("El meu nom és", nom)

## Operadors numèrics amb enters
a = 10
b = 3

suma = a + b
resta = a - b
multiplicacio = a * b
divisio = a // b
residu = a % b
potencia = a ** b

print("Suma:", suma)
print("Resta:", resta)
print("Multiplicació:", multiplicacio)
print("Divisió entera:", divisio)
print("Residu:", residu)
print("Potència:", potencia)

x = 5.5
y = 2.0

suma = x + y
resta = x - y
multiplicacio = x * y
divisio = x / y

print("Suma:", suma)
print("Resta:", resta)
print("Multiplicació:", multiplicacio)
print("Divisió:", divisio)

a = "aaac"
b = "aaab"

print("a és igual a b?", a == b)
print("a és diferent de b?", a != b)
print("a és menor que b?", a < b)
print("a és major que b?", a > b)
print("a és menor o igual que b?", a <= b)
print("a és major o igual que b?", a >= b)

## Operadors lògics
a = 21
b = 12

es_a_parell = (a % 2 == 0)
es_a_major_que_b = (a > b)

print("És A imparell?", not es_a_parell)
print("A és parell i major que B?", es_a_parell and es_a_major_que_b)