#Uses python3

import sys

def reach(adj, n, x, y):
    #write your code here
    v = [0]*n
    s = []
    s.append(x)
    v[x] = 1
    while s:
        current = s[-1]
        if current == y:
            return 1
        #print(s)
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
            
    return 0

if __name__ == '__main__':
    #print('read input and parse')
    #input = sys.stdin.read()
    #data = list(map(int, input.split()))
    #print(data)
    #n, m = data[0:2]
    #data = data[2:]
    #edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    #x, y = data[2 * m:]
    n,m = map(int, input().split())
    adj = [[] for _ in range(n)]
    for i in range(0,m):
        a,b = map(int, sys.stdin.readline().split())
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    x,y = map(int, sys.stdin.readline().split())
    x = x-1
    y = y-1
    #print(n,m,adj,x,y)
    print(reach(adj, n, x, y))
