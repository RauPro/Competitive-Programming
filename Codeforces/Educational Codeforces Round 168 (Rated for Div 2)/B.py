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
import re
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
    t = int(input())
    for _ in range(t):
        n = int(input())
        m = [[i for i in input()], [i for i in input()]]
        print(solve(n, m))

def delete_consecutives(s):
    patron = r'(?=(x\.{1,}x))'
    matches = list(re.finditer(patron, s))
    return [(match.start(1), match.end(1) - 1) for match in matches]
def solve(n ,m):
    if n <= 2:
        return 0
    ranges = []
    start = 0
    list_s1 = delete_consecutives(''.join(m[0]))
    list_s2 = delete_consecutives(''.join(m[1]))
    #print(list_s2, list_s1)
    ans = 0
    for s, e in list_s1:
        num_x = e - s - 2
        if num_x == sum(1 for it in m[1][s:e+1] if it == 'x'):
            ans += 1
    for s, e in list_s2:
        num_x = e - s - 2
        if num_x == sum(1 for it in m[0][s:e+1] if it == 'x'):
            ans += 1
    return ans


if __name__ == "__main__":
    main()
