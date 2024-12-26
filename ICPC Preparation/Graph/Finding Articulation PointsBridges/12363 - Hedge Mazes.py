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
from enum import Enum

# Para mejorar el rendimiento de la entrada/salida
input = lambda: sys.stdin.readline().strip()
flush = lambda: sys.stdout.flush()
print = lambda *args, **kwargs: sys.stdout.write(' '.join(map(str, args)) + kwargs.get("end", "\n")) and flush()

# Optimización de la recursión para Python
sys.setrecursionlimit(100000)


# Funciones para lectura de múltiples tipos de datos
def ints(): return map(int, input().split())
def strs(): return input().split()
def chars(): return list(input().strip())
def mat(n): return [list(ints()) for _ in range(n)]  # Matriz de n x m donde m es el número de enteros en una línea


# Constantes útiles
INF = float('inf')
MOD = 1000000007  # Modulo por defecto, cambiar si se necesita otro


# Algunas funciones útiles
def add(x, y, mod=MOD): return (x + y) % mod
def sub(x, y, mod=MOD): return (x - y) % mod
def mul(x, y, mod=MOD): return (x * y) % mod


# Fast power - a^b % mod
def powmod(a, b, mod=MOD):
    res = 1
    a = a % mod
    while b > 0:
        if b % 2:
            res = mul(res, a, mod)
        a = mul(a, a, mod)
        b //= 2
    return res


# Inverso multiplicativo de a modulo m (cuando m es primo)
def invmod(a, mod=MOD): return powmod(a, mod - 2, mod)


# GCD y LCM
def lcm(a, b): return a * b // gcd(a, b)


# Factorial con memoización
@lru_cache(maxsize=None)
def factorial(n): return n * factorial(n - 1) if n else 1


# Combinaciones con memoización (nCr)
@lru_cache(maxsize=None)
def comb(n, r):
    if r == 0 or r == n: return 1
    return comb(n - 1, r - 1) + comb(n - 1, r)


class flag(Enum):
  UNVISITED = -1

class DisjointSetUnion:
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

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a != b:
            if self.size[a] < self.size[b]:
                a, b = b, a

            self.num_sets -= 1
            self.parent[b] = a
            self.size[a] += self.size[b]

    def set_size(self, a):
        return self.size[self.find(a)]

    def __len__(self):
        return self.num_sets

ans = []
map1 = {}
def main():
    global ans
    global map1
    res = []
    while True:
        r, c, q = ints()
        if r == c== q == 0:
            break
        AL = [[] for _ in range(r + 1)]
        for _ in range(c):
            u, v = ints()
            AL[u].append(v)
            AL[v].append(u)
        #print(AL)
        uf = DisjointSetUnion(r+1)
        dfs_num = []
        dfs_low = []
        dfs_parent = []
        articulation_vertex = []
        dfsNumberCounter = 0
        dfsRoot = 0
        rootChildren = 0
        V = r + 1
        dfs_num = [flag.UNVISITED.value] * V
        dfs_low = [0] * V
        dfs_parent = [-1] * V
        articulation_vertex = [False] * V
        dfsNumberCounter = 0
        bridges = []
        def articulationPointAndBridge(u):
            nonlocal AL
            nonlocal dfs_num, dfs_parent, dfs_low, articulation_vertex
            nonlocal dfsNumberCounter, dfsRoot, rootChildren

            dfs_low[u] = dfs_num[u] = dfsNumberCounter
            dfsNumberCounter += 1
            for v in AL[u]:
                if dfs_num[v] == flag.UNVISITED.value:
                    dfs_parent[v] = u
                    if u == dfsRoot:
                        rootChildren += 1
                    articulationPointAndBridge(v)
                    if dfs_low[v] >= dfs_num[u]:
                        articulation_vertex[u] = True
                    if dfs_low[v] > dfs_num[u]:
                        uf.union(u, v)
                        #print(' Edge (%d, %d) is a bridge' % (u, v))
                    dfs_low[u] = min(dfs_low[u], dfs_low[v])
                elif v != dfs_parent[u]:
                    dfs_low[u] = min(dfs_low[u], dfs_num[v])
        for u in range(r+1):
            if dfs_num[u] != flag.UNVISITED:
                articulationPointAndBridge(u)
        for i in range(q):
            u,v = ints()
            if uf.find(u) == uf.find(v):
                res.append("Y")
            else: res.append("N")
        res.append("-")
    print("\n".join(res))
if __name__ == "__main__":
    main()





