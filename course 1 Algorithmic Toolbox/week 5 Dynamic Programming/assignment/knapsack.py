# Uses python3
import sys

def optimal_weight(W, w):
    # write your code here
    n = len(w)
#    optimal_solution = [0]*n
    
    value = [[0]*(n+1) for i in range(W+1)]
    
    for i in range(1,n+1):
        for weight in range(1,W+1):
            value[weight][i] = value[weight][i-1]
            if w[i-1]<=weight:
                new_value = value[weight-w[i-1]][i-1]+w[i-1]
                if new_value>value[weight][i]:
                    value[weight][i]=new_value
    
    return value[W][n]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
