import math
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
abcd = "abcdefghijklmnopqrstuvwxyz"


# Algunas funciones útiles
def add(x, y, mod=MOD): return (x + y) % mod


def sub(x, y, mod=MOD): return (x - y) % mod


def mul(x, y, mod=MOD): return (x * y) % mod


# Inverso multiplicativo de a modulo m (cuando m es primo)
def invmod(a, mod=MOD): return pow(a, mod - 2, mod)


def lcm(a, b): return a * b // gcd(a, b)


RANDOM = getrandbits(32)


class Wrapper(int):
    def __init__(self, x):
        int.__init__(x)

    def __hash__(self):
        return super(Wrapper, self).__hash__() ^ RANDOM


def precompute_factorials(n, mod):
    fact = [1] * (n + 1)
    ifact = [1] * (n + 1)
    for i in range(2, n + 1):
        fact[i] = fact[i - 1] * i % mod
    ifact[n] = invmod(fact[n], mod)
    for i in range(n - 1, 0, -1):
        ifact[i] = ifact[i + 1] * (i + 1) % mod
    return fact, ifact


def comb(n, k, fact, ifact, mod):
    if k > n or k < 0:
        return 0
    return fact[n] * ifact[k] % mod * ifact[n - k] % mod


def main():
    t = int(input())
    fact, ifact = precompute_factorials(200000 + 5, MOD)
    for _ in range(t):
        n, m = ints()
        a = list(ints())
        print(solve(n, a, m, fact, ifact))


def solve(n, a, k, fact, ifact):
    total_ones = sum(a)
    total_zeros = n - total_ones

    ans = 0
    start = (k + 1) // 2
    end = k + 1
    for i in range(start, end):
        ans += comb(total_ones, i, fact, ifact, MOD) * comb(total_zeros, k - i, fact, ifact, MOD)
        ans %= MOD
    return ans


if __name__ == "__main__":
    main()
