import math

class Coordinate:
  x = 0
  y = 0

def area_of_triangle(p1, p2, p3):
  #Calculate using absolute values
  area = abs(p1.x * p2.y + p2.x * p3.y + p3.x * p1.y - p3.y * p1.x - p1.y * p2.x - p2.y * p3.x) / 2
  return round(area, 2)
    
print("Test Case 1")
p1 = Coordinate()
p1.x = 1.5
p1.y = -3.4
p2 = Coordinate()
p2.x = 4.6
p2.y = 5
p3 = Coordinate()
p3.x = 9.5
p3.y = -3.4
print(area_of_triangle(p1, p2, p3))

print("Test Case 2")
p1 = Coordinate()
p1.x = 2.0
p1.y = -3.4
p2 = Coordinate()
p2.x = 4.6
p2.y = 5
p3 = Coordinate()
p3.x = 9.5
p3.y = -1.4
print(area_of_triangle(p1, p2, p3))

print("Test Case 3")
p1 = Coordinate()
p1.x = 1.5
p1.y = 3.4
p2 = Coordinate()
p2.x = 4.6
p2.y = 5
p3 = Coordinate()
p3.x = -1.5
p3.y = 3.4
print(area_of_triangle(p1, p2, p3))

print("Test Case 4")
p1 = Coordinate()
p1.x = -1.5
p1.y = 3.4
p2 = Coordinate()
p2.x = 4.6
p2.y = 5
p3 = Coordinate()
p3.x = 4.3
p3.y = -3.4
print(area_of_triangle(p1, p2, p3))