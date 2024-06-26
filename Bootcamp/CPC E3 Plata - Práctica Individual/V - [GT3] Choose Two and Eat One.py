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


# Algunas funciones útiles
def add(x, y, mod=MOD): return (x + y) % mod
def sub(x, y, mod=MOD): return (x - y) % mod
def mul(x, y, mod=MOD): return (x * y) % mod

# Inverso multiplicativo de a modulo m (cuando m es primo)
def invmod(a, mod=MOD): return powmod(a, mod - 2, mod)

def lcm(a, b): return a * b // gcd(a, b)

RANDOM = getrandbits(32)

class Wrapper(int):
    def __init__(self, x):
        int.__init__(x)
    def __hash__(self):
        return super(Wrapper, self).__hash__() ^ RANDOM

class UnionFind:                                # OOP style
    def __init__(self, N):
        self.p = [i for i in range(N)]
        self.rank = [0 for i in range(N)]
        self.setSize = [1 for i in range(N)]
        self.numSets = N

    def findSet(self, i):
        if (self.p[i] == i):
            return i
        else:
            self.p[i] = self.findSet(self.p[i])
            return self.p[i]

    def isSameSet(self, i, j):
        return self.findSet(i) == self.findSet(j)

    def unionSet(self, i, j):
        if (not self.isSameSet(i, j)):
            self.numSets -= 1
            x = self.findSet(i)
            y = self.findSet(j)
        # rank is used to keep the tree short
        if (self.rank[x] > self.rank[y]):
            self.p[y] = x
            self.setSize[x] += self.setSize[y]
        else:
            self.p[x] = y
            self.setSize[y] += self.setSize[x]
            if (self.rank[x] == self.rank[y]):
                self.rank[y] += 1

    def numDisjointSets(self):
        return self.numSets

    def sizeOfSet(self, i):
        return self.setSize[self.findSet(i)]

def main():
    n, m = ints()
    print(solve(n, m))


def solve(V, E):
    a = list(ints())
    EL = []
    for i in range(V):
        for j in range(i+1, V):
            w = (pow(a[i], a[j], E) + pow(a[j], a[i], E)) % E
            EL.append((w, i, j))
    EL.sort(reverse=True)
    #print(EL)
    mst_cost = 0
    num_taken = 0
    UF = UnionFind(V)

    for it in EL:
        if num_taken == V - 1:
            break
        w, u, v = it
        if (not UF.isSameSet(u, v)):
            num_taken += 1
            mst_cost += w
            UF.unionSet(u, v)

    return mst_cost

if __name__ == "__main__":
    main()
