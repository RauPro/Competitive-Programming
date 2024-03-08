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


def preprocess_string(S):
    segments = []
    start = 0
    for i in range(1, len(S)):
        if S[i] != S[i - 1]:
            segments.append((start, i - 1, S[i - 1]))
            start = i
    segments.append((start, len(S) - 1, S[start]))


    index_to_segment = {}
    for start, end, char in segments:
        for i in range(start, end + 1):
            index_to_segment[i] = (start, end, char)

    return index_to_segment


def update_string(S, index_to_segment, i):

    S = S[:i] + '#' + S[i + 1:]

    start, end, char = index_to_segment[i]
    if start < i:
        for j in range(start, i):
            index_to_segment[j] = (start, i - 1, char)
    if end > i:
        for j in range(i + 1, end + 1):
            index_to_segment[j] = (i + 1, end, char)
    index_to_segment[i] = (i, i, '#')
    return S


def solve_queries(S, queries):
    index_to_segment = preprocess_string(S)
    results = []
    for query in queries:
        type_q, i = query
        if type_q == 1:
            start, end, _ = index_to_segment[i]
            results.append(end - start + 1)
        else:
            S = update_string(S, index_to_segment, i)
    return results

def main():
    t = int(input())
    for _ in range(t):
        s = input()
        n = int(input())
        queries = []
        for n in range(n):
            a, b = ints()
            queries.append((a, b))
        results = solve_queries(s, queries)
        print(f"Case {_ + 1}:")
        for res in results:
            print(res)



def solve(n ,a ):
    pass



if __name__ == "__main__":
    main()
