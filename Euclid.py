# -*- coding: utf-8 -*-
# Euclid.py

import sys

#絶対値を求める
def abs(n):
    if n < 0:
        n = n * (-1)
    return n

#ユークリッドの互除法のアルゴリズム
def Euclid(a, b):
    a = abs(a)
    b = abs(b)
    while b != 0:
        r = a % b
        a = b
        b = r
    return a 

if __name__ == '__main__':

    args = sys.argv

    a = int(args[1])
    b = int(args[2])
    gcd = Euclid(a, b)

    print("gcd({0},{1}) = {2}".format(a, b, gcd))
