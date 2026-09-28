a = 2
b = 2.0
print("a:", a, "(", type(a), ")")
print("b:", b, "(", type(b), ")")

suma = a + b
print("a + b:", suma, "(", type(suma), ")")


divisio = a / b
print("a / b:", divisio, "(", type(divisio), ")")

int_divisio = a // b
print("a // b:", int_divisio, "(", type(int_divisio), ")")


residu = a % b
print("a % b:", residu, "(", type(residu), ")")

potencia = a ** b
print("a ** b:", potencia, "(", type(potencia), ")")

print("a == b", a == b)
print("a != b", a != b)
print("a < b", a < b)
print("a > b", a > b)
print("a <= b", a <= b)
print("a >= b", a >= b)

a = 2
b = 2
c = 2
iguals = a == b and b == c
print("a == b == c", iguals)