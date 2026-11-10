def get_longest_word(text):
    longest = None
    for w in text.split():
        if longest is None or len(w) > len(longest):
            longest = w
    return longest

def get_shortest_word(text):
    shortest = None
    for w in text.split():
        if shortest is None or len(w) < len(shortest):
            shortest = w
    return shortest 

if __name__ == "__main__":
    # text = input()
    text = "Python es un llenguatge de programació molt potent i fàcil d'aprendre"

    word_count = len(text.split())
    char_count = len(text)
    # longest_word = get_longest_word(text)
    longest_word = max(text.split(), key=len)

    # shortest_word = get_shortest_word(text)
    shortest_word = min(text.split(), key=len)

    unique_count = 0

    print(f"Nombre de paraules: {word_count}")
    print(f"Nombre de caràcters: {char_count}")
    print(f"Paraula més llarga: {longest_word}")
    print(f"Paraula més curta: {shortest_word}")
    print(f"Nombre de paraules úniques: {unique_count}")
    print("Aparicions de cada paraula:")