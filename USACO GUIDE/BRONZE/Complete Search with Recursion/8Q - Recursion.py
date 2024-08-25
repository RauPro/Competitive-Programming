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

ans = 0
diag1 = defaultdict(lambda: False)
diag2 = defaultdict(lambda: False)
row_taken = [False] * 8

def main():
    m = []
    for i in range(8):
        m.append(list(input().strip()))
    solve(0, m)
    print(ans)



def solve(c, m):
    global ans, diag1, diag2, row_taken
    if c == 8:
        ans +=1
        return
    for r in range(8):
        if m[r][c] == '*' or row_taken[r] or diag1[r + c] or diag2[r - c]: continue
        row_taken[r] = True
        diag1[r + c] = True
        diag2[r - c] = True
        solve(c+1, m)
        row_taken[r] = False
        diag1[r + c] = False
        diag2[r - c] = False


if __name__ == "__main__":
    main()
