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
        n, k, pb, ps = ints()
        p = list(ints())
        a = list(ints())
        print(solve(n, k, pb, ps, p, a))


def solve(n, k, pb, ps, p, a):
    b = [0] * (n + 1)
    s = [0] * (n + 1)
    for i in range(1, n + 1):
        b[i] = b[i - 1] + a[p[(pb + i - 2) % n]]
        s[i] = s[i - 1] + a[p[(ps + i - 2) % n]]

    sb, ss = 0, 0
    for i in range(1, k + 1):
        sb += a[p[(pb + i - 2) % n]]
        ss += a[p[(ps + i - 2) % n]]
        sb += s[min(k - i, n)] - s[0]
        ss += b[min(k - i, n)] - b[0]

    if sb > ss:
        print("Bodya")
    elif sb < ss:
        print("Sasha")
    else:
        print("Draw")



if __name__ == "__main__":
    main()
