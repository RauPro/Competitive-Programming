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
        h, m = strs()
        print(solve(h,m))

def mins_to_h(total_time):
    h = total_time // 60
    m = total_time - ((total_time // 60) * 60)
    if h < 10:
        h = "0" + str(h)
    if m < 10:
        m = "0" + str(m)
    return h, m

def check_pal(total_time):
    h, m = mins_to_h(total_time)
    h = str(h)
    m = str(m)
    return h[0] == m[1] and h[1] == m[0]
def solve(h,m):
    time_h, time_m = h.split(':')
    time_h =int(time_h)
    time_m = int(time_m)
    time_h_to_m = 60 * time_h

    total_time = time_h_to_m + time_m
    initial_time = total_time
    m = int(m)
    total_time+= m
    total_time %= 1440
    ans = int(check_pal(total_time))
    while total_time != initial_time:
        total_time += m
        total_time %= 1440
        ans += check_pal(total_time)
    return ans


if __name__ == "__main__":
    main()
