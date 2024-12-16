import os
import sys
from collections import *
from heapq import *
from math import gcd, floor, ceil, sqrt
from copy import deepcopy
from itertools import permutations, combinations, product
from bisect import bisect_left, bisect_right
from functools import lru_cache, reduce
import operator
from random import getrandbits
from itertools import accumulate

input = lambda: sys.stdin.readline().strip()
flush = lambda: sys.stdout.flush()
print = lambda *args, **kwargs: sys.stdout.write(' '.join(map(str, args)) + kwargs.get("end", "\n")) and flush()

sys.setrecursionlimit(100000)


def ints(): return map(int, input().split())
def strs(): return input().split()
def chars(): return list(input().strip())
def mat(n): return [list(ints()) for _ in range(n)]

INF = 10 ** 18
MOD = 1000000007
abcd = "abcdefghijklmnopqrstuvwxyz"

def add(x, y, mod=MOD): return (x + y) % mod
def sub(x, y, mod=MOD): return (x - y) % mod
def mul(x, y, mod=MOD): return (x * y) % mod

def invmod(a, mod=MOD): return powmod(a, mod - 2, mod)

def lcm(a, b): return a * b // gcd(a, b)

RANDOM = getrandbits(32)

class Wrapper(int):
    def __init__(self, x):
        int.__init__(x)
    def __hash__(self):
        return super(Wrapper, self).__hash__() ^ RANDOM

# wx = Wrapper(x)
# cnt[wx] = cnt.get(wx, 0) + 1


class Dinic:
    def __init__(self, n):
        self.lvl = [0] * n
        self.ptr = [0] * n
        self.q = [0] * n
        self.adj = [[] for _ in range(n)]

    def add_edge(self, a, b, c, rcap=0):
        self.adj[a].append([b, len(self.adj[b]), c, 0])
        self.adj[b].append([a, len(self.adj[a]) - 1, rcap, 0])

    def dfs(self, v, t, f):
        if v == t or not f:
            return f

        for i in range(self.ptr[v], len(self.adj[v])):
            e = self.adj[v][i]
            if self.lvl[e[0]] == self.lvl[v] + 1:
                p = self.dfs(e[0], t, min(f, e[2] - e[3]))
                if p:
                    self.adj[v][i][3] += p
                    self.adj[e[0]][e[1]][3] -= p
                    return p
            self.ptr[v] += 1

        return 0

    def calc(self, s, t):
        flow, self.q[0] = 0, s
        for l in range(31):  # l = 30 maybe faster for random data
            while True:
                self.lvl, self.ptr = [0] * len(self.q), [0] * len(self.q)
                qi, qe, self.lvl[s] = 0, 1, 1
                while qi < qe and not self.lvl[t]:
                    v = self.q[qi]
                    qi += 1
                    for e in self.adj[v]:
                        if not self.lvl[e[0]] and (e[2] - e[3]) >> (30 - l):
                            self.q[qe] = e[0]
                            qe += 1
                            self.lvl[e[0]] = self.lvl[v] + 1

                p = self.dfs(s, t, INF)
                while p:
                    flow += p
                    p = self.dfs(s, t, INF)

                if not self.lvl[t]:
                    break

        return flow


def main():
    N, M = ints()
    edges = []
    for _ in range(M):
        u, v = ints()
        edges.append((u, v))
    c = list(ints())
    total = 2 * N + 1
    dinic = Dinic(total)
    for i in range(2, N):
        dinic.add_edge(i, i + N, c[i - 1])
    for a, b in edges:
        a_node = a if a in (1, N) else a + N
        b_node = b if b in (1, N) else b + N
        dinic.add_edge(a_node, b, INF)
        dinic.add_edge(b_node, a, INF)

    source = 1
    sink = N
    flow = dinic.calc(source, sink)
    visited = [False] * (total)
    q = deque()
    q.append(source)
    visited[source] = True
    while q:
        v = q.popleft()
        for e in dinic.adj[v]:
            if e[2] > e[3] and not visited[e[0]]:
                visited[e[0]] = True
                q.append(e[0])

    separators = []
    total_cost = 0
    for i in range(2, N):
        i_in = i
        i_out = i + N
        if visited[i_in] and not visited[i_out]:
            separators.append(i)
            total_cost += c[i - 1]
    print(total_cost, flow)
    print(len(separators))
    print(' '.join(map(str, sorted(separators))))

if __name__ == "__main__":
    main()
