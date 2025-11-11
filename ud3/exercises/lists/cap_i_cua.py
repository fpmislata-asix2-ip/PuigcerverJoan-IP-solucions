from list_utils import read_list

def is_capicua_reverse(lst):
    return lst == lst[::-1]

def is_capicua_while(lst):
    i = 0
    j = len(lst) - 1
    while j > i:
        if lst[i] != lst[j]:
            return False

        i += 1
        j -= 1
    return True


def is_capicua_for(lst):
    for i in range(len(lst) // 2):
        if lst[i] != lst[-(i + 1)]:
            return False

    return True

l = read_list()
print("Is capicua (reverse)?:", is_capicua_reverse(l))
print("Is capicua (while)?:", is_capicua_while(l))
print("Is capicua (for)?:", is_capicua_for(l))