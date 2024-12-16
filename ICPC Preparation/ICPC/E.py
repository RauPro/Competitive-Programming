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
    solve()

def can_add(prev, sig, ini, fini):
    if ini[sig] < ini[prev]:
        sig, prev = prev, sig

    # ({)} bad
    if ini[sig] < fini[prev] and fini[prev] < fini[sig]:
        return False
    return True

def dfs(u, graph, color, ok):
    for v in graph[u]:
        if color[v] == -1:
            color[v] = 1 - color[u]
            dfs(v, graph, color, ok)
        elif color[v] == color[u]:
            ok[0] = False
def solve():
    n = int(input())

    a = [0] * (2 * n + 1)
    ini = [0] * (n + 1)
    fini = [0] * (n + 1)
    in_ = [int(i) for i in list(map(str, input().split()))]
    for i in range(2 * n):
        if in_[i] > 0:
            ini[in_[i]] = i
        else:
            fini[-in_[i]] = i
    graph = [[] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if can_add(i, j, ini, fini):
                continue
            graph[i].append(j)
            graph[j].append(i)
    print(graph)
    color = [-1] * (n + 1)
    ok = [True]

    for i in range(1, n + 1):
        if color[i] != -1:
            continue
        color[i] = 0
        dfs(i, graph, color, ok)

    if ok[0]:
        for i in range(1, n + 1):
            print('G' if color[i] == 0 else 'S', end='')
        print()
    else:
        print("*")

if __name__ == "__main__":
    main()
