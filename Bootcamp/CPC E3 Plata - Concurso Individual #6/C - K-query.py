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
    n = int(input())
    a = list(ints())
    q = int(input())
    solve(n, a, q)





class STree:
    def __init__(self, l):
        self.l = l
        self.n = len(l)
        self.st = [0] * (4 * self.n)
        self.islazy = [False] * (4 * self.n)
        self.lazy = [0] * (4 * self.n)

        self.build(1, 0, self.n - 1)

    def left(self, p):
        return p << 1

    def right(self, p):
        return (p << 1) + 1

    def build(self, p, l, r):
        if (l == r):
            self.st[p] = l
        else:
            self.build(self.left(p), l, (l + r) // 2)
            self.build(self.right(p), (l + r) // 2 + 1, r)
            p1 = self.st[self.left(p)]
            p2 = self.st[self.right(p)]
            if self.l[p1] <= self.l[p2]:
                self.st[p] = p1
            else:
                self.st[p] = p2

    def _q(self, p, pl, pr, fr, to):
        if fr > pr or to < pl:
            return -1, -1
        if self.islazy[p]:
            return fr, self.lazy[p]
        if fr <= pl and to >= pr:
            return self.st[p], self.l[self.st[p]]

        res1 = self._q(self.left(p), pl, (pl + pr) // 2, fr, to)
        res2 = self._q(self.right(p), (pl + pr) // 2 + 1, pr, fr, to)

        if (res1[0] == -1):
            return res2
        elif res2[0] == -1:
            return res1
        elif res1[1] <= res2[1]:
            return res1
        else:
            return res2

    def _u(self, p, pl, pr, fr, to, newval):
        if fr > pr or to < pl:
            return self.st[p]

        if fr == pl and to == pr:
            if fr == to:
                self.l[pl] = newval
                self.islazy[p] = False
            else:
                self.lazy[p] = newval
                self.islazy[p] = True

            self.st[p] = fr
            return self.st[p]

        pm = (pl + pr) // 2

        if self.islazy[p]:
            self.islazy[p] = False
            self.islazy[self.left(p)] = True
            self.islazy[self.right(p)] = True
            self.lazy[self.left(p)] = self.lazy[p]
            self.lazy[self.right(p)] = self.lazy[p]
            self.st[self.left(p)] = pl
            self.st[self.right(p)] = pm

        p1 = self._u(self.left(p), pl, pm, max(fr, pl), min(to, pm), newval)
        p2 = self._u(self.right(p), pm + 1, pr, max(fr, pm + 1), min(to, pr), newval)

        if self.l[p1] <= self.l[p2]:
            self.st[p] = p1
        else:
            self.st[p] = p2
        return self.st[p]

    def q(self, fr, to):
        return self._q(1, 0, self.n - 1, fr, to)[0]

    def u(self, fr, to, val):
        return self._u(1, 0, self.n - 1, fr, to, val)

def solve(n, a, q):
    for i in range(q):
        i,j,k = ints()
        new_arr = a[i-1:j]
        new_arr.sort()
        rest = 0
        lo, hi = 0, len(new_arr) - 1
        while hi - lo > 1:
            mid = (lo + hi) // 2
            if new_arr[mid] > k:
                hi = mid
            else:
                lo = mid
        if hi == 0:
            print(0)
            continue
        total = (j - (i-1)) - (hi)
        print(total)


if __name__ == "__main__":
    main()
