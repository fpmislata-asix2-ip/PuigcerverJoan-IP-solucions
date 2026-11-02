def parse_user(line):
    parts = line.split(":")
    user = parts[0]
    home = parts[5]
    shell = parts[6]

if __name__ == "__main__":
    line = input()

    if line != "END":
        parse_user(line)
        line = input()