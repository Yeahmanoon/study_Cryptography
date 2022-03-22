# -*- coding: utf-8 -*-
# CFB.py
#ASCII(0~127) コード用

import sys

#10進数から2進数(桁固定)
def changeTo2from10(num, lim):
    d = lim / 2
    bin_num = ""
    while d > 0:
        if num // d == 1:
            num = num - d
            bin_num = bin_num + "1"
        else:
            bin_num = bin_num + "0"
        d = d // 2
    return bin_num

#暗号化関数(CFB)
def E_CFB(plaintext, key, c0, lim):
    ciphertext = ""
    bin_c = changeTo2from10(c0, lim)
    #print("bin_c {0}".format(bin_c))
    for i in range(0, len(plaintext), 1):
        bin_plaintext = changeTo2from10(ord(plaintext[i]), lim)
        print("bin_c          {0} in E".format(bin_c))
        print("bin_plaintext  {0} in E".format(bin_plaintext))
        bin_ciphertext = ""
        for j in range(0, len(bin_plaintext), 1):
            #print("bin_c[{0}] {1}".format(j, bin_c[j]))
            #print("bin_plaintext[{0}] {1}".format(j, bin_plaintext[j]))
            if int(bin_c[j]) + int(bin_plaintext[j]) == 1:
                bin_ciphertext = bin_ciphertext + "1"
            else:
                bin_ciphertext = bin_ciphertext + "0"
        print("bin_ciphertext {0} in E".format(bin_ciphertext))
        for j in range(0, lim, 1):
            if int(bin_ciphertext, 2) == key[0][j]:
                ciphertext = ciphertext + chr(key[1][j])
                bin_c = changeTo2from10(key[1][j], lim)
    return ciphertext 
    
#復号化関数(CFB)
def D_CFB(ciphertext, key, c0, lim):
    plaintext = ""
    bin_c = changeTo2from10(c0, lim)
    for i in range(0, len(ciphertext), 1):
        for j in range(0, lim, 1):
            if ord(ciphertext[i]) == key[1][j]:
                bin_ciphertext = changeTo2from10(key[0][j], lim)
        print("bin_c          {0} in D".format(bin_c))
        print("bin_ciphertext {0} in D".format(bin_ciphertext))
        bin_plaintext = ""
        for j in range(0, len(bin_ciphertext), 1):
            #print("bin_c[{0}] {1}".format(j, bin_c[j]))
            #print("bin_ciphertext[{0}] {1}".format(j, bin_ciphertext[j]))
            if int(bin_c[j]) + int(bin_ciphertext[j]) == 1:
                bin_plaintext = bin_plaintext + "1"
            else:
                bin_plaintext = bin_plaintext + "0"
        print("bin_plaintext  {0} in D".format(bin_plaintext))
        plaintext = plaintext + chr(int(bin_plaintext, 2))
        bin_c = changeTo2from10(ord(ciphertext[i]), lim)
    return plaintext


if __name__ == '__main__': 
    
    args = sys.argv

    plaintext = args[1]
    permutation = int (args[2])
    c0 = int(args[3])
    lim = 2**7
    key = [ [], [] ]
    for i in range(0, lim, 1):
        key[0].append(i)
        if i + permutation < lim and i + permutation >= 0:
            key[1].append(i + permutation)
        elif i + permutation >= lim:
            a = (i + permutation) // lim
            key[1].append(i + permutation - lim * a)
        elif i + permutation < 0 and i + permutation > -lim:
            key[1].append(i + permutation + lim)
        else:
            a = - (i + permutation) // lim + 1
            key[1].append(i + permutation + lim * a)
    print("c0             {0}".format(changeTo2from10(c0, lim)))
    ciphertext = E_CFB(plaintext, key, c0, lim)
    print(ciphertext)
    plaintext = D_CFB(ciphertext, key, c0, lim)
    print(plaintext)