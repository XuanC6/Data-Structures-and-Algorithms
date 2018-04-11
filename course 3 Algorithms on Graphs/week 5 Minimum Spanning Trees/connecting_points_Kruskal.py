#Uses python3
import sys
import math

def find(u):
    global parent
    # find parent and compress path
    if u != parent[u]:
        parent[u] = find(parent[u])
    return parent[u]

def union(u, v):
    global rank
    u_parent, v_parent = find(u), find(v)

    if u_parent == v_parent:
        return
    if rank[u_parent] >= rank[v_parent]:
        parent[v_parent] = u_parent
        if rank[u_parent]==rank[v_parent]:
            rank[u_parent]+=1
    if rank[u_parent] < rank[v_parent]:
        parent[u_parent] = v_parent


def minimum_distance_Kruskal(edges):
    edges = sorted(edges,key = lambda x:x[1])
    costs = []
    for (u,v),w in edges:
        if find(u)!=find(v):
            costs.append(w)
            union(u,v)
    
    return sum(costs)



if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]

    rank = [1] * n
    parent = list(range(n))

    adj = [[] for _ in range(n)]
    weight = [[] for _ in range(n)]

    def creat_edges(x,y):
        for i in range(n):
            for j in range(i+1,n):
                dis = math.sqrt((x[i]-x[j])**2+(y[i]-y[j])**2)
                yield ((i,j),dis)
    
    edges = list(creat_edges(x,y))
    
    print("{0:.9f}".format(minimum_distance_Kruskal(edges)))
