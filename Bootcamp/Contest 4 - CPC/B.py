from heapq import heappush, heappop
import sys
INF = int(1e10)

input = lambda: sys.stdin.readline().strip()
flush = lambda: sys.stdout.flush()
print = lambda *args, **kwargs: sys.stdout.write(' '.join(map(str, args)) + kwargs.get("end", "\n")) and flush()

def can(AL, V, limit, T):
    s = 1
    dist = [INF for u in range(V+1)]
    dist[s] = 0
    pq = []
    heappush(pq, (0, s))

    while (len(pq) > 0):
        d, u = heappop(pq)
        if (d > dist[u]): continue
        for v, w in AL[u]:
            if (dist[u] + w >= dist[v] or w < limit or dist[u] + w > T): continue
            dist[v] = dist[u] + w
            heappush(pq, (dist[v], v))
    return dist[V] != INF

n, m, t = map(int, input().split())
AL = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    AL[u].append((v, w))
    AL[v].append((u, w))


lo, hi = 0, int(1e9)
ans = -1
while lo <= hi:
    mid = (lo + hi) // 2
    if can(AL, n, mid, t):
        lo = mid + 1
        ans = mid
    else:
        hi = mid - 1


#print(hi)
#print(dist)
print(ans if ans != -1 else "He is taking an uber.")