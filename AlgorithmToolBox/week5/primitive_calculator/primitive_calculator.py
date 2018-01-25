# Uses python3
import sys

def optimal_sequence(n):
    sequence = []
    MinNumOp = {}
    MinNumOp[0]=0
    
    for m in range(1, n+1):
        MinNumOp[m] = 1e30
        numOp1 = MinNumOp[m-1] + 1
        if numOp1 < MinNumOp[m]:
            MinNumOp[m] = numOp1
        numOp2 = 1e30
        if m%2==0:
            numOp2 = MinNumOp[m/2]+1
        if numOp2 < MinNumOp[m]:
            MinNumOp[m] = numOp2
        numOp3 = 1e30
        if m%3==0:
            numOp3 = MinNumOp[m/3] + 1
        if numOp3 < MinNumOp[m]:
            MinNumOp[m] = numOp3

    i = n
    sequence.append(n)
    while i > 1:
        #print(i)
        if MinNumOp[i-1]==MinNumOp[i]-1:
            sequence.append(i-1)
            i = i-1
            continue
        elif i%2==0 and MinNumOp[i/2]==MinNumOp[i]-1:
            i = int(i/2)
            sequence.append(i)
            continue
        elif i%3==0 and MinNumOp[i/3]==MinNumOp[i]-1:
            i = int(i/3)
            sequence.append(i)
            continue
        
    return list(reversed(sequence))

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
