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
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(ints())
        print(solve(n, a))

lvl = []
AL = []
padre = []
def dfs(u, p):
    global lvl,AL, padre
    lvl[u] = p
    for v in AL[u]:
        if v != padre[u]:
            padre[v] = u
            dfs(v, p + 1)



def solve(n , p ):
    global lvl, AL, padre
    AL = [[] for _ in range(n + 1)]
    lvl = [0] * (n + 1)
    padre = [0] * (n + 1)
    for i in range(2, n + 1):
        AL[p[i - 2]].append(i)
    dfs(1, 1)
    #print(lvl)
    lvl = lvl[1:]
    lvl.sort()
    frec = Counter(lvl)
    unpaired = 0
    ans = 0
    #print(frec)
    frec = dict(sorted(frec.items(), key=lambda item: item[0], reverse=True))
    for lv, it in frec.items():
        if it > 1:
            to_match = min(unpaired, it - 1)
            unpaired -= to_match
            it -= to_match
            ans += to_match
        ans += (it // 2)
        #print(ans, it)
        it %= 2
        unpaired += it
    return (ans)



if __name__ == "__main__":
    main()
