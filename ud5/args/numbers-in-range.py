import argparse

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("start", type=int)
    parser.add_argument("end", type=int)
    parser.add_argument("-s", "--step", type=int, default=1)
    parser.add_argument("--exclude-end", action="store_true", default=False)
    return parser


def print_range(start, end, step=1, exclude_end=False):
    if not exclude_end:
        end += 1

    for n in range(start, end, step):
        print(n, end=" ")
    print()


if __name__ == "__main__":
    parser = create_parser()
    args = parser.parse_args()

    print_range(args.start, args.end, step=args.step, exclude_end=args.exclude_end)