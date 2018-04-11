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

def shift_down(i,n):
    global post
    max_index = i
    
    left_child_i = 2*i+1
    if left_child_i<n and post[left_child_i][1]>post[max_index][1]:
        max_index = left_child_i
    
    right_child_i = 2*i+2
    if right_child_i<n and post[right_child_i][1]>post[max_index][1]:
        max_index = right_child_i
    
    if i != max_index:
        post[i],post[max_index] = post[max_index],post[i]
        shift_down(max_index,n)

def build_heap(n):
    for i in range(((n-1)//2)+1):
        j = (n-1)//2 -i
        shift_down(j,n)

def heap_sort(n):
    global post
    size = n
    for i in range(n-1):
        post[0], post[size-1] = post[size-1],post[0]
        size -= 1
        shift_down(0,size)
        

def toposort(adj,n):
    DFS(adj)
    build_heap(n)
    heap_sort(n)
    for i in range(n):
        j = n-1-i
        index = post[j][0]
        yield index


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    
    visited = [0]*n
    clock = 1
    pre = [0]*n
    post = [[i,0] for i in range(n)]

    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj,n)
    for x in order:
        print(x + 1, end=' ')

