#Uses python3
import sys
import math
import numpy as np
def extractMin(priority, visited):
    minVal = 1.0e20
    minIndex = -1
    #print("after-priority", priority)
    for i in range( len(priority)):
        if visited[i]==True:
            continue
        if priority[i] < minVal:
            minVal = priority[i]
            minIndex = i
    return minIndex

def minimum_distance(x, y):
    result = 0.
    n = len(x)
    dist = np.zeros((n,n))
    for i in range(n):
        for j in range(i+1,n,1):
            dist[i][j] = np.sqrt( (x[i]-x[j])**2 + (y[i]-y[j])**2 )
            dist[j][i] = dist[i][j]
    #print(dist)
    q = [10**10]*n
    parent = [-1]*n
    visited = [False]*n
    
    q[0] = 0
    
    while True:
        u = extractMin(q, visited)
        if u==-1:
            break
        
        visited[u] = True
        for i in range(n):
            if i==u or visited[i]==True:
                continue
            #change priority
            if dist[u][i] < q[i]:
                parent[i] = u
                q[i] = dist[u][i]
    #print(parent)
    for i in range(n):
        if parent[i]>=0:
            result+=dist[ i ][parent[i]]
    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
