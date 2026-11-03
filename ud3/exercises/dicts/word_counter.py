def count_words(text):
    words = text.lower().split()

    counter = {}
    for w in words:
        if w not in counter:
            counter[w] = 1
        else:
            counter[w] += 1

    return counter


if __name__ == "__main__":
    text = input("> ")
    word_count = count_words(text)

    for w, count in word_count.items():
        print(f"{w}: {count}")