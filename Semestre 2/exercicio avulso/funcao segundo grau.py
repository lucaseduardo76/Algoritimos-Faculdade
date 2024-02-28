from math import sqrt

def funcSec(a,b,c):
    delta = b**2 - 4*a*c
    if(delta > 0):
        xpos = ((-b) + sqrt(delta))/(2*a)
        xneg = ((-b) - sqrt(delta))/(2*a)

        return[xpos, xneg]
    elif(delta == 0):
        xpos = ((-b) + sqrt(delta))/(2*a)

        return xpos

print(funcSec(1,25,6))


