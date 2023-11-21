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

class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, idx, value):
        while idx <= self.size:
            self.tree[idx] += value
            idx += idx & -idx

    def query(self, idx):
        sum = 0
        while idx > 0:
            sum += self.tree[idx]
            idx -= idx & -idx
        return sum

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(ints())
        b = list(ints())
        print(solve(n, a, b))


def calculate_initial_beauty(a, b):
    return sum(abs(a_i - b_i) for a_i, b_i in zip(a, b))

def solve(n, a, b):
    initial_differences = [abs(a[i] - b[i]) for i in range(n)]
    initial_beauty = sum(initial_differences)

    # Arreglos de DP para máximos incrementos posibles
    max_increase_before = [0] * n
    max_increase_after = [0] * n

    # Llenar los arreglos de DP para el incremento máximo antes de cada índice
    for i in range(1, n):
        max_increase_before[i] = max(max_increase_before[i - 1],
                                     abs(a[i] - b[i - 1]) - initial_differences[i] + initial_differences[i - 1])

    # Llenar los arreglos de DP para el incremento máximo después de cada índice
    for i in range(n - 2, -1, -1):
        max_increase_after[i] = max(max_increase_after[i + 1],
                                    abs(a[i] - b[i + 1]) - initial_differences[i] + initial_differences[i + 1])

    # Calcular la belleza absoluta máxima
    max_beauty = initial_beauty
    for i in range(n):
        # Considerar el mejor intercambio hasta el índice i
        max_beauty = max(max_beauty, initial_beauty + max_increase_before[i] + max_increase_after[i])

    return max_beauty



if __name__ == "__main__":
    main()
