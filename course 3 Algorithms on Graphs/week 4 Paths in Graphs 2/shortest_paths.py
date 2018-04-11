#Uses python3

import sys

def BellmanFord(adj, cost, s):
    dist[s] = 0
    for _ in range(n-1):
        for u in range(n):
            u_cost = cost[u]
            u_neighbors = adj[u]
            for j in range(len(u_neighbors)):
                if dist[u_neighbors[j]] > dist[u] + u_cost[j]:
                    dist[u_neighbors[j]] = dist[u] + u_cost[j]

def explore(v,adj):
    visited[v] = 1
    for u in adj[v]:
        if visited[u]==0:
            explore(u,adj)

def shortet_paths(adj, cost):
    for u in range(n):
        u_cost = cost[u]
        u_neighbors = adj[u]
        for j in range(len(u_neighbors)):
            if dist[u_neighbors[j]] > dist[u] + u_cost[j]:
                dist[u_neighbors[j]] = dist[u] + u_cost[j]
                explore(u_neighbors[j],adj)

    for i in range(n):
        if visited[i] == 1:
            dist[i] = '-'

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    s = data[0]
    s -= 1

    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]

    visited = [0]*n
    dist =[float('inf')]*n

    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)

    BellmanFord(adj, cost, s)
    shortet_paths(adj, cost)

    for each_dist in dist:
        print('*' if each_dist == float('inf') else each_dist)
