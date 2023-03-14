#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 13:16:06 2023

@author: retina15
"""
bits = ["A","B","C","D"]

def shifter(arrayIn,shift):
    tmpAr = []
    n = len(arrayIn)
    for i in range(n):
        newIndex = (i+shift)%n
        tmpAr.append(arrayIn[newIndex])
    return tmpAr

print(shifter(bits,-3))



xor = int(30000) ^ int(40000)
a = hex(30000)
b = hex(40000)
xor = hex(xor)

ander = 40000 & 30000
#ander = hex(ander)


no = ~(4)
#no = bin(no)

vik = hex(no & 8)
vik2 = hex(no ^8)

def ext(arrIn, lenTarget):    
    tmp = []
    aBin = arrIn
    for i in aBin:
        if i == '1':
            tmp.append("1")
        if i == '0':
            tmp.append("0")
    tmp = tmp[1:]
    tmp2 = []
    for i in range(lenTarget-len(tmp)):
        tmp2.append("0")
    #print(tmp)    
    #print(tmp2)
    #print(noteable)
    return tmp2+tmp

g = list(bin(10))

k = ext(g,5)
print(k)

def notGood(a):
     tmp = []
     aBin = list(bin(a))
     for i in aBin:
         if i == '1':
            tmp.append("0")
         if i == '0':
             tmp.append("1")
     size = len(tmp)-1
     #print(tmp)    
     noteable = tmp[1:]
     #print(noteable)
     tmp = "".join(noteable)
     dec = 0
     for i in range(len(noteable)-1,0,-1):
         if noteable[i]=="1":
            dec+= 2**(i-1)
            #print(dec)
     print(noteable) 
     return dec
def binarizar(n):
    tmp = []
    aBin = list(bin(n))
    for i in aBin:
        if i == '1':
            tmp.append("1")
        if i == '0':
            tmp.append("0")
    tmp = tmp[1:]
    #print(tmp)
    return tmp

bintest=binarizar(157)

print(bintest)



def desbinarAr(binAr):
    oneLiner = "".join(binAr)
    binNtoDec = int(oneLiner,2)
    return binNtoDec

print(desbinarAr(bintest))

print(4<<1)
print(4^5)


def xorear2list(l1,l2):
    tmp = []
    for i in range(len(l1)):
        tmp.append(l1[i]^l2[i])
    return tmp
pol1 = [4,2,1,2,1]
pol2 = [5,2,1,2,1]

print(xorear2list(pol1, pol2))

def notGoodList(l1):
    tmp = []
    for i in l1:        
        tmp.append( (notGood(i)) )
    return tmp
print(notGoodList(pol1))
# testNot = notMamalon(50)
# print(testNot)
def trilist(l):
    tmp = []
    for i in range(l):
        tmp.append(3)
    return tmp
print(trilist(6))
print(notGood(4))
z = [
[1,1,1,1,1,0,1,0,0,0,1,0,0,1,0,1,0,1,1,0,0,0,0,1,1,1,0,0,1,1,0,1,1,1,1,1,0,1,0,0,0,1,0,0,1,0,1,0,1,1,0,0,0,0,1,1,1,0,0,1,1,0], 
[1,0,0,0,1,1,1,0,1,1,1,1,1,0,0,1,0,0,1,1,0,0,0,0,1,0,1,1,0,1,0,1,0,0,0,1,1,1,0,1,1,1,1,1,0,0,1,0,0,1,1,0,0,0,0,1,0,1,1,0,1,0],
[1,0,1,0,1,1,1,1,0,1,1,1,0,0,0,0,0,0,1,1,0,1,0,0,1,0,0,1,1,0,0,0,1,0,1,0,0,0,0,1,0,0,0,1,1,1,1,1,1,0,0,1,0,1,1,0,1,1,0,0,1,1],
[1,1,0,1,1,0,1,1,1,0,1,0,1,1,0,0,0,1,1,0,0,1,0,1,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,1,0,1,0,0,1,1,1,0,0,1,1,0,1,0,0,0,0,1,1,1,1],
[1,1,0,1,0,0,0,1,1,1,1,0,0,1,1,0,1,0,1,1,0,1,1,0,0,0,1,0,0,0,0,0,0,1,0,1,1,1,0,0,0,0,1,1,0,0,1,0,1,0,0,1,0,0,1,1,1,0,1,1,1,1]
        ]




print(z[1][0])
llavero = [
    [123,123,345,567,789,46,34,12],
    [12,456,678,234,456,234,123,77]
    ]

def balanceList(d,p2Target):
    tmp = []
    for i in p2Target:
        tmp.append(d)
    return tmp

def extensorK(k,target):
    tmp = []
    for i in range(target):
        try:
            tmp.append(k[i])
        except:
            tmp.append([0,0,0,0,0,0,0,0])
    return tmp

print(balanceList(2, pol1))

print(extensorK(llavero, 9))

def andearList(l1,l2):
    tmp = []
    for i in range(len(l1)):
        tmp.append((l1[i])&(l2[i]))
    return tmp
p1=[1,1,1,4,4,4]
p2=[1,2,3,4,5,6]
print(p1,p2)
print(andearList(p1, p2))
def ext2(arr, target):
    t = target-len(arr)
    tmp = [0]*t
    return tmp+arr

def joinList(l1):
    z=[]
    for i in range(len(l1)):
        z = z + l1[i]
    return z

l = [[1,2,3],[1,1,1]]
ll=joinList(l)
ll= ext2(ll, 30)

tag =  [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1] 

def desTag128(Ta):
    n=8
    output=[Ta[i:i + n] for i in range(0, len(Ta), n)]
    tmp = []
    for i in output:
        res = int("".join(str(x) for x in i), 2)
        tmp.append(res)
    return tmp

def asciificarTag(l1):
    tmp = []
    print("Tag en ascii:")
    for i in l1:
        print(chr(i),end="")
    print(" ")
kkl = desTag128(tag)

asciificarTag(kkl)
# print()
