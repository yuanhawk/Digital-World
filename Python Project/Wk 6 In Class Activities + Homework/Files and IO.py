import math

class Coordinate:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def mag(self):
        return math.sqrt(self.x**2 + self.y**2)

def get_maxmin_mag(f):    
    cmax, cmin = Coordinate(), Coordinate(100,100)

    for line in f.readlines():
        x, y = line.split('\t')
        
        x = float(x)
        y = float(y)

        #print(x,y)

        ctry = Coordinate(x, y)
        
        if ctry.mag() > cmax.mag():
            cmax.x = ctry.x
            cmax.y = ctry.y
        if ctry.mag() < cmin.mag():
            cmin.x = ctry.x
            cmin.y = ctry.y

    return cmax, cmin