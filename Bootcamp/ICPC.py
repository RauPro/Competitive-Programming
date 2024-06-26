import os
import sys
from collections import *
import heapq
from math import gcd, floor, ceil, sqrt
from copy import deepcopy
from itertools import permutations, combinations, product
from bisect import bisect_left, bisect_right
from functools import lru_cache, reduce, cmp_to_key
import operator

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


n = 0
AL, mapper, mapper2 = [], defaultdict(lambda : []), {}
def BFS(u):
    global AL, mapper, mapper2
    for v in mapper[u]:
        if v not in mapper2:
            continue
        if AL[mapper2[v]][0] != 0:
            AL[mapper2[v]][0] += 1

def can(x, y):
    return (x >= 0 and x < n) and (y >= 0 and y < n)


dx = [-2, -1, 2, 1, -2, 1, 2, -1]
dy = [-1, -2, -1, -2, 1, 2, 1, 2]


def comparator(a,b):
    return a if len(a) < len(b) else b
def hopcroft_karp(graph, n, m):
    """
    Maximum bipartite matching using Hopcroft-Karp algorithm, running in O(|E| sqrt(|V|))
    """
    assert (n == len(graph))
    match1 = [-1] * n
    match2 = [-1] * m

    # Find a greedy match for possible speed up
    for node in range(n):
        for nei in graph[node]:
            if match2[nei] == -1:
                match1[node] = nei
                match2[nei] = node
                break
    while 1:
        bfs = [node for node in range(n) if match1[node] == -1]
        depth = [-1] * n
        for node in bfs:
            depth[node] = 0

        for node in bfs:
            for nei in graph[node]:
                next_node = match2[nei]
                if next_node == -1:
                    break
                if depth[next_node] == -1:
                    depth[next_node] = depth[node] + 1
                    bfs.append(next_node)
            else:
                continue
            break
        else:
            break

        pointer = [len(c) for c in graph]
        dfs = [node for node in range(n) if depth[node] == 0]
        while dfs:
            node = dfs[-1]
            while pointer[node]:
                pointer[node] -= 1
                nei = graph[node][pointer[node]]
                next_node = match2[nei]
                if next_node == -1:
                    # Augmenting path found
                    while nei != -1:
                        node = dfs.pop()
                        match2[nei], match1[node], nei = node, nei, match1[node]
                    break
                elif depth[node] + 1 == depth[next_node]:
                    dfs.append(next_node)
                    break
            else:
                dfs.pop()
    return match1, match2

def main():
    global n, AL, mapper, mapper2
    n, k = ints()
    p = []
    mx = [[0 for i in range(n)] for j in range(n)]
    for i in range(1, k + 1):
        x, y = ints()
        x -= 1
        y -= 1
        mx[x][y] = i
        p.append((x, y))
    AL = [[] for i in range(k+1)]
    #print(mx)
    for x, y in p:
        for i in range(8):
            next_x, next_y = x + dx[i], y + dy[i]
            if can(next_x, next_y) and mx[next_x][next_y]:
                #print("Caballo", x, y, "Atacando:", next_x, next_y, mx[next_x][next_y])
                AL[mx[x][y]].append(mx[next_x][next_y])
    print(AL)

    #print(mx)
    ans, aux = hopcroft_karp(AL, k + 1, k + 1)
    print(ans, aux)
    print(sum([1 for u in ans if u != -1]) // 2)
def solve(n, a):
    pass


if __name__ == "__main__":
    main()
