#Uses python3

import sys
#sys.setrecursionlimit(10**7)

def explore(v):
    visited[v] = 1
    for u in adj[v]:
        if visited[u]==0:
            explore(u)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    
    visited = [0 for _ in range(n)]
    
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    
    explore(x)
    print(1 if visited[y] else 0)
