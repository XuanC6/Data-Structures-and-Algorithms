# Uses python3

def get_fibonacci_huge(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


n, m = map(int, input().split())
print(get_fibonacci_huge(n, m))
