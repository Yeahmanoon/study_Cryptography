# -*- coding: utf-8 -*-
# ECB.py
#ASCII(0~127) コード用

import sys

#暗号化関数(ECB)
def E_ECB(plaintext, key):
    ciphertext = ""
    for i in range(0, len(plaintext), 1):
        for j in range(0, 128, 1):
            if ord(plaintext[i]) == key[0][j]:
                ciphertext = ciphertext + chr(key[1][j])
    return ciphertext 
    
#復号化関数(ECB)
def D_ECB(ciphertext, key):
    plaintext = ""
    for i in range(0, len(ciphertext), 1):
        for j in range(0, 128, 1):
            if ord(ciphertext[i]) == key[1][j]:
                plaintext = plaintext + chr(key[0][j])
    return plaintext


if __name__ == '__main__': 
    
    args = sys.argv

    plaintext = args[1]
    permutation = int (args[2])
    key = [ [], [] ]
    for i in range(0, 128, 1):
        key[0].append(i)
        if i + permutation < 128 and i + permutation >= 0:
            key[1].append(i + permutation)
        elif i + permutation >= 128:
            a = (i + permutation) // 128
            key[1].append(i + permutation - 128 * a)
        elif i + permutation < 0 and i + permutation > -128:
            key[1].append(i + permutation + 128)
        else:
            a = - (i + permutation) // 128 + 1
            key[1].append(i + permutation + 128 * a)

    ciphertext = E_ECB(plaintext, key)
    print(ciphertext)
    plaintext = D_ECB(ciphertext, key)
    print(plaintext)