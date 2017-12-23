# Uses python3
import sys
import time

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10

def fibonacci_sum_fast(n):
    if n <= 1:
        return n

    previousLD = 0
    currentLD  = 1
    period = 60
    LDList = [0, 1]
    
    for _ in range(period-1):
        previousLD, currentLD = currentLD, (previousLD + currentLD)%10
        LDList.append(currentLD)

    sumLD = 0
    FN2 = LDList[(n+2)%period]
    sumLD = (FN2-1)%10
        
    return sumLD
    
if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    #start = time.time()
    print(fibonacci_sum_fast(n))
    #end = time.time()
    #print( end - start)
