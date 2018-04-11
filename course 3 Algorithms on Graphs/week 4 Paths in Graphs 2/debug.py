#Uses python3
import random

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
    post[v][1] = clock
    clock += 1

def DFS(adj):
    for i in range(n):
        if visited[i]==0:
            explore(i,adj)

def partition2(a, l, r):
    x = a[l][1]
    j = l;
    for i in range(l + 1, r + 1):
        if a[i][1] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j

def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    j = partition2(a, l, r)
    randomized_quick_sort(a, l, j - 1);
    randomized_quick_sort(a, j + 1, r);

def explore_2(v,adj,n_scc):
    visited_2[v] = 1
    scc[n_scc].append(v)
    for u in adj[v]:
        if visited_2[u]==0:
            explore_2(u,adj,n_scc)

def strongly_connected_components(rev_adj,adj):
    DFS(rev_adj)
    randomized_quick_sort(post, 0, n-1)

    n_scc = 0
    for i in range(n):
        j = n-1-i
        index = post[j][0]
        if visited_2[index]==0:
            scc.append([])
            explore_2(index,adj,n_scc)
            n_scc += 1

def scc_process():
    for each_scc in scc:
        for i in each_scc:
            neighbors = adj[i]
            i_cost = cost[i]
            k = 0
            for each_neighbor in neighbors:
                if each_neighbor not in each_scc:
                    neighbors.pop(k)
                    i_cost.pop(k)
                k += 1
            adj[i] = neighbors
            cost[i] = i_cost



def BellmanFord(adj, cost, scc):
    dists = [None]*len(scc)
    for i in range(len(scc)):
        dists[i] = {scc[i][j]:float('inf') for j in range(len(scc[i]))}
        
        dists[i][scc[i][0]] = 0
             
        for _ in range(len(scc[i])-1):
            for u in scc[i]:
                u_cost = cost[u]
                neighbors = adj[u]
                for j in range(len(neighbors)):
                    if dists[i][neighbors[j]] > dists[i][u] + u_cost[j]:
                        dists[i][neighbors[j]] = dists[i][u] + u_cost[j]
    return dists


def negative_cycle(adj, cost):
    
    for i in range(len(scc)):
        for u in scc[i]:
            u_cost = cost[u]
            u_neighbors = adj[u]
            for j in range(len(u_neighbors)):
                if dists[i][u_neighbors[j]] > dists[i][u] + u_cost[j]:
                    return 1
    return 0


data = list(map(int, input().split()))
n, m = data[0:2]
data = data[2:]
edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
data = data[3 * m:]

adj = [[] for _ in range(n)]
rev_adj = [[] for _ in range(n)]
cost = [[] for _ in range(n)]

visited = [0]*n
visited_2 = [0]*n
clock = 1
pre = [0]*n
post = [[i,0] for i in range(n)]
scc = []

for ((a, b), w) in edges:
    adj[a - 1].append(b - 1)
    rev_adj[b-1].append(a-1)
    cost[a - 1].append(w)

strongly_connected_components(rev_adj,adj)
scc_process()

dists = BellmanFord(adj, cost, scc)
print(negative_cycle(adj, cost))
