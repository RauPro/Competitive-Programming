import sys
import heapq
input = lambda: sys.stdin.readline().rstrip("\r\n")
flush = lambda: sys.stdout.flush()
print = lambda *args, **kwargs: sys.stdout.write(' '.join(map(str, args)) + kwargs.get("end", "\n")) and flush()
def ints(): return map(int, input().split())
def strs(): return input().split()
def chars(): return list(input().strip())
def mat(n): return [list(ints()) for _ in range(n)]



def main():
    n, m = ints()
    AL = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = ints()
        AL[u].append((v, w))
        AL[v].append((u, w))
    dist = [int(10e18)] * (n + 1)
    prev = [-1] * (n + 1)
    dist[1] = 0
    pq = [(0, 1)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]: continue
        for v, w in AL[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u
                heapq.heappush(pq, (dist[v], v))
    path = []
    curr = n
    while curr != -1:
        path.append(curr)
        curr = prev[curr]
    print(*path[::-1])
if __name__ == "__main__":
    main()