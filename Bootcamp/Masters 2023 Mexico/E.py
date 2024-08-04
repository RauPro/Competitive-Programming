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

visited = []
def dfs(u, AL):
    global visited
    visited[u] = True
    for (v,w) in AL[u]:
        if not visited[v]:
            dfs(v, AL)
def main():
    global visited
    V, E, S, D = ints()
    AL = [[] for i in range(V+1)]
    raw = []
    for i in range(E):
        u, v, w = ints()
        raw.append((u,v,w))
    profit = list(ints())
    for u, v, w in raw:
        w -= profit[v-1]
        AL[u].append((v, w))

    dist = [INF] * (V+1)
    dist[S] = 0
    for i in range(V):
        modified = False
        for u in range(V+1):
            if dist[u] != INF:
                for v, w in AL[u]:
                    if dist[u] + w >= dist[v]:
                        continue
                    dist[v] = dist[u] + w
    negative = []
    hasNegativeCycle = False
    for u in range(V+1):
        if dist[u] != INF:
            for (v,w) in AL[u]:
                if dist[v] > dist[u] + w:
                    hasNegativeCycle = True
                    negative.append(u)
    #print(negative)
    visited = [False] * (V + 1)
    for u in negative:
        dfs(u, AL)
    #print(visited)
    if hasNegativeCycle and visited[D]:
        print("Money hack!")
    else:
        print(dist[D]*-1 if dist[D] != INF else "Bad trip")



if __name__ == "__main__":
    main()
