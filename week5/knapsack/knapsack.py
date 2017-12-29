# Uses python3
import sys
#import numpy

def optimal_weight(W, w):
    # write your code here
    result = 0
    n = len(w)
    #value = numpy.zeros((W+1, n+1))
    value = [[0 for x in range(n+1)] for y in range(W+1)]
    #print(value)
    
    for i in range(0,n+1):
        value[0][i] = 0
    for i in range(0, W+1):
       value[i][0] = 0

    for i in range(1, n+1):
        for g in range(1, W+1):
            value[g][i] = value[g][i-1]
            currentW = w[i-1]
            if currentW <= g:
                val = value[g-currentW][ i-1] + currentW
                if value[g][i] < val:
                    value[g][i] = val
    #print(value)
    return value[W][n]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
