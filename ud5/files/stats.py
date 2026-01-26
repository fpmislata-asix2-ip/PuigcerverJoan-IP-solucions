import argparse
import os

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="+", type=str)
    return parser


def check_path(path):
    """
    Comprova si existeix un element en la ruta proporcionada
    i indica el seu tipus (fitxer o directori).
    """
    if not os.path.exists(path):
        print(f"{path}: No exists")
    elif os.path.isfile(path):
        print(f"{path}: File")
    elif os.path.isdir(path):
        print(f"{path}: Directory")
    else:
        print(f"{path}: Unknown")


if __name__ == "__main__":
    parser = create_parser()
    args = parser.parse_args()

    for path in args.path:
        check_path(path)