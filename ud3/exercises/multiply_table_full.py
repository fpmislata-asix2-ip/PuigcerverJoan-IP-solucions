from multiply_table import print_multiply_table

def print_multiply_table_range(a, b):
    for i in range(a, b + 1):
        print(f"=== TAULA DEL {i} ===")
        print_multiply_table(i)
        print()

a = int(input())
b = int(input())
print_multiply_table_range(a, b)