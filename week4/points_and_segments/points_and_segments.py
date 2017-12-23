# Uses python3
import sys
import math

def binary_search(dataArr, x):
    start = 0
    end = len(dataArr)
    while start < end-1 and start < len(dataArr) and end >=0:
        #print(start, end)
        if (end-start)==2:
            if x < dataArr[start]:
                return start
            elif x > dataArr[end-1]:
                return end
            else:
                return start+1
            
        mid = math.floor( (start+end)/2)
        #print(start, end, mid)
        if dataArr[mid] <= x and dataArr[mid+1] >=x:
            return mid+1
        elif dataArr[mid] < x and dataArr[mid+1] < x:
            start = mid+1
        elif dataArr[mid] > x and dataArr[mid+1] > x:
            end = mid

    #print(start, end)
    if (end-start)==1:
        if x < dataArr[start]:
            return start
        else:
            return end
        
    if start >= len(dataArr):
        return start
    elif end <= 0:
        return 0
    

def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    #write your code here
    numSeg = len(starts)
    i = 0
    for point in points:
        left = binary_search(starts, point)
        right = binary_search(ends, point)
        #print(point, left, right)
        while left < numSeg:
            #print(left)
            if starts[left]==point:
                left+=1
            else:
                break
                
        while right > 0 and right <= numSeg:
            if ends[right-1]==point:
                right-=1
            else:
                break

        #print(point, left, right)
        right = numSeg - right
        cnt[i] = left + right - numSeg
        i+=1
    return cnt

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    SortedStarts = sorted(starts)
    SortedEnds = sorted(ends)
    #cnt = naive_count_segments(starts, ends, points)
    cnt = fast_count_segments(SortedStarts, SortedEnds, points)
    for x in cnt:
        print(x, end=' ')
