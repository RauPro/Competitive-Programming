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
from random import getrandbits

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
abcd = "abcdefghijklmnopqrstuvwxyz"

# Algunas funciones útiles
def add(x, y, mod=MOD): return (x + y) % mod
def sub(x, y, mod=MOD): return (x - y) % mod
def mul(x, y, mod=MOD): return (x * y) % mod

# Inverso multiplicativo de a modulo m (cuando m es primo)
def invmod(a, mod=MOD): return powmod(a, mod - 2, mod)

def lcm(a, b): return a * b // gcd(a, b)

RANDOM = getrandbits(32)

class Wrapper(int):
    def __init__(self, x):
        int.__init__(x)
    def __hash__(self):
        return super(Wrapper, self).__hash__() ^ RANDOM


def can_be_covered(subset, barn, airs):
    total_cost = 0
    current = [0] * 100
    ans = INF
    for i in subset:
        ai, bi, pi, mi = airs[i]
        ai -= 1
        bi -= 1
        total_cost += mi
        for j in range(ai, bi+1):
            current[j] += pi
    all_covered = True
    for i in range(100):
        if barn[i] == INF: continue
        if current[i] < barn[i]:
            all_covered = False
            break
    if all_covered:
        ans = min(total_cost, ans)
    return ans
def main():
    n, m = ints()
    barn = [INF] * 100
    for i in range(n):
        ai, bi, t = ints()
        ai -= 1
        bi -= 1
        for j in range(ai, bi + 1):
            if barn[j] == INF:
                barn[j] = t
            barn[j] = max(barn[j], t)
    airs = []
    ans = INF
    for i in range(m):
        ai, bi, pi, mi = ints()
        airs.append((ai, bi, pi, mi))
    for b in range(1<<m):
        current = []
        for i in range(m):
            if b & (1 << i):
                current.append(i)
        if len(current) == 0: continue
        ans = min(ans, can_be_covered(current, barn, airs))
    print(ans)


def solve(n ,a ):
    pass



if __name__ == "__main__":
    main()
