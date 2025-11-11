from list_utils import read_list

def count_odds(lst):
    count = 0
    for e in lst:
        if e % 2 != 0:
            count += 1

    return count


def odds_sublist(lst):
    odds_list = []
    for e in lst:
        if e % 2 != 0:
            odds_list.append(e)

    return odds_list


l = read_list()
print("Nombre de números imparells:", count_odds(l))
print("Números imparells:", odds_sublist(l))