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
    a = [i for i in range(1, n+1)]
    solve(n,a)


def solve(n ,a ):
    sum_ = sum(a)
    total_w = sum_ // 2
    if sum_ - total_w*2 != 0:
        print("NO")
    else:
        @lru_cache(maxsize=None)
        def kns(i, rem):
            if i == n - 1 or rem == 0:
                if rem ==0:
                    print("YES")
                    """list_ = [int(el) for el in list_]
                    frec = Counter(list_)
                    print(len(list_))
                    print(*list_)
                    print(n-len(list_))
                    for it in a:
                        if frec[it] == 1:
                            continue
                        print(it, end = " ")"""
                    exit(0)
                return 0
            if a[i] > rem:
                return kns(i+1, rem, )
            return max(kns(i+1, rem, ), a[i] + kns(i+1, rem - a[i], ))
        ans = kns(0, total_w)
        if ans - total_w == 0:
            print("YES")
        else:
            print("NO")



if __name__ == "__main__":
    main()
