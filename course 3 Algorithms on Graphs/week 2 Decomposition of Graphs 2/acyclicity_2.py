#Uses python3

import sys

def explore(v,adj):
    visited[v] = 1
    previsit(v)
    for u in adj[v]:
        if visited[u]==0:
            explore(u,adj)
    postvisit(v)

def previsit(v):
    global clock
    pre[v] = clock
    clock += 1

def postvisit(v):
    global clock
    post[v] = clock
    clock += 1

def DFS(adj):
    for i in range(n):
        if visited[i]==0:
            explore(i,adj)

def acyclic(rev_adj,adj):
    DFS(rev_adj)
    deleted_i = []

    while max(post)>0:
        i = post.index(max(post))
        for neighbor in adj[i]:
            if neighbor not in deleted_i:
                return 1
        post[i] = 0
        deleted_i.append(i)
    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    rev_adj = [[] for _ in range(n)]
    
    visited = [0]*n
    clock = 1
    pre = [0]*n
    post = [0]*n
    
    for (a, b) in edges:
        adj[a-1].append(b-1)
        rev_adj[b-1].append(a-1)

    print(acyclic(rev_adj,adj))
