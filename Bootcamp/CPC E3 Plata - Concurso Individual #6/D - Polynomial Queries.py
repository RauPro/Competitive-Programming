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
    n, m = ints()
    a = list(ints())
    print(solve(n,m,a))



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
            self.st[p] = self.l[l]  # store value instead of index
        else:
            self.build(self.left(p), l, (l + r) // 2)
            self.build(self.right(p), (l + r) // 2 + 1, r)
            self.st[p] = self.st[self.left(p)] + self.st[self.right(p)]  # sum instead of min

    def _q(self, p, pl, pr, fr, to):
        if fr > pr or to < pl:
            return 0  # return 0 for out of range
        if self.islazy[p]:
            return self.lazy[p] * (min(to, pr) - max(fr, pl) + 1)  # return lazy value * range size
        if fr <= pl and to >= pr:
            return self.st[p]

        res1 = self._q(self.left(p), pl, (pl + pr) // 2, fr, to)
        res2 = self._q(self.right(p), (pl + pr) // 2 + 1, pr, fr, to)

        return res1 + res2  # return sum of left and right

    def _u(self, p, pl, pr, fr, to):
        if fr > pr or to < pl:
            return
        if fr <= pl and to >= pr:
            self.lazy[p] += (pr - pl + 1) * (pr - pl + 2) // 2
            self.islazy[p] = True
            return
        pm = (pl + pr) // 2

        if self.islazy[p]:
            self.islazy[p] = False
            self.islazy[self.left(p)] = True
            self.islazy[self.right(p)] = True

            # Propagate the lazy value to the children
            self.lazy[self.left(p)] += self.lazy[p]
            self.lazy[self.right(p)] += self.lazy[p]

        self._u(self.left(p), pl, pm, max(fr, pl), min(to, pm))
        self._u(self.right(p), pm + 1, pr, max(fr, pm + 1), min(to, pr))

        self.st[p] = self.st[self.left(p)] + self.st[self.right(p)]

    def q(self, fr, to):
        return self._q(1, 0, self.n - 1, fr, to)

    def u(self, fr, to):
        return self._u(1, 0, self.n - 1, fr, to)


def solve(n ,m,a ):
    st = STree(a)
    for q in range(m):
        t, a, b = ints()
        if t == 1:
            st.u(a-1, b-1)
        else:
            print(st.q(a-1, b-1))



if __name__ == "__main__":
    main()
