# -*- coding: utf-8 -*-
# euclid.py

import sys

#絶対値を求める
def abs(n):
    if n < 0:
        n = n * (-1)
    return n

#ユークリッドの互除法のアルゴリズム
def euclid(a, b):
    a = abs(a)
    b = abs(b)
    count = 0
    while b != 0:
        count += 1
        r = a % b
        a = b
        b = r
    print("反復回数：{0}".format(count))
    return a 

if __name__ == '__main__':

    args = sys.argv

    a = int(args[1])
    b = int(args[2])
    gcd = euclid(a, b)

    print("gcd({0},{1}) = {2}".format(a, b, gcd))
