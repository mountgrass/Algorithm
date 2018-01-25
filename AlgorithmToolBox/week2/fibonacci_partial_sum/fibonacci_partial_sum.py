# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

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

def fibonacci_partial_sum_fast(from_, to):
    sumLDTo = fibonacci_sum_fast(to)
    if from_ >=1:
        sumLDFrom = fibonacci_sum_fast(from_-1)
    else:
        sumLDFrom = 0
        
    return (sumLDTo - sumLDFrom)%10
        
if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    #print(fibonacci_partial_sum_naive(from_, to))
    print(fibonacci_partial_sum_fast(from_, to))
