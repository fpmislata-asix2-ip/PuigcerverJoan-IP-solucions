def letter_frequency(text):
    text = text.lower()

    letter_counter = {}
    for l in text:
        if l.isalpha():
            letter_counter[l] = letter_counter.get(l, 0) + 1
    return letter_counter


def print_letter_fequency(letter_frequency):
    # t = (l, c) - Ordena per valors (t[1])
    for l, c in sorted(letter_frequency.items(), key=lambda t: t[1], reverse=True):
        print(f"{l}: {c}")


if __name__ == '__main__':
    text = input()
    letter_counter = letter_frequency(text)
    print_letter_fequency(letter_counter)