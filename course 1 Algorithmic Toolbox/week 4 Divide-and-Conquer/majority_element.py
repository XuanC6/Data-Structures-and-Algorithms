# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    mid = left + (right-1-left)//2
    count = 0
    for i in range(left,right):
        if a[i]==a[mid]:
            count+=1
    if count>(right-left)//2:
        return a[mid]
    else:
        b1 = get_majority_element(a, left, mid)
        b2 = get_majority_element(a, mid+1, right)
        count1 = 0
        count2 = 0
        for i in range(left,right):
            if a[i]==b1:
                count1+=1
            elif a[i]==b2:
                count2+=1
        if count1>(right-left)//2:
            return b1
        elif count2>(right-left)//2:
            return b2
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
