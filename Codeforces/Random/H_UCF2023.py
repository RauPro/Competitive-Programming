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
    global sums, visited, AL
    n, m = ints()
    AL = [[] for i in range(n+1)]
    for i in range(m):
        u, v, c, w = strs()
        w = int(w) * (-1 if c == 'r' else 1)
        u = int(u)
        v = int(v)
        AL[u].append((v, w))
    dist = [INF for i in range(n+1)]
    in_queue = [0 for i in range(n + 1)]
    dist[1] = 0
    q = deque([])
    q.append(1)
    while q:
        u = q.pop()
        in_queue[u] = 0;
        for v, w in AL[u]:
            if dist[u] +  w >= dist[v]: continue
            dist[v]  = dist[u] + w
            if not in_queue[v]:
                q.append(v)
                in_queue[v] = 1
    for u in range(n+1):
        if dist[u] < 0:
            print(u)
def solve(n ,a ):
    pass



if __name__ == "__main__":
    main()
