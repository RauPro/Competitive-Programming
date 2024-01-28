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
    N, T = ints()
    arr_prio = []
    arr_not = []
    for _ in range(N):
        prior, size = input().split()
        size = int(size)
        if prior == "P":
            arr_prio.append(size)
        else:
            arr_not.append(size)
    solve(T, arr_prio, arr_not)

def solve(T ,a , a_n):
    T_prior = T * 0.75
    T_rest = T - T_prior
    sum_prior = sum(a)
    sum_not = sum(a_n)
    time_prior = sum_prior / T_prior
    time_rest = sum_not / T_rest
    if time_prior < time_rest:
        size_downloaded = T_rest * time_prior
        sum_not = sum_not - size_downloaded
        ans_not = sum_not / T
        print(ans_not + time_prior)
    else:
        size_downloaded = T_prior * time_rest
        sum_prior = sum_prior - size_downloaded
        ans_not = sum_prior / T
        print(ans_not + time_rest)



if __name__ == "__main__":
    main()
