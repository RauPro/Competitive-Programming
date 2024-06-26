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

from collections import Counter

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
        n,m,k = ints()
        a = list(ints())
        b = list(ints())
        print(solve(n,m,k, a,b))


def solve(n,m,k, a,b):
    frec_b = Counter(b)
    frec_a = Counter(a[:m])
    it = 0
    for key, value in frec_a.items():
        if key in frec_b:
            it += min(frec_b[key], value)
    ans = 0
    if it >= k:
        ans += 1
    for i in range(1, n - m + 1):
        frec_a[a[i - 1]] -= 1
        if a[i - 1] in frec_b and frec_b[a[i - 1]] > frec_a[a[i - 1]]:
            it -= 1
        frec_a[a[i + m - 1]] += 1
        if a[i + m - 1] in frec_b and frec_b[a[i + m - 1]] >= frec_a[a[i + m - 1]]:
            it += 1
        if it >= k:
            ans += 1

    return ans
if __name__ == "__main__":
    main()
