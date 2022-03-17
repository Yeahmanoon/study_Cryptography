# -*- coding: utf-8 -*-
# ex24.py

import sys
import math

def ex24(c):
    list_c = []
    for i in range(2, c + 1, 1):
        list_c.append(i)
    C = int(math.sqrt(c))
    for i in range(2, c, 1):
        for j in range(2, C, 1):
            try:
                list_c.remove(i * j)
            except ValueError:
                continue
    
    return list_c


if __name__ == '__main__':

    args = sys.argv

    c = int(args[1])
    list_seive = ex24(c)
    print(list_seive)