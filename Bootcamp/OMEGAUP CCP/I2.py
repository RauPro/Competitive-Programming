import os
import sys
from collections import *
from heapq import *
from math import *
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
    n, q = ints()
    a = list(ints())
    solve(n, q, a)

class FTree:
    def __init__(self, f):
        self.n = len(f)
        self.ft = [0] * (self.n + 1)

        for i in range(1, self.n + 1):
            self.ft[i] += f[i - 1]
            if i + self.lsone(i) <= self.n:
                self.ft[i + self.lsone(i)] += self.ft[i]

    def lsone(self, s):
        return s & (-s)

    def query(self, i, j):
        if i > 1:
            return self.query(1, j) - self.query(1, i - 1)

        s = 0
        while j > 0:
            s += self.ft[j]
            j -= self.lsone(j)

        return s

    def update(self, i, v):
        while i <= self.n:
            self.ft[i] += v
            i += self.lsone(i)



def  solve(n, q, a):
    v = []
    for i, it in enumerate(a):
        if it == 0:
            v.append(INF)
        if it < 0:
            v.append(-1)
        if it > 0:
            v.append(1)
    print(v)
    ft =FTree(v)
    for _ in range(q):
        a, b, c = strs()
        b = int(b)
        c = int(c)
        if a == "M":
            ans = ft.query(b,c)
            if ans > int(10e9):
                print(0)
            elif ans < (c-b)+1 and (((c-b) + 1) - ans) % 2 != 0 and ((c-b) + 1) - ans != 1 :
                print("-")
            else:
                print("+")
        else:
            to_set = 0
            if c == 0:
                to_set = INF
            elif c > 0:
                to_set = 1
            else:
                to_set = -1

            ft.update(b,-v[b])
            ft.update(b, to_set)
            v[b]=to_set




if __name__ == "__main__":
    main()