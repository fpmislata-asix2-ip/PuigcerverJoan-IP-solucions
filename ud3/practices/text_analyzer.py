def word_count(text):
    return len(text.split())


def char_count(text):
    text = text.replace(" ", "")
    text = text.replace("'", "")
    return len(text)


def longest_word(text):
    #return max(text.split(), key=len)
    max_length_word = ""
    for w in text.split():
        if len(w) > len(max_length_word):
            max_length_word = w
    return max_length_word


def shortest_word(text):
    #return min(text.split(), key=len)
    words = text.split()
    min_length_word = words[0]
    for w in words:
        if len(w) < len(min_length_word):
            min_length_word = w
    return min_length_word


def uniq_word_count(text):
    uniq_word_counter = {}
    for w in text.split():
        if w not in uniq_word_counter:
            uniq_word_counter[w] = 1
        else:
            uniq_word_counter[w] += 1

        # uniq_word_counter[w] = uniq_word_counter.get(w, 0) + 1

    return uniq_word_counter


def print_word_count(uniq_word_dict):
    for w, c in uniq_word_dict.items():
        print(f"- {w}: {c}")


if __name__ == "__main__":
    text = input()

    print(f"Nombre de paraules: {word_count(text)}")
    print(f"Nombre de caràcters: {char_count(text)}")
    print(f"Paraula més llarga: {longest_word(text)}")
    print(f"Paraula més curta: {shortest_word(text)}")

    uniq_word_counter = uniq_word_count(text)
    print(f"Nombre de paraules úniques: {len(uniq_word_counter)}")
    print(f"Aparicions de cada paraula:")
    print_word_count(uniq_word_counter)