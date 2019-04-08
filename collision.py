#!/usr/bin/env python3
import sys
import math

def ball_collide(b1, b2):
    """ This function will determine whether or not the balls collide

        Args:
            b1 - tuple holding stats of ball 1
            b2 - tuple holding stats of ball 2

        Returns:
            boolean saying whether or not the balls are colliding
    """
    #tuple unpacking into correct coordinates
    (x1, y1, z1, r1) = b1
    (x2, y2, z2, r2) = b2

    #formula for calculation: sqrt((x2-x1)^2 + (Y2-y1)^2 + (Z2-z1)^2)
    #R is added together for comparison
    X = pow(int(x2) - int(x1),2)
    Y = pow(int(y2) - int(y1),2)
    Z = pow(int(z2) - int(z1),2)
    R = (int(r2) + int(r1))

    distance = math.sqrt(X + Y + Z)

    #For Testng Purposes
    #print(b1,b2)
    #print('X: ', X)
    #print('Y: ', Y)
    #print('Z: ', Z)
    #print('R: ', R)
    #print('Distance: ', distance)
    
    #comparing R to distance, if R is greater collision true else false
    if R > distance:
        print('Collides')
        return True
    else:
        print('Does not collide')
        return False



def main():
    b1 = ()
    b2 = ()

    #Storing input into two tuples hopefully entered in correctly
    b1 = tuple(input('Please enter coordinates for ball 1 in format - x,y,z,r: ').split(','))
    b2 = tuple(input('Please enter coordinates for ball 2 in format - x,y,z,r: ').split(','))
    
    #handling incorrect input with value error
    try:
        ball_collide(b1,b2)

    except ValueError:
        print('Please try again and  enter coordinates correctly')
        return -1

if __name__ == '__main__':
    main()

