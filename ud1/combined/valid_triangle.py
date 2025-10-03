a = int(input())
b = int(input())
c = int(input())

def is_valid_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

if is_valid_triangle(a, b, c):
    print("El triangle és vàlid!")
