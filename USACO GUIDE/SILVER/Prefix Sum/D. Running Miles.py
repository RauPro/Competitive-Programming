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

b = []
n = 0

def main():
    global n
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(ints())
        print(solve(n, a))
        dp.cache_clear()


@lru_cache(maxsize=None)
def dp(i, taken):
    #print(taken)
    if taken == 3:
        return 0
    if i == n or taken > 3:
        return int(1e5) * -1
    include = 0
    if taken == 0:
        include = dp(i + 1, taken + 1) + b[i] + i + 1
    elif taken == 1:
        include = dp(i + 1, taken + 1) + b[i]
    elif taken == 2:
        include = (dp(i + 1, taken + 1) + b[i]) - (i+1)
    exclude = dp(i + 1, taken)
    return max(include, exclude)


def iterative_dp(n, b):
    # Initialize DP table with a large negative value
    dp = [[-1e5 * 1000 for _ in range(4)] for _ in range(n + 1)]

    # Base case: when taken == 3, return 0
    for i in range(n + 1):
        dp[i][3] = 0

    # Iterate in reverse order
    for i in range(n - 1, -1, -1):
        for taken in range(3):
            # Calculate the 'exclude' case
            exclude = dp[i + 1][taken]

            # Calculate the 'include' case
            include = -1e5 * 1000
            if taken == 0:
                include = dp[i + 1][taken + 1] + b[i] + i + 1
            elif taken == 1:
                include = dp[i + 1][taken + 1] + b[i]
            elif taken == 2:
                include = dp[i + 1][taken + 1] + b[i] - (i + 1)

            # Store the maximum of include and exclude
            dp[i][taken] = max(include, exclude)

    # Return the maximum value achievable starting from the beginning
    return dp[0][0]


def solve(n ,a ):
    global b
    b = a
    #return dp(0, 0)
    return iterative_dp(n, b)



if __name__ == "__main__":
    main()
