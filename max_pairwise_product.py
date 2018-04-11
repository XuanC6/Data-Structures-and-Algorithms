# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

a1 = max(a)
a.remove(a1)
a2 = max(a)

result = a1*a2

print(result)
