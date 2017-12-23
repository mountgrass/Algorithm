# Uses python3
import sys

def mergeSort(a,b, left, ave, right): 
    i = left
    j = ave
    k = left
    numberInversion = 0
    while i < ave and j < right:
        if a[i] <= a[j]:
            b[k] = a[i]
            i+=1
            k+=1
        else:
            b[k] = a[j]
            j+=1
            k+=1
            numberInversion+=(ave-i)
    if i==ave:
         while j < right:
             b[k] = a[j]
             k+=1
             j+=1
    elif j==right:
          while i < ave:
             b[k] = a[i]
             k+=1
             i+=1
    for t in range(left, right):
         a[t] = b[t]

    return numberInversion
    
def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)
    #write your code here
    number_of_inversions += mergeSort(a,b,left, ave, right)
    
    #print(a,b, left, ave, right, number_of_inversions)
    return number_of_inversions

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)))
