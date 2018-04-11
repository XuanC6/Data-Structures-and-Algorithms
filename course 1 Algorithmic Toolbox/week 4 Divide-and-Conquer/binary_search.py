# Uses python3
import sys

def binary_search(a,left,right,x):

    if left>=right:
        return -1
    mid = left+(right-1-left)//2
    if x==a[mid]:
        return mid
    elif x>a[mid]:
        left = mid +1
    else:
        right = mid
    return binary_search(a,left,right,x)

#def linear_search(a, x):
#    for i in range(len(a)):
#        if a[i] == x:
#            return i
#    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a,0,n,x), end = ' ')
