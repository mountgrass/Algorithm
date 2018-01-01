# python3
from random import *

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def toNumber(t):
    return ord(t)-ord('A')

def PrecomputeHashes(T, P, p, x):
    lenT = len(T)
    lenP = len(P)
    H=[]
    for i in range(0, lenT-lenP+1):
        H.append(0)
    S = T[lenT-lenP:lenT]
    H[lenT-lenP]= PolyHash(S, p,x)
    y = 1
    for i in range(0, lenP):
        y = (y*x+p)%p
        
    for i in range(lenT-lenP-1, -1, -1):
        #print(T[i:i+lenP])
        H[i] = x*H[i+1]+toNumber(T[i])-y*toNumber(T[i+lenP])
        H[i] = (H[i]+p)%p

    #print(H) 
    return H

def PolyHash(P, p, x):
    lenP = len(P)
    hash = 0
    for i in range(lenP-1, -1, -1):
        hash = hash*x + toNumber(P[i])
        hash = (hash+p)%p
    return hash
    
def get_occurrences(pattern, text):
    """return [
        i 
        for i in range(len(text) - len(pattern) + 1) 
        if text[i:i + len(pattern)] == pattern
    ]"""
    p = 100003
    x = randint(1,p-1)
    result=[]
    pHash = PolyHash(pattern, p, x)
    H = PrecomputeHashes(text, pattern, p, x)
    lenT = len(text)
    lenP = len(pattern)
    for i in range(0, lenT-lenP+1):
        #print(pHash, H[i])
        if pHash!=H[i]:
            continue
        s = text[i:i+lenP]
        if s==pattern:
            result.append(i)
    return result

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

