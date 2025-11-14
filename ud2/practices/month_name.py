def is_valid_month_number(n):
    return n >= 1 and n <= 12

def get_month_name(n):
    match (n):
        case 1:
            return "Gener"
        case 2:
            return "Febrer"
        case 3:
            return "Març"
        case _:
            return "NO_VALID"

if __name__ == '__main__':
    n = int(input())
    while not is_valid_month_number(n):
        print(f"El valor '{n}' no és vàlid.")
        n = int(input())

    month = get_month_name(n)
    print(month)