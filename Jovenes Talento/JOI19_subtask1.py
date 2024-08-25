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
abcd = "abcdefghijklmnopqrstuvwxyz"

# Algunas funciones útiles
def add(x, y, mod=MOD): return (x + y) % mod
def sub(x, y, mod=MOD): return (x - y) % mod
def mul(x, y, mod=MOD): return (x * y) % mod

# Inverso multiplicativo de a modulo m (cuando m es primo)
def invmod(a, mod=MOD): return powmod(a, mod - 2, mod)

def lcm(a, b): return a * b // gcd(a, b)

RANDOM = getrandbits(32)

class Wrapper(int):
    def __init__(self, x):
        int.__init__(x)
    def __hash__(self):
        return super(Wrapper, self).__hash__() ^ RANDOM


depth = []
parent = []
visited = []
AL = []
uf = None


class UF:
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


# Tree compression from vertex a to b
def path_compression(a, b):
    a = uf.find(a)
    b = uf.find(b)
    while a != b:
        if depth[a] < depth[b]:
            b, a = a, b
        uf.union(parent[a], a)
        a = uf.find(parent[a])


def dfs(u, lvl, p):
    global AL, visited, parent, depth, uf
    stack = [(u, lvl, p)]
    while stack:
        u, lvl, p = stack.pop()
        for v in AL[u]:
            if not visited[v]:
                stack.append((v, lvl+1, u))
        visited[u] = True
        depth[u] = lvl
        parent[u] = p
def main():
    global AL, visited, parent, depth, uf
    n, m = ints()
    edges = []
    for i in range(n-1):
        u,v = ints()
        edges.append((u, v))
    tree_groups = {}
    groups = [[] for i in range(n+1)]
    for i in range(n):
        g = int(input())
        tree_groups[i+1] = g
        groups[g].append(i+1)


    uf = UF(n+1)
    for u, v in edges:
        if tree_groups[u] == tree_groups[v]:
            uf.union(u, v)

    for g in groups:
        if len(g) != 0:
            print(uf.set_size(g[0]), len(g))



if __name__ == "__main__":
    main()
