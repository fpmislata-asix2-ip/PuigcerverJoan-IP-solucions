class Rectangle:
    def __init__(self, width, height, x=0, y=0):
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2*self.width + 2*self.height

    def is_square(self):
        return self.width == self.height

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def contains(self, x, y):
        inside_x = self.x <= x <= (self.x + self.width) # chained comparison
        inside_y = self.y <= y <= (self.y + self.height)
        return inside_x and inside_y

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height}, x={self.x}, y={self.y})"


if __name__ == '__main__':
    r = Rectangle(x=-3, y=0, width=6, height=2)
    print(r)
    print(f"Area: {r.area()}")
    print(f"Perimeter: {r.perimeter()}")

    r.set_position(-1, -1)
    print(f"{r} moved to (-1, -1)")
    r.move(2, 2)
    print(f"{r} moved +2, +2")

    points = [
        (1, 1),
        (1, -1),
        (-4, 1),
        (-4, -1),
        (2, 0)
    ]
    for x, y in points:
        print(f"Is ({x}, {y}) inside {r}? -> {r.contains(x, y)}")
