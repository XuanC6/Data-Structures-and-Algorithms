# Uses python3


def fibonacci_sum_last_digit(n):
    
    n = n%60
    a,b = 0,1
    p = 0
    for i in range(n):
        a,b = b,(a+b)%10
        p = (p+a)%10
    return p


def fibonacci_partial_sum_last_digit(m,n):

    assert m>=0 and m<=n
    n = n%60
    m = m%60

    if m != 0:
        q = (-fibonacci_sum_last_digit(m-1))%10
    q = (q+fibonacci_sum_last_digit(n))%10
    
    return q

m, n = map(int, input().split())
print(fibonacci_partial_sum_last_digit(m, n))