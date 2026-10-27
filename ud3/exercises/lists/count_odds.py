from list_utils import read_list

def count_odds_from_list(l):
    count = 0
    for n in l:
        if n % 2 != 0:
            count += 1
    return count

if __name__ == "__main__":
    l = read_list()
    n_odds = count_odds_from_list(l)
    print("Nombre de números imparells:", n_odds)