# -*- coding: utf-8 -*-
# ex10.py

import sys

def ex10(n, g):
    if g == 2:
        return bin(n)
    elif g == 8:
        return oct(n)
    elif g == 16:
        return hex(n)
    else:
        print("Unnecessary") 

if __name__ == '__main__':

    args = sys.argv

    n = int(args[1])
    g = int(args[2])
    r = ex10(n, g)

    print("{0} is {1}".format(n, r))