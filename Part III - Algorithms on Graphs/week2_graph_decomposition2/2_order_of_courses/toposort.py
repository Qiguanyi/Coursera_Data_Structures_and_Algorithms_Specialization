#Uses python3

import sys

def dfs(adj, used, order, x):
    #write your code here
    if used[x] == 0:
        for i in adj[x]:
            dfs(adj, used, order, i)
        used[x] = 1
        order.append(x)
    

def toposort(adj):
    used = [0] * len(adj)
    order = []
    #write your code here
    for i in range(len(adj)):
        dfs(adj, used, order, i)
    
    return order

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in range(n):
        print(order.pop() + 1, end=' ')

