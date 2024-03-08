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

class flag(Enum):
  UNVISITED = -1

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



AL = []
dfs_num = []
dfs_low = []
dfs_parent = []
articulation_vertex = []
dfsNumberCounter = 0
dfsRoot = 0
rootChildren = 0
visited = []

def dfs(u, skip):
    global AL, visited
    visited[u] = True
    if u == skip:
        return
    for v in AL[u]:
        if visited[v]:
            continue
        dfs(v, skip)

def main():
    global AL, visited
    global dfs_num, dfs_parent, dfs_low, articulation_vertex
    global dfsNumberCounter, dfsRoot, rootChildren
    while True:
        V, m = ints()
        if V == m == 0:
            break

        AL = [[] for _ in range(V+1)]
        while True:
            u, v = ints()
            if u == v == -1:
                break
            AL[u].append(v)
            AL[v].append(u)


        #print('Articulation Points & Bridges (the input graph must be UNDIRECTED)')
        dfs_num = [flag.UNVISITED.value] * V
        dfs_low = [0] * V
        dfs_parent = [-1] * V
        articulation_vertex = [False] * V
        dfsNumberCounter = 0
        #print('Bridges:')
        for u in range(V):
            if dfs_num[u] == flag.UNVISITED.value:
                dfsRoot = u
                rootChildren = 0
                articulationPointAndBridge(u)
                articulation_vertex[dfsRoot] = (rootChildren > 1)

        #print('Articulation Points:')
        vertex = []
        for u in range(V):
            if articulation_vertex[u]:
                vertex.append(u)

        ans = 0
        visited = [0] * V
        #print(vertex)
        list_ans = []
        for v in vertex:
            for i in range(V):
                if i == v:
                    continue
                if not visited[i]:
                    dfs(i, v)
                    ans += 1
            list_ans.append((v, ans))
            visited = [0] * V
            ans = 0

        list_ans.sort(reverse = True ,key=sorting)
        acum = 0
        for a, b in list_ans:
            if acum == m:
                break
            acum+=1
            print(a,b)


        if acum < m:
            for i in range(V):
                if acum == m:
                    break
                if i in vertex:
                    continue
                acum+=1
                print(i, 1)
        print()


def sorting(e):
    a,b = e
    return b




def articulationPointAndBridge(u):
  global AL
  global dfs_num, dfs_parent, dfs_low, articulation_vertex
  global dfsNumberCounter, dfsRoot, rootChildren

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
      dfs_low[u] = min(dfs_low[u], dfs_low[v])
    elif v != dfs_parent[u]:
      dfs_low[u] = min(dfs_low[u], dfs_num[v])

if __name__ == "__main__":
    main()
