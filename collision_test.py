#!/usr/bin/env python3

from collision import main, ball_collide
from urllib.request import urlopen
import sys


def main():
    txtfile = 'http://icarus.cs.weber.edu/home/lrowe/submit/files/balltest.txt'
    for line in txtfile:
        print(line)



if __name__ == '__main__':
    main()

