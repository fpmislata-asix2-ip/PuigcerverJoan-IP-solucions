from argparse import ArgumentParser

def salute(name):
    print(f"Hello, {name}!")

if __name__ == "__main__":
    parser = ArgumentParser(description="Salute program")
    parser.add_argument("name", nargs="?", default="World")
    args = parser.parse_args()

    salute(args.name)
