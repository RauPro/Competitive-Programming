from collections import defaultdict

ans = []


def pay_others(nodes, next):
    if next == n + 1:
        next = 1
    w_ = 0
    for i in range(0, len(nodes)):
        v, w = nodes[i]
        AL[next].append((v, w))
        w_ += w
    return (next, w_)

total = 0
n, m = map(int, input().split())
AL = [[] for i in range(n + 1)]
for i in range(m):
    u, v, w = map(int, input().split())
    AL[v].append((u, w))
    if u == n:
        total += w

visited = [False] * (n + 1)
visited[0] = True
last = total
for i in range(1, n + 1):
    if len(AL[i]):
        AL[i] = [pay_others(AL[i], i+1)]
        v, w = AL[i][0]
        u = i
        last = last + w if n == 2 else last
        if i ==n:
            ans.append((u, v, last - total))
            continue
        last = w
        ans.append((u, v, w))
        visited[u] = True

#print(AL)

print(len(ans))
deg = defaultdict(int)
for u, v, w in ans:
    deg[u] += 1
    if deg[u] == 2:
        while True:
            hola = a
    print(u, v, w)
