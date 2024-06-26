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
        m, x = ints()
        cost = []
        happiness = []
        for i in range(m):
            c, h = ints()
            cost.append(c)
            happiness.append(h)
        print(solve(m,x, cost, happiness))


def solve(m,x, cost, happiness ):
    n = len(cost)
    def knapsack(remW, index):
        if index == n or remW == 0:
            return 0, 0  # Return zero happiness and zero cost

            # If the current item's cost exceeds the remaining weight, skip this item
        if cost[index] > remW:
            return knapsack(remW, index + 1)

            # Explore two scenarios: not taking the current item, and taking the current item
        without_item = knapsack(remW, index + 1)
        with_item_happiness, with_item_cost = knapsack(remW - cost[index], index + 1)
        with_item_happiness += happiness[index]  # Increase happiness by the current item's value
        with_item_cost += cost[index]  # Increase cost by the current item's cost

        # Choose the option that provides the maximum happiness
        if with_item_happiness > without_item[0]:
            return with_item_happiness, with_item_cost
        else:
            return without_item

    ans = 0
    for i in range(1, n):
        curr = knapsack(x, i)
        print(curr)
    return ans


if __name__ == "__main__":
    main()
