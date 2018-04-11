# Uses python3

def fibonacci_sum_last_digit(n):
    
    n = n%60
    a,b = 0,1
    m = 0
    for i in range(n):
        a,b = b,(a+b)%10
        m = (m+a)%10
    return m

n = int(input())
print(fibonacci_sum_last_digit(n))