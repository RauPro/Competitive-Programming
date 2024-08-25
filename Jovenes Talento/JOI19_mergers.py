import sys
from collections import defaultdict
from sys import setrecursionlimit, stdin, stdout

setrecursionlimit(1000000)


class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.num_sets = n

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def merge(self, a, b):
        a, b = self.find(a), self.find(b)
        self.num_sets -= 1
        self.parent[b] = a
        self.size[a] += self.size[b]

    def set_size(self, a):
        return self.size[self.find(a)]

    def __len__(self):
        return self.num_sets


def dfs(v, parent):
    stack = [(v, parent)]
    while stack:
        v, parent = stack.pop()
        for p in AL[v]:
            if p == parent:
                continue
            depth[p] = depth[v] + 1
            up[p] = v
            stack.append((p, v))


def merge(a, b):
    a = dsu.find(a)
    b = dsu.find(b)
    while a != b:
        if depth[a] < depth[b]:
            a, b = b, a
        dsu.merge(up[a], a)
        a = dsu.find(up[a])


n, k = map(int, input().split())

AL = [[] for i in range(n + 1)]
dsu = DSU(n)
up = [0] * n
depth = [0] * n

for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    AL[a].append(b)
    AL[b].append(a)

dfs(0, -1)

groups = [[] for i in range(n + 1)]
for i in range(n):
    a = int(input()) - 1
    groups[a].append(i)

for group in groups:
    for j in range(1, len(group)):
        merge(group[0], group[j])


degree = [0] * n
for u in range(n):
    for v in AL[u]:
        if dsu.find(u) != dsu.find(v):
            degree[dsu.find(u)] += 1

ans = sum([1 for it in degree if it == 1])
print((ans + 1) // 2)
