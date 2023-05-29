class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + self.y)

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)
other = Point(3, 6)
point.draw()
print(type(point))
print(isinstance(point, Point))

print(point > other)
print(point + other)
