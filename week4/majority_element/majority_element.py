# Uses python3
import sys
import math

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    mid = int( (left+right)/2)
    m1 = get_majority_element(a, left, mid)
    m2 = get_majority_element(a, mid, right)
    #print(left, right, m1, m2)
    if m1==m2:
        return m1
    count1 = 0
    count2 = 0
    for i in range(left, right):
        if a[i]==m1:
            count1 = count1+1
        elif a[i]==m2:
            count2 = count2+1
    halfLen = (right-left)/2
    if count1 > halfLen:
        return m1
    elif count2 > halfLen:
        return m2
    
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
