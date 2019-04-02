#!/usr/bin/env python3

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

    
    #okay now you just need to compute everything and figure out how to handle errors for non numbers.
    #keep up the good work!





def main():
    b1 = ()
    b2 = ()

    b1 = tuple(input('Please enter coordinates for ball 1 in format - x,y,z,r: ').split(','))
    b2 = tuple(input('Please enter coordinates for ball 2 in format - x,y,z,r: ').split(','))
    
    ball_collide(b1,b2)

if __name__ == '__main__':
    main()

