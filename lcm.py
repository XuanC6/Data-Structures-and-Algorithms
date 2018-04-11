# Uses python3


def gcd(a,b):
    if a<b:
        a,b = b,a
    
    if b == 0:
        return a
    else:
        a,b = b,a%b
        return gcd(a,b)

def lcm(a, b):
    d = gcd(a,b)
    l = int(a*b//d)
    return l

a, b = map(int, input().split())
print(lcm(a, b))

