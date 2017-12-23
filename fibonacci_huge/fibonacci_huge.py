# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

def get_fibonacci_huge_fast(n,m):
    
    previousRes = 0
    currentRes  = 1

    RemainderList = [0,1]
    while True:
        previousRes, currentRes = currentRes, (previousRes + currentRes)%m
        RemainderList.append(currentRes)
        compareList = RemainderList[-3:]
        if len(RemainderList) > 3 and compareList==[0, 1, 1]:
            del RemainderList[-3:]            
            break
        
    if m == 1:
        period = 1
    else:
        period = len(RemainderList)

    #print(period)
    return RemainderList[ n%period ]
    
    
if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    # print(get_fibonacci_huge_naive(n, m))
    print(get_fibonacci_huge_fast(n,m))
