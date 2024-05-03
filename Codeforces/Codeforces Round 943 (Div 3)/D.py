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
        n, k, pb, ps = ints()
        p = list(ints())
        a = list(ints())
        print(solve(n, k, pb, ps, p, a))


def solve(n, k, pb, ps, p, a):
    score_Bodya, score_Sasha = 0, 0
    pos_Bodya, pos_Sasha = pb - 1, ps - 1
    positions_Bodya, positions_Sasha = [], []
    scores_Bodya, scores_Sasha = [], []
    for _ in range(k):
        score_Bodya += a[pos_Bodya]
        if pos_Bodya in positions_Bodya:
            remaining_turns = k - len(positions_Bodya)
            score_Bodya += (a[pos_Bodya] * (remaining_turns - 1))
            break
        if a[p[pos_Bodya] - 1] > a[pos_Bodya]:
            pos_Bodya = p[pos_Bodya] - 1
        positions_Bodya.append(pos_Bodya)
        scores_Bodya.append(score_Bodya)
    for _ in range(k):
        score_Sasha += a[pos_Sasha]
        if pos_Sasha in positions_Sasha:
            remaining_turns = k - len(positions_Sasha)
            score_Sasha += (a[pos_Sasha] * (remaining_turns - 1))
            break
        if a[p[pos_Sasha] - 1] > a[pos_Sasha]:
            pos_Sasha = p[pos_Sasha] - 1
        positions_Sasha.append(pos_Sasha)
        scores_Sasha.append(score_Sasha)
    print(score_Sasha, score_Bodya)
    if score_Bodya > score_Sasha:
        return "Bodya"
    elif score_Sasha > score_Bodya:
        return "Sasha"
    else:
        return "Draw"



if __name__ == "__main__":
    main()
