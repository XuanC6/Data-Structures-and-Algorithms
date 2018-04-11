#Uses python3

import sys

def largest_number(a):
    #write your code here
    res = ""
    n = len(a)
    max_len = max(list(map(len,a)))
    
    first_digits = list(map(lambda x:int(x[0]),a))
    same_first_index = []
    indexi = []
    
    for i in range(n):
        max_first = max(first_digits)
        j = first_digits.index(max_first)
        indexi.append[j]
        first_digits.pop(j)
        first_digits.insert(j,-1)
        indexi.append(j)
        if max(first_digits)!=max_first:
            same_first_index.append[indexi]

    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
