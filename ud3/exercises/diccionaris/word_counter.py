def count_words(text):
    word_counter = {}
    for word in text.split():
        word = word.lower()
        # utilitzant get()
        word_counter[word] = word_counter.get(word, 0) + 1

        # sense utilitzar get
        # if word not in word_counter:
        #     word_counter[word] = 1
        # else:
        #     word_counter[word] += 1

    return word_counter


def print_word_ocurrences(word_counter):
    for word, ocurrences in sorted(word_counter.items()):
        print(f"{word}: {ocurrences}")

text = input()
word_counter = count_words(text)
print_word_ocurrences(word_counter)