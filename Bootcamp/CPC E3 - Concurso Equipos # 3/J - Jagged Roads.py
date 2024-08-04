from heapq import heappop, heappush, heapify
from math import log


def calLog(n):
    return log(n) / log(7)

INF = int(1e9)
n, m = map(int, input().split())
AL = [[] for i in range(n+1)]
for i in range(m):
    u,v,w = map(int, input().split())
    AL[u].append((v,calLog(w)))
    AL[v].append((u, calLog(w)))


dist = [INF] * (n+1)
dist[1] = 0
pq = []
heappush(pq, (0, 1))



while pq:
    d, u = heappop(pq)
    if d > dist[u]: continue
    for v, w in AL[u]:
        if dist[u] + w >= dist[v]: continue
        dist[v] = dist[u] + w
        heappush(pq, (dist[v], v))

print(dist[n])
