import sys
from collections import deque, defaultdict

# import psutil

input = lambda: sys.stdin.readline().strip()
flush = lambda: sys.stdout.flush()
print = lambda *args, **kwargs: sys.stdout.write(' '.join(map(str, args)) + kwargs.get("end", "\n")) and flush()

sys.setrecursionlimit(100000)
parent = []
AL = []

def ints(): return map(int, input().split())


"""def check_memory(location):
    process = psutil.Process()
    memory_info = process.memory_info()
    memory_usage = memory_info.rss / (1024 * 1024)  # Convert to MB
    print(f"Memory usage at {location}: {memory_usage:.2f} MB")"""


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.size = [1] * n

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b:
            return
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.parent[b] = a
        self.size[a] += self.size[b]


def dfs(u, p):
    stack = [(u, p)]
    parent[u] = p
    while stack:
        u, p = stack.pop()
        for v in AL[u]:
            if v not in parent:
                parent[v] = u
                stack.append((v, u))


def main():
    n, m = ints()
    solve(n, m)


def solve(n, m):
    global parent, AL
    movies = [[] for _ in range(m)]
    for i in range(n):
        _, *actors = map(int, input().split())
        for actor in actors:
            movies[actor - 1].append(i)
    uf = UnionFind(n)
    AL = [[] for _ in range(n)]
    movie = [[-1] * n for _ in range(n)]
    for i in range(m):
        if movies[i]:
            for j in range(1, len(movies[i])):
                a, b = movies[i][j], movies[i][0]
                if uf.find(a) != uf.find(b):
                    uf.union(a, b)
                    AL[a].append(b)
                    AL[b].append(a)
                    movie[b][a] = movie[a][b] = i
    parent = [-1] * n
    q = int(input())
    ans = []
    for i in range(q):
        start, end = ints()
        start-=1
        end-=1
        if not movies[start] or not movies[end] or uf.find(movies[start][0]) != uf.find(movies[end][0]):
            ans.append(str(-1))
        else:
            parent = [-1] * n
            dfs(movies[start][0], movies[start][0])
            u = movies[end][0]
            path = []
            while u != movies[start][0]:
                path.append(u)
                u = parent[u]
            path.append(movies[start][0])
            path.reverse()
            ans.append(str((3 + 2 * (len(path) - 1) + 1) // 2))
            aux = []
            aux.append(str(start + 1))
            aux.append(str(path[0] + 1))
            for i in range(1, len(path)):
                aux.append(str(movie[path[i - 1]][path[i]] + 1))
                aux.append(str(path[i] + 1))
            aux.append(str(end + 1))
            ans.append(" ".join(aux))
    print("\n".join(ans))
if __name__ == "__main__":
    main()
