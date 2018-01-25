#Uses python3

import sys
import queue

def extractMin(total, visited):
    minVal = 1.0e10
    minIndex = -1
    #print("after-total", total)
    for i in range( len(total)):
        if visited[i]==True:
            continue
        if total[i]!=-1 and total[i] < minVal:
            minVal = total[i]
            minIndex = i
    return minIndex

def distance(adj, cost, s, t):
    #write your code here
    n = len(adj)
    total = [-1] *n
    visited = [False] * n

    total[s] = 0
    while True:
        u = extractMin(total, visited)
        #print("u", u)
        if u==-1:
            break

        visited[u] = True
        #print("adj", adj[u])
        #print("before-total", total)
        for i in range( len(adj[u]) ):
            v = adj[u][i]          
            newCost = total[u]+cost[u][i]
            #print("newcost:", newCost)
            if total[v] >=0 and newCost > total[v]:
                continue
            total[v] = newCost
    
    return total[t]


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
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
