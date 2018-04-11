# Uses python3

def get_change(m):
    n = 0
    coin = [10,5,1]
    for i in range(3):
        if m==0:
            return n
        ni = m//coin[i]
        n = n+ni
        m = m%coin[i]
    return n


m = int(input())
print(get_change(m))
