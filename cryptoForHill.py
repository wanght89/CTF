import math
import sympy
from sympy import init_printing,pprint
from sympy import Matrix
from sympy.vector import matrix_to_vector,CoordSysCartesian

def decrypt(matrix,words):
    cipher=''
    M=Matrix(matrix)
    print(M)
    M=M.inv_mod(64)
    length=len(M)
    print(length)
    d={}
    d2={}
    alphbet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789_{}"
    for x in range(len(alphbet)):
        d[alphbet[x]]=x
        d2[x]=alphbet[x]
    count=0
    l=[]

    for ch in words:
        if(count+1)%(8+1) ==0:
            m=Matrix(l)
            dot_pr_m=M*m
            n=[]
            for i in dot_pr_m:
                cipher+=d2[i%64]
            count=0
            l=[]
        l.append(d[ch])
        count += 1
    if(count+1) %(8+1) ==0:
        m=Matrix(l)
        dot_pr_m=M*m
        n=[]
        for i in dot_pr_m:
            cipher+=d2[i % 64]
    return cipher

if __name__=='__main__':
    matrixInfo = [[54, 53, 28, 20, 54, 15, 12, 7],
              [32, 14, 24, 5, 63, 12, 50, 52],
              [63, 59, 40, 18, 55, 33, 17, 3],
              [63, 34, 5, 4, 56, 10, 53, 16],
              [35, 43, 45, 53, 12, 42, 35, 37],
              [20, 59, 42, 10, 46, 56, 12, 61],
              [26, 39, 27, 59, 44, 54, 23, 56],
              [32, 31, 56, 47, 31, 2, 29, 41]]
    ciphertext = "7Nv7}dI9hD9qGmP}CR_5wJDdkj4CKxd45rko1cj51DpHPnNDb__EXDotSRCP8ZCQ"
    print(ciphertext)
    print(decrypt(matrixInfo,ciphertext))