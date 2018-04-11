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
    post[v][1] = clock
    clock += 1

def DFS(adj):
    for i in range(n):
        if visited[i]==0:
            explore(i,adj)

def explore_2(v,adj,n_scc):
    visited_2[v] = 1
    scc[n_scc].append(v)
    for u in adj[v]:
        if visited_2[u]==0:
            explore_2(u,adj,n_scc)

def strongly_connected_components(rev_adj,adj):
    global post
    DFS(rev_adj)
    post = sorted(post,key = lambda x:x[1])

    n_scc = 0
    for i in range(n):
        j = n-1-i
        index = post[j][0]
        if visited_2[index]==0:
            scc.append([])
            explore_2(index,adj,n_scc)
            n_scc += 1

def scc_process():
    global adj,cost
    for each_scc in scc:
        for i in each_scc:
            neighbors2 = adj[i].copy()
            i_cost2 = cost[i].copy()
            k = 0
            for each_neighbor in adj[i]:
                if each_neighbor not in each_scc:
                    neighbors2.pop(k)
                    i_cost2.pop(k)
                    continue
                k += 1
            adj[i] = neighbors2.copy()
            cost[i] = i_cost2.copy()
            del(neighbors2)
            del(i_cost2)


def BellmanFord(adj,cost,scc):
    dists = [None]*len(scc)
    for i in range(len(scc)):
        dists[i] = {scc[i][j]:float('inf') for j in range(len(scc[i]))}
        
        dists[i][scc[i][0]] = 0
             
        for _ in range(len(scc[i])-1):
            for u in scc[i]:
                u_cost = cost[u]
                u_neighbors = adj[u]
                for j in range(len(u_neighbors)):
                    if dists[i][u_neighbors[j]] > dists[i][u] + u_cost[j]:
                        dists[i][u_neighbors[j]] = dists[i][u] + u_cost[j]
    return dists


def negative_cycle(adj,cost,scc):
    for i in range(len(scc)):
        if len(scc[i])>1:
            for u in scc[i]:
                u_cost = cost[u]
                u_neighbors = adj[u]
                for j in range(len(u_neighbors)):
                    if dists[i][u_neighbors[j]] > dists[i][u] + u_cost[j]:
                        return 1
    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
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

    dists = BellmanFord(adj,cost,scc)
    print(negative_cycle(adj,cost,scc))
