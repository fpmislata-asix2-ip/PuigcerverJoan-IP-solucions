from multiply_table import print_multiply_table

def print_multiple_multiply_table(start, end):
    for i in range(start, end + 1):
        print(f"=== TAULA DEL {i} === ")
        print_multiply_table(i)
        print()

if __name__ == "__main__":
    inici = int(input())
    final = int(input())

    print_multiple_multiply_table(inici, final)
