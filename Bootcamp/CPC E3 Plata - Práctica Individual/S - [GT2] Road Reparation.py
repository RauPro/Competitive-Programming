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


# Algunas funciones útiles
def add(x, y, mod=MOD): return (x + y) % mod


def sub(x, y, mod=MOD): return (x - y) % mod


def mul(x, y, mod=MOD): return (x * y) % mod


# Inverso multiplicativo de a modulo m (cuando m es primo)
def invmod(a, mod=MOD): return powmod(a, mod - 2, mod)


def lcm(a, b): return a * b // gcd(a, b)


def process(u, taken, AL, pq):
    taken[u] = 1
    for v, w in AL[u]:
        if (not taken[v]):
            heappush(pq, (w, v))


def main():
    n, m = ints()
    print(solve(n, m))


def solve(V, E):
    AL = [[] for i in range(V)]
    for i in range(E):
        u, v, w = ints()
        v-=1
        u-=1
        AL[u].append((v, w))
        AL[v].append((u, w))

    taken = [0 for i in range(V)]
    pq = []
    process(0, taken, AL, pq)
    mst_cost = 0
    num_taken = 0
    while len(pq) > 0 and num_taken < V - 1:
        w, u = heappop(pq)
        if not taken[u]:
            num_taken += 1
            mst_cost += w
            process(u, taken, AL, pq)

    return mst_cost if num_taken == V - 1 else "IMPOSSIBLE"


if __name__ == "__main__":
    main()
