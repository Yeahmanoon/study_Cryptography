# -*- coding: utf-8 -*-
# pow.py

import sys

#高速指数計算法
def pow(base, exponent):
    result = 1
    #count = 0
    while exponent > 0:
        #count += 1
        if int(exponent) % 2 == 1:
            result = result * base
        base = base * base
        exponent = int(exponent) / 2
    #print("試行回数:{0}".format(count))
    return result

#雑魚雑魚指数計算法
def zakopow(base, exponent):
    result = 1
    #count = 0
    for i in range(0, exponent, 1):
        #count += 1
        result = result * base
    #print("試行回数:{0}".format(count))
    return result

if __name__ == '__main__':

    args = sys.argv

    base = int(args[1])
    exponent = int(args[2])

    result = pow(base, exponent)
    print("{0}^{1} = {2}".format(base, exponent, result))

    answer = zakopow(base, exponent) 
    print("{0}^{1} = {2}".format(base, exponent, answer))