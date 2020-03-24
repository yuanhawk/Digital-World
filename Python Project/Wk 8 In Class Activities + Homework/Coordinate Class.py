import math

class Coordinate:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        
    def magnitude(self):
        mag = math.sqrt(self.x ** 2 + self.y ** 2)
        return mag
    
    def translate(self, dx, dy):
        self.x += dx
        self.y += dy
        return self.x, self.y
    
    def __eq__(self, other):
        if other.x == self.x and other.y == self.y:
            return True
        return False