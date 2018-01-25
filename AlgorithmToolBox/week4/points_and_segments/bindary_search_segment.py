# Uses python3
import sys
import math

def binary_search(dataArr, x):
    start = 0
    end = len(dataArr)
    while start < end-1 and start < len(dataArr) and end >=0:
        print(start, end)
        if (end-start)==2:
            if x < dataArr[start]:
                return start
            elif x > dataArr[end-1]:
                return end
            else:
                return start+1
            
        mid = math.floor( (start+end)/2)
        print(mid)
        if dataArr[mid] <= x and dataArr[mid+1] >=x:
            return mid+1
        elif dataArr[mid] < x and dataArr[mid+1] < x:
            start = mid+1
        elif dataArr[mid] > x and dataArr[mid+1] > x:
            end = mid-1

    print(start, end)
    
    if start >= len(dataArr):
        return start
    elif end < 0:
        return 0
    
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    data=a[0:-1]
    x = a[-1]
    index = binary_search(data, x)
    print(index)
