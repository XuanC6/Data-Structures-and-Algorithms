# Uses python3
import sys

def invermerge(B,C):
    D = []
    inver_num = 0
    while len(B)>0 and len(C)>0:
        b = B[0]
        c = C[0]
        if b>c:
            D.append(b)
            B.remove(b)
            inver_num +=len(C)
        else:
            D.append(c)
            C.remove(c)
    if len(B)>0:
        D.extend(B)
    elif len(C)>0:
        D.extend(C)
    return D,inver_num

def invermergesort_invernum(A):
    n = len(A)
    if n==1:
        return A,0
    mid = len(A)//2
    B, inver_num_B = invermergesort_invernum(A[0:mid])
    C, inver_num_C = invermergesort_invernum(A[mid:n])
    A_new,inver_num= invermerge(B,C)
    total_inver_num = inver_num_B+inver_num_C+inver_num
    return A_new,total_inver_num
    

#def get_number_of_inversions(a, b, left, right):
#    number_of_inversions = 0
#    if right - left <= 1:
#        return number_of_inversions
#    ave = (left + right) // 2
#    number_of_inversions += get_number_of_inversions(a, b, left, ave)
#    number_of_inversions += get_number_of_inversions(a, b, ave, right)
#    #write your code here
#    
#    return number_of_inversions

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
#    b = n * [0]
#    print(get_number_of_inversions(a, b, 0, len(a)))
    _,inver_num = invermergesort_invernum(a)
    print(inver_num)
