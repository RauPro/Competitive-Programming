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

class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (2*self.n)
        self.build_tree(arr)

    def build_tree(self, arr):
        for i in range(self.n):
            self.tree[self.n + i] = arr[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[i << 1] * self.tree[i << 1 | 1]

    def update(self, p, value):
        p += self.n
        self.tree[p] = value
        i = p
        while i > 1:
            self.tree[i >> 1] = self.tree[i] if i % 2 == 0 else self.tree[i] * self.tree[i ^ 1]
            i >>= 1

    def query(self, left, right):
        left += self.n
        right += self.n
        prod = 1
        while left < right:
            if left & 1:
                prod *= self.tree[left]
                left += 1
            if right & 1:
                right -= 1
                prod *= self.tree[right]
            left >>= 1
            right >>= 1
        return prod



def  solve(n, q, a):
    ft =SegmentTree(a)
    for _ in range(q):
        a, b, c= strs()
        b = int(b)
        c = int(c)
        if a == 'M':
            ans = ft.query(b, c)
            print(ans)
            if ans == 0:
                print(0)
            else:
                print("+" if ans > 0 else "-")
        else:
            ft.update(b, 1//c)
            ft.update(b, c)




if __name__ == "__main__":
    main()
