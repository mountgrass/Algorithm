#Uses python3

import sys
import queue


def shortet_paths(adj, cost, s, distance, reachable, shortest):
    #write your code here
    n = len(adj)
    #distance = [1.0e10] * n
    distance[s] = 0
    A = []
    for i in range(n):
        updated = False
        #print(distance)
        for u in range(n):            
            for j in range( len(adj[u]) ):
                v = adj[u][j]
                newDist = distance[u]+cost[u][j]
                #print(u,v,newDist)
                if newDist < distance[v]:
                    distance[v] = newDist
                    if i==n-1 and distance[v] < 10**12:
                        A.append(v)
                        updated = True
    
    #print("A", A, updated)
    visited = [0] * n
    InfA = []
    while A:
        u = A.pop(0)
        visited[u] = 1
        InfA.append(u)
        for v in adj[u]:
            if visited[v]==1:
                continue
            A.append(v)
            
    for i in range(n):
        if distance[i] < 10**12:
            reachable[i] = 1
    
    for u in InfA:
        shortest[u] = 0

    #print("reachable:", reachable)
    #print("distance", distance)
    #print("shortest", shortest)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s = data[0]
    s -= 1
    distance = [10**19] * n
    reachable = [0] * n
    shortest = [1] * n
    shortet_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])

