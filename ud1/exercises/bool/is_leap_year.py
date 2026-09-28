def is_leap(year):
    """
    És de traspàs si:
    - És divisible entre 4.
    - Que no siga divisible entre 100.
        - A no ser que siga divisible entre 400.
    """
    es_divisible_4 = year % 4 == 0
    es_divisible_100 = year % 100 == 0
    es_divisible_400 = year % 400 == 0

    return es_divisible_4 and ((not es_divisible_100) or es_divisible_400)

year = int(input())

if is_leap(year):
    print("L'any", year, "és de traspàs.")
else:
    print("L'any", year, "no és de traspàs.")