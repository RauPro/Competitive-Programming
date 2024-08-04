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

cc = 0
visited = []
s = ""
def dfs(u, time, AL):
    global cc, visited
    cc+=1
    visited[u] = True
    for v, w in AL[u]:
        if not visited[v] and w >= time and s[v-1] == '1':
            dfs(v, time, AL)

def main():
    global cc, visited, s
    #sys.stdin = open('tracing.in', 'r')
    #sys.stdout = open('tracing.out', 'w')
    n, m =ints()
    s = input()
    infected = s.count('1')
    AL = [[] for i in range(n+1)]
    for i in range(m):
        w, u, v = ints()
        AL[u].append((v, w))
        AL[v].append((u, w))



    print(zero_p, min_k, "Infinity" if max_k == INF else max_k)


if __name__ == "__main__":
    main()
