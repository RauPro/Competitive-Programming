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


def is_non_decreasing(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

def create_seq(a):
    b = []
    for i in range(1, len(a)):
        b.append(gcd(a[i], a[i - 1]))
    return b

def solve(n, a):
    b = [gcd(a[i], a[i + 1]) for i in range(n - 1)]
    index = -1
    for i in range(n-2):
        if b[i+1] < b[i]:
            index = i + 1
    if index == -1:
        return "YES"
    #print(b)
    new_a1 = a[:index] + a[index+1:]
    new_a2 = a[:index+1] + a[index + 2:]
    index-=1
    new_a3 = a[:index] + a[index + 1:]
    new_a4 = a[:index + 1] + a[index + 2:]
    #print(new_a3, new_a4)
    new_b = [gcd(new_a1[i], new_a1[i + 1]) for i in range(len(new_a1)-1)]
    new_b2 = [gcd(new_a2[i], new_a2[i + 1]) for i in range(len(new_a2) - 1)]
    new_b3 = [gcd(new_a3[i], new_a3[i + 1]) for i in range(len(new_a3) - 1)]
    new_b4 = [gcd(new_a4[i], new_a4[i + 1]) for i in range(len(new_a4) - 1)]
    #print(new_b2, new_b)
    return "YES" if (is_non_decreasing(new_b) or
                     is_non_decreasing(new_b2) or
                     is_non_decreasing(new_b3) or
                     is_non_decreasing(new_b4)) else "NO"


if __name__ == "__main__":
    main()
