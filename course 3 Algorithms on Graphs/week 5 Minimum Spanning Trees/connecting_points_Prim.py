#Uses python3
import sys
import math

def minimum_distance_Prim(adj, weight):
    cost = [float('inf')]*n
    prev = [None]*n
    cost[0]=0

    H = {i:cost[i] for i in range(n)}

    while len(H)>0:
        u = min(H, key = H.get)
        H.pop(u)
        u_neighbors = adj[u]
        u_weight = weight[u]
        for i in range(len(u_neighbors)):
            if (u_neighbors[i] in H) and cost[u_neighbors[i]] > u_weight[i]:
                cost[u_neighbors[i]] = u_weight[i]
                H[u_neighbors[i]] = cost[u_neighbors[i]]
                prev[u_neighbors[i]] = u
            
    return sum(cost)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    adj = [[] for _ in range(n)]
    weight = [[] for _ in range(n)]

    for i in range(n):
        for j in range(i+1,n):
            adj[i].append(j)
            adj[j].append(i)
            dis = math.sqrt((x[i]-x[j])**2+(y[i]-y[j])**2)
            weight[i].append(dis)
            weight[j].append(dis)
    
    print("{0:.9f}".format(minimum_distance_Prim(adj, weight)))
