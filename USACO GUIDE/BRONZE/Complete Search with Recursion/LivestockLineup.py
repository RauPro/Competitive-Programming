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

names = ["Bessie", "Buttercup", "Belinda", "Beatrice", "Bella", "Blue", "Betsy", "Sue"]
AL = []
visited = []
depth = []
def dfs(u, d, p = False):
    global visited, AL, depth
    if p ==  True: print(names[u])
    visited[u] = True
    depth[u] = (d, u)
    for v in AL[u]:
        if not visited[v]:
            dfs(v, d+1)
def main():
    global visited, AL, depth
    sys.stdin = open('lineup.in', 'r')
    sys.stdout = open('lineup.out', 'w')
    n = int(input())
    AL = defaultdict(list)
    mapper = {names[i]: i for i in range(8)}
    for i in range(n):
        aux = list(input().split())
        AL[mapper[aux[0]]].append(mapper[aux[-1]])
        AL[mapper[aux[-1]]].append(mapper[aux[0]])
    visited = [False] * 8
    depth = [0] * 8
    for i in range(8):
        if not visited[i]:
            dfs(i, 0)
    depth.sort(reverse=True)
    visited = [False] * 8
    for d, u in depth:
        dfs(u, 0,  True)




if __name__ == "__main__":
    main()
