def translate_text(text, translations_dict):
    """
    Translates the given text using the translations dict

    @param text String: text to be translated
    @return String: translated text
    """
    text = text.lower()

    translated = []
    for w in text.split():
        if w in translations_dict:
            w = translations_dict[w]
        translated.append(w)

    return " ".join(translated)
    # return " ".join([translations_dict.get(w, w) for w in text.lower().split()])


if __name__ == '__main__':
    translations_dict = {
        "hello": "hola",
        "world": "món",
        "cat": "gato",
        "dog": "gos",
        "food": "menjar",
        "water": "aigua",
        "house": "casa",
        "car": "cotxe",
        "book": "llibre",
        "computer": "ordinador"
    }

    text = input()
    translated = translate_text(text, translations_dict)
    print(translated)