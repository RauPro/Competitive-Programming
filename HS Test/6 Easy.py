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


def tiene_conexion_directa(grafo, nodo):
    # BFS para encontrar los hijos del hijo
    for vecino in grafo[nodo]:
        for nieto in grafo[vecino]:
            if nodo in grafo[nieto]:
                return True
    return False



if __name__ == "__main__":
    n, m = ints()
    AL = [[] for i in range(n+1)]
    existing_roads = set()
    for _ in range(m):
        u, v = ints()
        AL[u].append(v)
        AL[v].append(u)
        existing_roads.add((min(u, v), max(u, v)))


    for i in range(1, n+1):
        print(tiene_conexion_directa(AL, i))
    def bfs(s, visited):
        queue = deque([s])
        nodes = []
        while queue:
            node = queue.popleft()
            if not visited[node]:
                visited[node] = True
                nodes.append(node)
                for neighbor in AL[node]:
                    if not visited[neighbor]:
                        queue.append(neighbor)
        return nodes


    visited = [False] * (n + 1)
    ccs = []

    # Buscando todos los ccs
    for i in range(1, n + 1):
        if not visited[i]:
            cc = bfs(i, visited)
            ccs.append(cc)

    ans = 0
    for cc in ccs:
        for i in range(len(cc)):
            for j in range(i + 1, len(cc)):
                a, b = cc[i], cc[j]
                if (a, b) not in existing_roads and (b, a) not in existing_roads:
                    ans += 1

    print(ans)
