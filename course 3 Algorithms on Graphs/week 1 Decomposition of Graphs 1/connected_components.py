#Uses python3

import sys

def explore(v,c):
    visited[v] = c
    for u in adj[v]:
        if visited[u]==0:
            explore(u,c)


def number_of_components():
    c = 1
    for i in range(n):
        if visited[i]==0:
            explore(i,c)
            c += 1
    return len(set(visited))

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    visited = [0 for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(number_of_components())
