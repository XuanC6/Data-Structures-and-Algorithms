#Uses python3

import sys
#import queue

def Dijkstra(adj, cost, s, t):
    dist = [float('inf')]*n
#    prev = [None]*n
    dist[s]=0
    H = {i:dist[i] for i in range(n)}
    while len(H)>0:
        u = min(H, key = H.get)
        H.pop(u)
        u_neighbors = adj[u]
        u_cost = cost[u]
        for i in range(len(u_neighbors)):
            if dist[u_neighbors[i]] > dist[u] + u_cost[i]:
                dist[u_neighbors[i]] = dist[u] + u_cost[i]
#                prev[neighbors[i]] = u
                H[u_neighbors[i]] = dist[u_neighbors[i]]
            
    return (-1 if dist[t] == float('inf') else dist[t])


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(Dijkstra(adj, cost, s, t))
