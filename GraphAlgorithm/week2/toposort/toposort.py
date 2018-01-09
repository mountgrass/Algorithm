#Uses python3

import sys

def dfs(adj, used, order, x):
    #write your code here
    pass


def toposort(adj):
    used = [0] * len(adj)
    order = []
    #write your code here

    preorder = [0]*n
    postorder = [0]*n
    visited = [0]*n
    t = 0

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
                if adj[current][i] >=0 and visited[ adj[current][i] ] ==0:
                    next = adj[current][i]
                    adj[current][i]=-1
                    break
            if next >=0:
                visited[next] = 1
                stack.append(next)
                preorder[next] = t
                #print("append {0} t={1}".format(next,t))
            else:
                stack.pop()
                #print("pop {0} t={1}".format(current,t))
                postorder[current]= t
            t+=1
        
    #print(preorder)
    #print(postorder)
    
    order = sorted(range(len(postorder)), key=postorder.__getitem__)
    order = reversed(order)
    return order

if __name__ == '__main__':
    n,m = map(int, input().split())
    adj = [[] for _ in range(n)]
    for i in range(0,m):
        a,b = map(int, sys.stdin.readline().split())
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

