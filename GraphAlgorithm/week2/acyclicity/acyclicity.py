#Uses python3

import sys


def acyclic(adj,n):

    preorder = [0]*n
    postorder = [0]*n
    
    t = 0

    visited = [0]*n

    while True:
        current = -1
        for i in range(0,n):
            if visited[i]==0:
                current = i
                break
        if current ==-1:
            break
        stack = []
        stack.append(current)
        visited[current] = 1
        preorder[current] = t
        t+=1
        while stack:
            #print(stack)
            current = stack[-1]
            next = -1
            for i in range(0,len(adj[current]) ):
                if adj[current][i] >=0:
                    next = adj[current][i]
                    adj[current][i]=-1
                    break
            if next >=0:
                if next in stack:
                    return 1
                visited[next] = 1
                stack.append(next)
                preorder[next] = t
                #print("append {0} t={1}".format(next,t))
            else:
                stack.pop()
                #print("pop {0} t={1}".format(current,t))
                postorder[current]= t
            t+=1
        
    print(preorder)
    print(postorder)
    return 0

if __name__ == '__main__':
    n,m = map(int, input().split())
    adj = [[] for _ in range(n)]
    for i in range(0,m):
        a,b = map(int, sys.stdin.readline().split())
        adj[a - 1].append(b - 1)
    print(acyclic(adj,n))
