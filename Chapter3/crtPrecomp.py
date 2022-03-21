# -*- coding: utf-8 -*-
# cryPrecomp.py

import sys, os

sys.path.append(os.path.abspath(".."))
from Chapter2.xeuclid import xeuclid

def crtPrecomp(list_modulo):
    modulus = 1
    multipliers = []
    for i in range(0, len(list_modulo), 1):
        modulus = modulus * list_modulo[i]
    for i in range(0, len(list_modulo), 1):
        m = list_modulo[i]
        M = modulus / m
        gcd = xeuclid(M, m)
        multipliers.append(gcd[1] * M % modulus)
    return modulus, multipliers

def crt(list_modulo, list_x):
    result = 0
    return_crtPrecomp = crtPrecomp(list_modulo)
    modulus = return_crtPrecomp[0]
    multipliers = return_crtPrecomp[1]
    for i in range(0, len(list_modulo), 1):
        result = (result + multipliers[i] * list_x[i]) % modulus
    return result

if __name__ == '__main__':
    
    list_modulo = [4, 3, 5]
    list_x = [2, 1, 0]

    result = crt(list_modulo, list_x)
    for i in range(0, len(list_modulo), 1):
        print("x = {0} mod {1}".format(list_x[i], list_modulo[i]))
    print("x = {0}".format(result))