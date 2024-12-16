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


INF = float('inf')
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
def _u(i, j, m):
    return f'u_{i}_{j}'


def _v(i, j, m):
    return f'v_{i}_{j}'


INF = 10 ** 18


class min_cost_max_flow:
    def __init__(self, V):
        self.V = V
        self.EL = []
        self.AL = [list() for _ in range(V)]
        self.vis = [False] * V
        self.total_cost = 0
        self.d = None
        self.last = None

    def SPFA(self, s, t):
        self.d = [INF] * self.V
        self.d[s] = 0
        self.vis[s] = True
        q = [s]
        while len(q) != 0:
            u = q[0]
            q.pop(0)
            self.vis[u] = False
            for idx in self.AL[u]:
                v, cap, flow, cost = self.EL[idx]
                if cap - flow > 0 and self.d[v] > self.d[u] + cost:
                    self.d[v] = self.d[u] + cost
                    if not self.vis[v]:
                        q.append(v)
                        self.vis[v] = True
        return self.d[t] != INF

    def DFS(self, u, t, f=INF):
        if u == t or f == 0:
            return f
        self.vis[u] = True
        for i in range(self.last[u], len(self.AL[u])):
            v, cap, flow, cost = self.EL[self.AL[u][i]]
            if not self.vis[v] and self.d[v] == self.d[u] + cost:
                pushed = self.DFS(v, t, min(f, cap - flow))
                if pushed != 0:
                    self.total_cost += pushed * cost
                    flow += pushed
                    self.EL[self.AL[u][i]][2] = flow
                    rv, rcap, rflow, rcost = self.EL[self.AL[u][i] ^ 1]
                    rflow -= pushed
                    self.EL[self.AL[u][i] ^ 1][2] = rflow
                    self.vis[u] = False
                    self.last[u] = i
                    return pushed
        self.vis[u] = False
        return 0

    def add_edge(self, u, v, w, c, directed=True):
        if u == v:
            return
        self.EL.append([v, w, 0, c])
        self.AL[u].append(len(self.EL) - 1)
        self.EL.append([u, 0 if directed else w, 0, -c])
        self.AL[v].append(len(self.EL) - 1)

    def mcmf(self, s, t):
        mf = 0
        while self.SPFA(s, t):
            self.last = [0] * self.V
            f = self.DFS(s, t)
            while f != 0:
                mf += f
                f = self.DFS(s, t)
        return mf, self.total_cost


def main():
    t = int(input())
    for _ in range(t):
        input()
        n, m = ints()
        mx = [list(ints()) for i in range(n)]
        V = 2 * n * m
        mapper = {}
        total = 0
        for i in range(n):
            for j in range(m):
                mapper[_u(i, j, m)] = total
                total += 1
                mapper[_v(i, j, m)] = total
                total += 1
        mcmf = min_cost_max_flow(V)
        for i in range(n):
            for j in range(m):
                node_in = mapper[_u(i, j, m)]
                node_out = mapper[_v(i, j, m)]
                capacity = 2 if (i == 0 and j == 0) or (i == n - 1 and j == m - 1) else 1
                cost = -mx[i][j]
                mcmf.add_edge(node_in, node_out, capacity, cost)
        for i in range(n):
            for j in range(m):
                node_out = mapper[_v(i, j, m)]

                if j < m - 1:
                    right_in = mapper[_u(i, j + 1, m)]
                    mcmf.add_edge(node_out, right_in, 1, 0)
                if i < n - 1:
                    down_in = mapper[_u(i + 1, j, m)]
                    mcmf.add_edge(node_out, down_in, 1, 0)
        source = mapper[_u(0, 0, m)]
        sink = mapper[_v(n - 1, m - 1, m)]
        flow, cost = mcmf.mcmf(source, sink)
        print(f"Case {_ + 1}: {-cost - mx[0][0] - mx[n - 1][m - 1]}")


if __name__ == "__main__":
    main()
