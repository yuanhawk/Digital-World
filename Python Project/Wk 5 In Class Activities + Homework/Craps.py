import random

craps = set([2,3,12])
naturals = set([7,11])
sum = [4,5,6,8,9,10]

def roll_two_dices():
    d1 = random.randrange(1,7)
    d2 = random.randrange(1,7)
    return d1,d2

def print_lose():
    return print('You lose')

def print_win():
    return print('You win')

def print_point(p):
    string = 'Your points are {:d}'.format(p)
    return print(string)

def is_craps(n):
    for i in craps:
        if n == i:
            return True
    
def is_naturals(n):
    for i in naturals:
        if n == i:
            return True
    
def play_craps():
    point = -1
    while True:
        n1, n2 = roll_two_dices()
        sumn = n1 + n2
        print('You rolled {:d} + {:d} = {:d}'.format(n1, n2, sumn))
        if point == -1:
            if is_craps(sumn):
                print_lose()
                return 0
            elif is_naturals(sumn):
                print_win()
                return 1
            point = sumn
            print_point(point)
        else:
            if sumn == 7:
                print_lose()
                return 0
            elif sumn == point:
                print_win()
                return 1

play_craps()
