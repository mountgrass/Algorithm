# python3

import sys

n, m = map(int, sys.stdin.readline().split())
tableSize = list(map(int, sys.stdin.readline().split()))
rank = [1] * n
parent = list(range(0, n))
ans = max(tableSize)

def getParent(table):
    # find parent and compress path
    #if table!=parent[table]:
    #    parent[table] = getParent(parent[table])
    elem =[]
    while table!=parent[table]:
        table = parent[table]
        elem.append(table)

    for e in elem:
        parent[e] = table
    return table

def merge(destination, source):
    realDestination, realSource = getParent(destination), getParent(source)

    if realDestination == realSource:
        return False,tableSize[realDestination]

    mergedSize = 0
    # merge two components
    # use union by rank heuristic 
    # update ans with the new maximum table size
    #print(rank)
    if rank[realSource] < rank[realDestination]:
        parent[realSource] = realDestination
        tableSize[realDestination]+=tableSize[realSource]
        tableSize[realSource] = 0
        mergedSize = tableSize[realDestination]
    else:
        parent[realDestination] = realSource
        tableSize[realSource]+=tableSize[realDestination]
        tableSize[realDestination] = 0
        mergedSize = tableSize[realSource]
        if rank[realDestination]==rank[realSource]:
            rank[realSource] = rank[realSource]+1

        
    #print(tableSize)
    return True,mergedSize

for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())

    res, destTableSize = merge(destination - 1, source - 1)
    ans = max(ans, destTableSize)
    print(ans)
    
