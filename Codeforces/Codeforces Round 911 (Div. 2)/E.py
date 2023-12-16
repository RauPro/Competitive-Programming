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


def main():
    t = int(input())
    for _ in range(t):
        n,m = ints()
        a = list(ints())
        AL = []
        for _ in range(m):
            AL.append(ints())
        adj_matrix = floyd_warshall(n, AL)
        print(*solve(n, a, adj_matrix))


def floyd_warshall(n, edges):
    adj_matrix = [[False for _ in range(n)] for _ in range(n)]
    for u, v in edges:
        adj_matrix[u - 1][v - 1] = True
    for i in range(n):
        adj_matrix[i][i] = True
    for k in range(n):
        for i in range(n):
            for j in range(n):
                adj_matrix[i][j] = adj_matrix[i][j] or (adj_matrix[i][k] and adj_matrix[k][j])

    return adj_matrix

def solve(n, a_values, adj_matrix):
    max_length = 0
    min_value = float('inf')

    for start in range(n):
        for end in range(n):
            if adj_matrix[start][end]:
                length = sum(1 for i in range(n) if adj_matrix[start][i] and adj_matrix[i][end])
                value = sum(a_values[i] for i in range(n) if adj_matrix[start][i] and adj_matrix[i][end])
                print(value)
                if length > max_length or (length == max_length and value < min_value):
                    max_length = length
                    min_value = value

    return max_length, min_value



if __name__ == "__main__":
    main()
