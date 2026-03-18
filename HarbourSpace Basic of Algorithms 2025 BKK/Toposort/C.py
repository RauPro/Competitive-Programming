import sys
from types import GeneratorType
from collections import deque
input = lambda: sys.stdin.readline().rstrip("\r\n")
flush = lambda: sys.stdout.flush()
print = lambda *args, **kwargs: sys.stdout.write(' '.join(map(str, args)) + kwargs.get("end", "\n")) and flush()
def ints(): return map(int, input().split())
def strs(): return input().split()
def chars(): return list(input().strip())
def mat(n): return [list(ints()) for _ in range(n)]

def main():
    n, m = ints()
    edges = []
    fake = 0
    for _ in range(m):
        u, v, w = ints()
        edges.append((u, v, w))
        fake += w - 1
    s, t = ints()
    total = n + fake
    AL = [[] for _ in range(total + 1)]
    d = n + 1
    for u, v, w in edges:
        if w == 1:
            AL[u].append(v)
        else:
            prev = u
            for _ in range(w - 1):
                AL[prev].append(d)
                prev, d = d, d + 1
            AL[prev].append(v)
    dist, parent = [-1] * (total + 1), [-1] * (total + 1)
    q = deque([s])
    dist[s] = 0
    while q:
        u = q.popleft()
        if u == t: break
        for v in AL[u]:
            if dist[v] == -1:
                dist[v], parent[v] = dist[u] + 1, u
                q.append(v)
    if dist[t] == -1:
        print(-1)
        return
    path = []
    cur = t
    while cur != -1:
        path.append(cur)
        cur = parent[cur]
    print(*[x for x in reversed(path) if x <= n])

if __name__ == "__main__":
    main()
