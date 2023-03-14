#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 13:32:00 2023

@author: retina15
"""
import numpy as np

def MGF( A, B, P):
  M = np.polymul(A,B)
  q, r = np.polydiv(M, P)
  return r % 2

def ext(arrIn, lenTarget):    
    tmp = []
    aBin = arrIn
    for i in aBin:
        if i == 1:
            tmp.append(1)
        if i == 0:
            tmp.append(0)
    #tmp = tmp[1:]
    tmp2 = []
    for i in range(lenTarget-len(tmp)):
        tmp2.append(0)
    #print(tmp)    
    #print(tmp2)
    #print(noteable)
    return tmp2+tmp

fileList = []
with open('a.jpg', 'rb') as f:
    binValue = f.read(1)
    while len(binValue) != 0:
        hexVal = hex(ord(binValue))
        fileList.append(hexVal)
        #print(hexVal)
        # Do something with the hex value
        binValue = f.read(1)

def subDiv128(l):
    n=16
    output=[l[i:i + n] for i in range(0, len(l), n)]
    return output

def binarizarDec(n):
    tmp = []
    aBin = list(bin(n))
    for i in aBin:
        if i == '1':
            tmp.append(1)
        if i == '0':
            tmp.append(0)
    tmp = tmp[1:]
    return tmp

def xorear2list(l1,l2):
    tmp = []
    for i in range(len(l1)):
        tmp.append(l1[i]^l2[i])
    return tmp

subAr=subDiv128(fileList)
print(subAr)

a = int(subAr[0][0],base=16)
b=ext(binarizarDec(a),8)
print(b)
gmac = [0]*128

Ms = []
for i in range(len(subAr)):
    tmp = []
    for j in range(len(subAr[i])): 
        a = ext(binarizarDec(int(subAr[i][j],base=16)),8)#target son 8 de cada palabra de 1 byte
        tmp.append(a)
    Ms.append(tmp)
MsGood =[]  
for i in range(len(Ms)):
    z = []
    for j in range(len(Ms[i])):
       z=z+Ms[i][j]
    MsGood.append(z)



for m in MsGood:
    gmac = MGF(xorear2list(gmac, m), , P) 