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


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(ints())
        g = list(strs())
        print(solve_hopcroft_karp(n, a, g))


def bfs(U, pair_u, pair_v, dist):
    queue = deque()
    # Start by considering all free vertices in U to start BFS
    for u in range(1, len(U)):
        if pair_u[u] == 0:
            dist[u] = 0
            queue.append(u)
        else:
            dist[u] = float('inf')
    dist[0] = float('inf')  # Infinity for the null node

    while queue:
        u = queue.popleft()
        if dist[u] < dist[0]:
            for v in U[u]:
                if dist[pair_v[v]] == float('inf'):
                    dist[pair_v[v]] = dist[u] + 1
                    queue.append(pair_v[v])
    return dist[0] != float('inf')


def dfs(U, u, pair_u, pair_v, dist):
    if u != 0:
        for v in U[u]:
            if dist[pair_v[v]] == dist[u] + 1:
                if dfs(U, pair_v[v], pair_u, pair_v, dist):
                    pair_v[v] = u
                    pair_u[u] = v
                    return True
        dist[u] = float('inf')
        return False
    return True


def hopcroft_karp(U, V):
    pair_u = [0] * len(U)  # Pairing for u in U
    pair_v = [0] * len(V)  # Pairing for v in V
    dist = [0] * len(U)  # Distances in BFS

    matching = 0
    while bfs(U, pair_u, pair_v, dist):
        for u in range(1, len(U)):
            if pair_u[u] == 0:
                if dfs(U, u, pair_u, pair_v, dist):
                    matching += 1
    return matching


def solve_hopcroft_karp(n, personalities, genders):
    U = [[] for _ in range(n + 1)]
    V = [0] * (n + 1)

    students = [(personalities[i], genders[i]) for i in range(n)]
    index_map = {}

    for i, (_, g) in enumerate(students):
        index_map[i + 1] = i + 1

    for i in range(n):
        for j in range(i + 1, n):
            if (students[i][1] != students[j][1] or gcd(personalities[i], personalities[j]) > 1):
                U[i + 1].append(index_map[j + 1])
                V[j + 1] = 1

    max_matching = hopcroft_karp(U, V)

    min_groups = n - max_matching

    return min_groups


if __name__ == "__main__":
    main()
