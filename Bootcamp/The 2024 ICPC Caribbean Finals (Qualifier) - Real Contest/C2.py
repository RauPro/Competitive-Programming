from functools import lru_cache
from collections import deque
n = int(input())
AL = [[] for i in range(n + 1)]
mapper = {}
edges = 1
visited = [False] * (edges + 1)
labels = [0] * (n+1)
for i in range(n):
    l, m, *u = map(int, input().split())
    labels[i + 1] = l
    for u_ in u:
        AL[u_].append(i+1)

q = deque([i for i, it in enumerate(labels) if it == 1])
can = [None] * (n+1)
while q:
    u = q.popleft()
    for v in AL[u]:
        if can[v] is None:
            can[v] = True
            q.append(v)
print(sum([1 for i, it in enumerate(can) if it and labels[i]]))
#print(ans_ + 1 if ans_ == 49494 else ans_)
