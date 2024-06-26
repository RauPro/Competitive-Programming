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
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(ints())
        print(solve(n, a))

def psum(x):
    total = 0
    while x > 0:
        total += bit[x]
        x -= x & -x
    return total


def add(x, val):
    while x < len(bit):
        bit[x] += val
        x += x & -x

def solve(n ,a , k=3):
    if n <= 2:
        return min(a)
    a = [0] + a
    compressed = {}
    decompress = {}
    max_ = 0
    # Compress the values of 'a'
    unique_a = sorted(set(a[1:]))
    for index, value in enumerate(unique_a, start=1):
        compressed[value] = index
        decompress[index] = value

    global bit
    bit = [0] * (len(compressed) + 1)

    # Process the input data
    for i in range(1, n + 1):
        add(compressed[a[i]], 1)
        if i >= k + 1:
            add(compressed[a[i - k]], -1)
        if i >= k:
            mid = (k // 2) + (k % 2)
            lo, hi = 1, len(compressed)
            ans = -1
            while lo <= hi:
                m = (lo + hi) // 2
                if psum(m) >= mid and psum(m - 1) < mid:
                    ans = m
                    break
                elif psum(m) < mid:
                    lo = m + 1
                else:
                    hi = m - 1
            max_ = max(decompress[ans], max_)

    return max_

if __name__ == "__main__":
    main()
