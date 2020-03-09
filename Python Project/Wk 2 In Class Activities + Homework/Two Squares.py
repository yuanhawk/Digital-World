class Coordinate:
    x = 0
    y = 0
    
def is_in_square(s1, r1, s2, r2):
    #Coordinates of s1
    s1_botleft_x = s1.x - r1 / 2
    s1_botleft_y = s1.y - r1 / 2
    
    s1_topright_x = s1.x + r1 / 2
    s1_topright_y = s1.y + r1 / 2
    

    #Coordinates of s2
    s2_botleft_x = s2.x - r2 / 2
    s2_botleft_y = s2.y - r2 / 2
    
    s2_topright_x = s2.x + r2 / 2
    s2_topright_y = s2.y + r2 / 2
    
    
    #If condition is fulfilled (x or y position)
    if (s1_botleft_x > s2_topright_x or s1_botleft_y > s2_topright_y):
        return False
    elif (s1_topright_x < s2_botleft_x or s1_topright_y < s2_botleft_y):
        return False
    else:
        return True
    

s1 = Coordinate()
s1.x, s1.y = 10, 10
s2 = Coordinate()
s2.x, s2.y = 20, 10
is_in_square(s1, 5, s2, 4)