import math

def area_vol_cylinder(r, l):
  a = math.pi * r * r
  v = math.pi * r * r * l
  return round(a, 2), round(v, 2)

print(area_vol_cylinder(1.0, 2.0))
print(area_vol_cylinder(2.0, 2.3))
print(area_vol_cylinder(1.5, 4))
print(area_vol_cylinder(2.2, 5.0))