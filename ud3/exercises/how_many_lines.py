def count_until_end():
    count = 0
    text = input()
    while text != "END":
        count += 1
        text = input()

    return count


def count_until_end_while_true():
    count = 0
    while True:
        text = input()
        if text == "END":
            break
        count += 1

    return count


n = count_until_end()
print(n)