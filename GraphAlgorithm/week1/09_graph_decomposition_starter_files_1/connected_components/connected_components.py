#Uses python3

import sys


def number_of_components(adj,n):
    result = 0
    #write your code here
    v = [0]*n
    
    for i in range(n):
        if v[i] == 1:
            continue
        x = i
        s = []
        s.append(x)
        v[x] = 1
        while s:
            current = s[-1]
            complete = True
            for b in adj[current]:
                if v[b]==0:
                    s.append(b)
                    v[b] = 1
                    complete = False
                    break    
            if complete:
                s.pop()
            #print(s)
        result+=1

    return result

if __name__ == '__main__':
    n,m = map(int, input().split())
    adj = [[] for _ in range(n)]
    for i in range(0,m):
        a,b = map(int, sys.stdin.readline().split())
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(number_of_components(adj,n))
