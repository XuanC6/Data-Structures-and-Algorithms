# Uses python3
import sys

def optimal_sequence(n):
    seq_pre_num = [0]*(n+1)
    MinNum=[0]*(n+1)
    for num in range(2,n+1):
        min_sel = []
        prenums = []
        if num%2==0:
            min_sel.append(MinNum[num//2]+1)
            prenums.append(num//2)
        if num%3==0:
            min_sel.append(MinNum[num//3]+1)
            prenums.append(num//3)
        min_sel.append(MinNum[num-1]+1)
        prenums.append(num-1)
        
        min_val = min(min_sel)
        k = min_sel.index(min_val)
        seq_pre_num[num] = (prenums[k])
        MinNum[num] = min(min_sel)
        
    sequence = [n]
    t = n
    while t>1:
        t = seq_pre_num[sequence[-1]]
        sequence.append(t)
    
    sequence.reverse()
    return sequence


input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
