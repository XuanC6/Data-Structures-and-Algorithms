# Uses python3


def get_fibonacci_last_digit(n):
    
    n = n%60
    a,b = 0,1
    for i in range(n):
        a,b = b,(a+b)%10
    return a

n = int(input())
print(get_fibonacci_last_digit(n))
