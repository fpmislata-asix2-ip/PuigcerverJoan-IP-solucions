def get_month_days(month):
    match month:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            return 31
        case 4 | 6 | 9 | 11:
            return 30
        case 2:
            return 28
        case _:
            return -1

if __name__ == "__main__":
    month = int(input())
    days = get_month_days(month)
    if days == -1:
        print("Mes invàlid")
    else:
        print(days)