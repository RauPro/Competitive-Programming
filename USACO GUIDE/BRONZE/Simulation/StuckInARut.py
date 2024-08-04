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



def main():

    n = int(input())
    ncows = []
    ecows = []
    for i in range(n):
        dir, x, y = input().split()
        if dir == 'N':
            ncows.append((i, int(x), int(y)))
        elif dir == 'E':
            ecows.append((i, int(x), int(y)))
    ncows.sort(key=lambda cow: cow[1])
    ecows.sort(key=lambda cow: cow[2])
    res = [float('inf')] * n
    for c1 in ncows:
        for c2 in ecows:
            a, b = c1[1], c1[2]
            c, d = c2[1], c2[2]
            if a - c < 0 or d - b < 0 or a - c == d - b: continue
            if a - c > d - b:
                if a - c > res[c1[0]]: continue
                res[c2[0]] = min(res[c2[0]], a - c)
            else:
                if d - b > res[c2[0]]: continue
                res[c1[0]] = min(res[c1[0]], d - b)

    for j in range(n):
        print("Infinity" if res[j] == float('inf') else res[j])


if __name__ == "__main__":
    main()
