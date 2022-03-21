# -*- coding: utf-8 -*-
# p3_14_1.py

import sys
import os 

from pow import pow_mod
from pow import pow
sys.path.append(os.path.abspath(".."))
from Chapter2.ex24 import ex24

#素因数分解
def Prime_factorization(exponent):
    list_prime = []
    if exponent == 1:
        list_prime.append(1)
    else:    
        for i in ex24(exponent):
            while exponent % i == 0:
                exponent = exponent / i 
                list_prime.append(i)
    return list_prime

def p3_14_1(exponent, list_prime, base, modulo):
    e = {}
    f = {}
    count = 1
    for i in range(0, len(list_prime), 1):
        try:
            if list_prime[i] == list_prime[i + 1]:
                count += 1
            else:
                e[list_prime[i]] = count
                f[list_prime[i]] = 0
                for j in range(1, count + 1, 1):
                    sub_exponent = exponent / (pow(list_prime[i], j))
                    result = pow_mod(base, sub_exponent, modulo)
                    print("{0}^{1} == {2} mod {3}".format(base, sub_exponent, result, modulo))
                    if result == 1:
                        f[list_prime[i]] = j
                count = 1
        except IndexError:
            e[list_prime[i]] = count
            f[list_prime[i]] = 0
            for j in range(1, count + 1, 1):
                sub_exponent = exponent / (pow(list_prime[i], j))
                result = pow_mod(base, sub_exponent, modulo)
                print("{0}^{1} == {2} mod {3}".format(base, sub_exponent, result, modulo))
                if result == 1:
                    f[list_prime[i]] = j
    #print(e)
    #print(f)
    order = 1
    for i in e:
        order *= pow(i, e[i] - f[i]) 
    return order

if __name__ == '__main__':

    args = sys.argv

    exponent = int(args[1])#modulo の位数
    g = int(args[2])#調べたい元
    modulo = int(args[3])
    list_prime = Prime_factorization(exponent)
    print(list_prime)
    order = p3_14_1(exponent, list_prime, g, modulo)
    print("order ({0} + {1}ZZ) = {2}".format(g, modulo, order))