class Coordinate:
    def __init__(self, x=0, y=0): # Inserts self into the first argument
        self.x = x
        self.y = y

    def magnitude(self):
        return (self.x * self.x + self.y * self.y) ** 0.5

p1 = Coordinate()   # Create a new object instance
p2 = Coordinate(3, 4)