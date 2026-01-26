import argparse
import os

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="+", type=str)
    return parser


def print_file_content(path):
    if os.path.exists(path):
        with open(path, "r") as f:
            content = f.read()
            print(content)
    else:
        print(f"Error: '{path}' no such file.")


if __name__ == "__main__":
    parser = create_parser()
    args = parser.parse_args()

    if len(args.path) == 1:
        path = args.path[0]
        print_file_content(path)

    else:
        for path in args.path:
            print(f"==== {path} ====")
            print_file_content(path)