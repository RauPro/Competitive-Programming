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
    sys.stdin = open('cownomics.in', 'r')
    sys.stdout = open('cownomics.out', 'w')
    n, m = ints()
    positions_spot = [[] for i in range(m)]
    positions_plain = [[] for i in range(m)]
    for i in range(n):
        s = input()
        for i,it in enumerate(s):
            positions_spot[i].append(it)

    for i in range(n):
        s = input()
        for i,it in enumerate(s):
            positions_plain[i].append(it)
    ans = 0
    for i, it in enumerate(positions_spot):
        unique = set(it)
        flag = True
        for u in unique:
            if u in positions_plain[i]:
                flag = False
        if flag:
            ans +=1

    print(ans)



if __name__ == "__main__":
    main()
