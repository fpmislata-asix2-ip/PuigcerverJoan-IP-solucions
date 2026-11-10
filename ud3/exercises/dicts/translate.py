translations = {
    "hello": "hola",
    "i": "jo",
    "am": "soc",
}

def translate(text):
    translated_text = []
    for w in text.split():
        tr_word = translations.get(w.lower(), w)

        # Ampliació - conserva el "case"
        if w.isupper():
            tr_word = tr_word.upper()
        elif w.istitle():
            tr_word = tr_word.title()

        # if w in translations:
        #     tr_w = translations[w]
        # else:
        #     tr_w = w

        translated_text.append(tr_word)
    return " ".join(translated_text)

if __name__ == "__main__":
    #sentence = input("> ")
    sentence = "Hello hello HELLO I am Joan"

    translated = translate(sentence)
    print(translated)