#Uses python3

import sys
import random
sys.setrecursionlimit(200000)

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

def explore_2(v,adj):
    visited_2[v] = 1
    for u in adj[v]:
        if visited_2[u]==0:
            explore_2(u,adj)

def number_of_strongly_connected_components(rev_adj,adj):
    DFS(rev_adj)
    randomized_quick_sort(post, 0, n-1)
    result = 0
    
    for i in range(n):
        j = n-1-i
        index = post[j][0]
        if visited_2[index]==0:
            explore_2(index,adj)
            result += 1

    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    rev_adj = [[] for _ in range(n)]
    
    visited = [0]*n
    visited_2 = [0]*n
    clock = 1
    pre = [0]*n
    post = [[i,0] for i in range(n)]
    
    for (a, b) in edges:
        adj[a-1].append(b-1)
        rev_adj[b-1].append(a-1)

    print(number_of_strongly_connected_components(rev_adj,adj))
