class Permissions:
    def __init__(self, read=False, write=False, execute=False):
        self.read = read
        self.write = write
        self.execute = execute

    def __str__(self):
        r = "r" if self.read else "-"
        w = "w" if self.write else "-"
        x = "x" if self.execute else "-"
        return f"{r}{w}{x}"

    def enable(self, p):
        match p:
            case "r":
                self.read = True
            case "w":
                self.write = True
            case "x":
                self.execute = True
            case _:
                raise ValueError(f"Value {p} not supported.")

    def disable(self, p):
        match p:
            case "r":
                self.read = False
            case "w":
                self.write = False
            case "x":
                self.execute = False
            case _:
                raise ValueError(f"Value {p} not supported.")

    def toggle(self, p):
        match p:
            case "r":
                self.read = not self.read
            case "w":
                self.write = not self.write
            case "x":
                self.execute = not self.execute
            case _:
                raise ValueError(f"Value {p} not supported.")

    def has(self, p):
        match p:
            case "r":
                return self.read
            case "w":
                return self.write
            case "x":
                return self.execute
            case _:
                raise ValueError(f"Value {p} not supported.")

    def __eq__(self, other):
        return self.read == other.read \
            and self.write == other.write \
            and self.execute == other.execute

    def __or__(self, other):
        read = self.read or other.read
        write = self.write or other.write
        execute = self.execute or other.execute
        return Permissions(read=read, write=write, execute=execute)


    def __and__(self, other):
        read = self.read and other.read
        write = self.write and other.write
        execute = self.execute and other.execute
        return Permissions(read=read, write=write, execute=execute)

if __name__ == '__main__':
    p1 = Permissions(read=False, write=False, execute=True) # --x
    p2 = Permissions(read=False, write=True, execute=False) # -w-

    print(p1, "or", p2, "=", p1 | p2)
    print(p1, "and", p2, "=", p1 & p2)
