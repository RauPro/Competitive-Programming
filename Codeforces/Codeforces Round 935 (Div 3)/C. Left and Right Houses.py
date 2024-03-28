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

from collections import Counter

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
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = [i for i in input()]
        ans = solve(n, a)
        # print(right, left)
        print(ans)


#binary search that return the closest index to the target
def binary_search(a, n):
    """i = bisect_left(a, x)
        if i != len(a) and a[i] == x or i  == 0:
            return i
        else:
            return i-1"""
    index = a[0]
    for i in a[1:]:
        if abs((n / 2) - i) < abs((n/2) - index):
            index = i
    return index
def solve(n, a):
    frec = Counter(a)
    satisfied_1 = frec['1']
    satisfied_0 = 0
    mid = n // 2 if n % 2 == 0 else n // 2 + 1
    index = 0
    ans = []
    for i in range(n):
        if a[i] == '1':
            satisfied_1 -= 1
        else:
            satisfied_0 += 1
        if satisfied_0 >= ceil((i+1)/2) and frec['0'] - satisfied_0 <= (n - (i+1)) // 2:
            index = i + 1
            ans.append(index)
        #print(ans, satisfied_0, satisfied_0 - n)

    # satisied == n return 0
    if satisfied_0 == n:
        return n
    # insatified == n return n
    if satisfied_1 == n:
        return 0
    if len(ans) ==1 and ans[-1] == n and satisfied_0 == n - satisfied_0:
        return 0
    if len(ans) != 0:
        return (binary_search(ans, n))
    #print(ans[binary_search(ans, n//2)])
    return 0


if __name__ == "__main__":
    main()
