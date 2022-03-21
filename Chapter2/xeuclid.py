# -*- coding: utf-8 -*-
# xeuclid.py

import sys

#絶対値を求める
def abs(n):
    if n < 0:
        n = n * (-1)
    return n

#拡張されたユークリッドのアルゴリズム
def xeuclid(a, b):
    #係数の初期化
    xs = []
    ys = []
    xs.append(1)
    xs.append(0)
    ys.append(0)
    ys.append(1)
    sign = 1
    count = 0
    while b != 0:
        count += 1
        r = a % b
        q = a // b
        a = b
        b = r
        xx = xs[1]
        yy = ys[1]
        xs[1] = q * xs[1] + xs[0]
        ys[1] = q * ys[1] + ys[0]
        xs[0] = xx
        ys[0] = yy
        sign = sign * (-1)
    #print("反復回数：{0}".format(count))
    x = sign * xs[0]
    y = - sign * ys[0]
    return a, x, y

if __name__ == '__main__':

    args = sys.argv

    a = int(args[1])
    b = int(args[2])
    gcd = xeuclid(a, b)

    print("gcd({0},{1}) = {2}".format(a, b, gcd))
