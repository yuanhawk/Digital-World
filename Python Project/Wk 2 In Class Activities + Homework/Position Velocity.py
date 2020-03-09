def position_velocity(vo, t):
    g = 9.81

    #Equation to calculate position, y
    y = vo * t - 0.5 * g * t ** 2
    
    #Equation to calculate velocity, dy
    dy = vo - g * t
    return round(y, 2), round(dy, 2)

print(position_velocity(5.0, 10.0))
print(position_velocity(5.0, 0.0))
print(position_velocity(0.0, 5.0))