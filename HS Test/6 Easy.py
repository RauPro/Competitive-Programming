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


counter_nodes = 0
counter_degree = 0
visited = []
AL = []


def dfs(u):
    global counter_nodes, counter_degree, visited
    visited[u] = True
    counter_nodes += 1
    for v in AL[u]:
        counter_degree += 1
        if not visited[v]:
            dfs(v)


n, m = ints()
AL = [[] for i in range(n + 1)]
for _ in range(m):
    u, v = ints()
    AL[u].append(v)
    AL[v].append(u)

ans = 0
counter_nodes = 0
counter_degree = 0
visited = [False] * (n+1)
for u in range(1, n + 1):
    if not visited[u]:
        dfs(u)
        ans += (((counter_nodes * (counter_nodes - 1)) // 2) - (counter_degree // 2))
        counter_nodes = 0
        counter_degree = 0

print(ans)