# Uses python3
import sys

def optimal_summands(n):
    summands = []
    
    i = 1
    
    while True:
        if n>(2*i):
            summands.append(i)
            n = n-i
            i += 1
        else:
            summands.append(n)
            break
    
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
