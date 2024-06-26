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


class FT:
    def __init__(self, m):
        self.m = m + 1
        self.ft = [0] * (m + 1)

    def rsq_(self, pos):
        sum_ = 0
        while pos > 0:
            sum_ += self.ft[pos]
            pos -= pos & -pos
        return sum_
    def rsq(self,i,j):
        return self.rsq_(j) - self.rsq_(i-1)
    def update(self, pos, val):
        while pos < self.m:
            self.ft[pos] += val
            pos += pos & -pos


def main():
    n, m = ints()
    a = list(ints())
    solve(n, m, a)



def solve(n,m, a):
    ft = FT(n)
    for i, it in enumerate(a):
        ft.update(i+1, it)

    for q in range(m):
        p,b,c = ints()
        if p == 1:
            ft.update(b, -a[b-1])
            ft.update(b,c)
        if p == 2:
            print(ft.rsq_(c) - ft.rsq_(b-1))



if __name__ == "__main__":
    main()
