
def shifter(arrayIn,shift):
    tmpAr = []
    n = len(arrayIn)
    for i in range(n):
        newIndex = (i+shift)%n
        tmpAr.append(arrayIn[newIndex])
    return tmpAr

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
    tmp3 = []
    #print(noteable)
    tmp3 = tmp2 + tmp
    return tmp3

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
     #print(noteable) 
     return dec
def binarizarDec(n):
    tmp = []
    aBin = list(bin(n))
    for i in aBin:
        if i == '1':
            tmp.append("1")
        if i == '0':
            tmp.append("0")
    tmp = tmp[1:]
    return tmp

def desbinarAr(binAr):
    oneLiner = "".join(binAr)
    binNtoDec = int(oneLiner,2)
    return binNtoDec

def xorear2list(l1,l2):
    tmp = []
    for i in range(len(l1)):
        tmp.append(l1[i]^l2[i])
    return tmp

def notGoodList(l1):
    tmp = []
    for i in l1:        
        tmp.append( (notGood(i)) )
    return tmp

def trilist(l):
    tmp = []
    for i in range(l):
        tmp.append(3)
    return tmp

def balanceList(d,p2Target):
    tmp = []
    for i in p2Target:
        tmp.append(d)
    return tmp

def andearList(l1,l2):
    tmp = []
    for i in range(len(l1)):
        tmp.append((l1[i])&(l2[i]))
    return tmp
def printAscii(lis):
    print("----ASCII----->")
    for i in lis:
        print(chr(i),end="")
    print("")
    print("-----endASCII------")
n = 64 # tamanio de palabra

m=0


z = [
11111010001001010110000111001101111101000100101011000011100110, 
10001110111110010011000010110101000111011111001001100001011010,
10101111011100000011010010011000101000010001111110010110110011,
11011011101011000110010111100000010010001010011100110100001111,
11010001111001101011011000100000010111000011001010010011101111
        ]

z = [
[1,1,1,1,1,0,1,0,0,0,1,0,0,1,0,1,0,1,1,0,0,0,0,1,1,1,0,0,1,1,0,1,1,1,1,1,0,1,0,0,0,1,0,0,1,0,1,0,1,1,0,0,0,0,1,1,1,0,0,1,1,0], 
[1,0,0,0,1,1,1,0,1,1,1,1,1,0,0,1,0,0,1,1,0,0,0,0,1,0,1,1,0,1,0,1,0,0,0,1,1,1,0,1,1,1,1,1,0,0,1,0,0,1,1,0,0,0,0,1,0,1,1,0,1,0],
[1,0,1,0,1,1,1,1,0,1,1,1,0,0,0,0,0,0,1,1,0,1,0,0,1,0,0,1,1,0,0,0,1,0,1,0,0,0,0,1,0,0,0,1,1,1,1,1,1,0,0,1,0,1,1,0,1,1,0,0,1,1],
[1,1,0,1,1,0,1,1,1,0,1,0,1,1,0,0,0,1,1,0,0,1,0,1,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,1,0,1,0,0,1,1,1,0,0,1,1,0,1,0,0,0,0,1,1,1,1],
[1,1,0,1,0,0,0,1,1,1,1,0,0,1,1,0,1,0,1,1,0,1,1,0,0,0,1,0,0,0,0,0,0,1,0,1,1,1,0,0,0,0,1,1,0,0,1,0,1,0,0,1,0,0,1,1,1,0,1,1,1,1]
        ]


T = 0
j = 0


if n == 16:
    m=4

if n == 24 or n == 32:
    m=4

if n == 48:
    m=3

if n == 64:
    m=4


if n == 16:
    T=32
    j=0
if n == 24:
    T=36
    j=1
if n == 32:
    T = 44
    j = 3
if n == 48:
    T = 54
    j = 3
if n == 64:
    T = 68
    j = 2



x = []
y = []
count = 0;

textoClaro = list("MatevickyForm123")

textoMatriz = []
llaveMatriz = []
for t in textoClaro:
    textoMatriz.append(int(ord(t)))
#    print(hex(ord(t)))
print(textoMatriz)

print("partes X , Y ")
x = textoMatriz[:8]
y = textoMatriz[8:]

print("x>",x)

printAscii(x)

print("y>",y)

printAscii(y)


#generacion de llaves a partir de la cadena dada
llaveClaro = list("qwertyuiopasdfghjklñzxcvbnmqwert")
for k in llaveClaro:
    llaveMatriz.append(int(ord(k)))
#Tomamos las llaves del mismo vector llaveMatriz
keys = [llaveMatriz[:8],llaveMatriz[8:16],llaveMatriz[16:24],llaveMatriz[24:32]]
# keysExt = []
# for i in range(len(keys)):
#     print("llave ->",i)
#     for k in range(len(keys[i])):
#                    print(binarizarDec(keys[i][k]),",",keys[i][k],",",chr(keys[i][k]))
#                    nK = ext(binarizarDec(keys[i][k]),8)
#                    keysExt.append(nK)
#     print("------------")

#nos conviene manejar todas las operaciones en decimal puesto que python nos permite manejar
#operaciones logicas a nivel de bits con decimales y solo binarizaremos cuando usemos corrimientos
#circulares y not ya que el corrimiento circular no existe como tal en python y el not
#lo usa como binario complemento a 2

#---------- key expansion ----------
# Todo esta dividido en suboperaciones ya que se me hacia mas facil depurarlo de esta forma
for  i in range(m,T-1):
    tmp = shifter(keys[i-1], -3)
    if m == 4:
        tmp = xorear2list(tmp, keys[i-3])
        tmpShift = shifter(tmp, -1)
        tmp = xorear2list(tmp,tmpShift)
        tmpNot = notGoodList(keys[i-m])
        tmp1st = xorear2list(tmpNot, tmp)
        pos = (i-m) % 62
        tmp2nd = xorear2list(tmp1st, balanceList(z[j][pos],tmp1st))
        tmp3 = xorear2list(tmp2nd, trilist(len(tmp2nd)))
        try:
            keys[i]=tmp3
        except:
            keys.append(tmp3)
            
#--------encryption--------------
for i in range(T-1):
    tmp = x
    tmpAnd =  andearList(x, shifter(x, 8))
    tmpShift2 = shifter(x, 2)
    tmpOpleft = xorear2list(tmpShift2, keys[i])
    tmpOpRight = xorear2list(y, tmpAnd)
    x = xorear2list( tmpOpleft , tmpOpRight )
    y = tmp

print(x,y,"<- parte x , y")
print("<------x,y equivalencia ascii------->")
print(">X")
printAscii(x)
print(">y")
printAscii(y)

#print(z, m, T)
