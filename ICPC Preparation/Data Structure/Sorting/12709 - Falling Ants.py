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

g = 9.81

def get_weight(a, b, c):
    return (a * b * c) * g

def get_volume(a, b, c):
    return a * b * c

def get_acceleration(l, w, h):
    return g - (g / (2*h))

def main():
    while True:
        n = int(input())
        if n == 0: break
        ants = []
        for _ in range(n):
            l, w, h = ints()
            ants.append((l, w, h))
        solve(n, ants)

def solve(n, arr):
    volumes = []
    max_vol = 0
    ans = 0.0
    for i in range(n):
        l , w, h = arr[i]
        volumes.append(get_volume(l, w, h))
        a = get_acceleration(l, w, h)
        #print(a, volumes[-1])
        if a >= ans:
            if a > ans:
                max_vol = volumes[-1]
            elif volumes[-1] > max_vol:
                max_vol = volumes[-1]
            ans = a

    print(max_vol)


if __name__ == "__main__":
    main()
