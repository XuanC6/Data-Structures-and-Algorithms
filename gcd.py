# Uses python3

def gcd(a, b):
    if a<b:
        a,b = b,a
    
    if b == 0:
        return a
    else:
        a,b = b,a%b
        return gcd(a,b)


a, b = map(int, input().split())
print(gcd(a, b))
