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



def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(ints())
        print(solve(n, a))

def getMAD(a):
    cnt = {}
    mad = 0
    b = [0] * len(a)
    for i, it in enumerate(a):
        wx = Wrapper(it)
        cnt[wx] = cnt.get(wx, 0) + 1
        if cnt[wx] > 1:
            mad = max(mad, it)
        b[i] = mad
    return b

def solve(n ,a ):
    sum_ = 0
    allZero = False
    mad = getMAD(a)[i]
    while (not allZero):
        currentSum = 0
        for it in a:
            currentSum += it
        sum_ += currentSum
        b = [0] * n
        for i in range(n):
            b[i] = mad[i]
        allZero = True
        for i in range(n):
            a[i] = b[i]
            if a[i] != 0:
                allZero = False
    return sum_


if __name__ == "__main__":
    main()
