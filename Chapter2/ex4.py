# -*- coding: utf-8 -*-
# ex4.py

import sys

def ex4(a, b):
    if b > 0:
        for r in range(int (-b/2) ,int(b/2)+ 1,1):
            #print(r)
            q = a / (b + r)
            if q % 1 == 0:
                print("q is {0}".format(int(q)))
                print("{0} = {1} x {2} + {3}".format(a,int(q),b,r))
                return r
                break
    else:
        print("b is smaller than 0")

if __name__ == '__main__':

    args = sys.argv

    a = int(args[1])
    b = int(args[2])
    r = ex4(a, b)
    print("r is {0}".format(r))