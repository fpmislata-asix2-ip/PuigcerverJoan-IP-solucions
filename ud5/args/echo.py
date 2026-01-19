import argparse

def echo(words, upper=False, lower=False, reverse=False):
    if reverse:
        words = reversed(words)

    for w in words:
        if upper:
            w = w.upper()
        elif lower:
            w = w.lower()

        print(w, end=" ")
    print()

def echo2(words, upper=False, lower=False, reverse=False):
    if reverse:
        words = reversed(words)

    if upper:
        words = [w.upper() for w in words]
    elif lower:
        words = [w.lower() for w in words]
    print(" ".join(words))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("words", nargs="*")
    parser.add_argument("-u", "--uppercase", action="store_true")
    parser.add_argument("-l", "--lowercase", action="store_true")
    parser.add_argument("-r", "--reverse", action="store_true")
    args = parser.parse_args()
    print(args)

    words = args.words
    echo(words,
        upper=args.uppercase,
        lower=args.lowercase,
        reverse=args.reverse
    )