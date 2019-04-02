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
    print(b1,b2)
    (x1, y1, z1, r1) = b1
    (x2, y2, z2, r2) = b2

    X = pow(x2 - x1,2)
    print(X)

    Y = pow(y2 - y1,2)
    print(Y)

    Z = pow(z2-z1,2)
    print(Z)

    R = (r2 + r1)
    print(R)

    distance = math.sqrt(X + Y + Z)
    print(distance)
    if R > distance:
        print('Collides')
    else:
        print('Does not collide')

def main():
    b1 = ()
    b2 = ()

    #for testing purposes
    b1 = (1,2,4,6)
    b2 = (3,6,7,8)

    b1 = tuple(b1)
    b2 = tuple(b2)
    #b1 = tuple(input('Please enter coordinates for ball 1 in format - x,y,z,r: ').split(','))
    #b2 = tuple(input('Please enter coordinates for ball 2 in format - x,y,z,r: ').split(','))
    
    ball_collide(b1,b2)

if __name__ == '__main__':
    main()

