def count_vowels(text):
    dict_vowels = {}

    relacio_vocals_accents = {
        "á": "a",
        "à": "a",
        "é": "e",
        "è": "e",
        "í": "i",
        "ì": "i",
        "ó": "o",
        "ò": "o",
        "ú": "u",
        "ù": "u",
    }

    for c in text.lower():
        if c in relacio_vocals_accents:
            c = relacio_vocals_accents[c]
        if c in "aeiou":
            dict_vowels[c] = dict_vowels.get(c, 0) + 1

    return dict_vowels


def pretty_print_vowels(dict_vowels):
    for v in "aeiou":
        print(f"{v}: {dict_vowels.get(v, 0)}")


if __name__ == '__main__':
    text = input()

    dict_count = count_vowels(text)
    pretty_print_vowels(dict_count)