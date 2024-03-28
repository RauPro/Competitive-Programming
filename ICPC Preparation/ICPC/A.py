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


def main():
    m = int(input())
    AL = [[] for _ in range(m+1)]
    for _ in range(m):
        u, v = ints()
        AL[u].append(v)
        AL[v].append(u)
    print(AL)
    solve(m, AL)


#Print all path from vertex u to v



def solve(m, AL):
    visited = [False] * 5
    print( verify(1, 3, visited, AL))

#Get all cycles in the undirected graph
#Check if combined cycles are not
dfs_counter = 0
found = False
def dfs(u, v, visited, AL, cycles):
    global dfs_counter, found
    dfs_counter+=1
    #if found:
     #   return
    visited[v] = True
    if v not in cycles:
        cycles.append(v)
    for i in AL[v]:
        cycles = cycles[:cycles.index(v)+1]
        if not visited[i]:
            dfs(u, i, visited, AL, cycles)
        elif i in cycles and i!= u:
            continue
        elif i == u and dfs_counter > 3:
            found = True
            print(cycles)

def solve(m, AL):
    global dfs_counter, found
    all_cycles = []
    for i in range(m):
        cycles = []
        dfs_counter = found = 0
        visited = [False] * m
        dfs(i, i, visited, AL, cycles)
        all_cycles.append(set(cycles))
    print(all_cycles)


if __name__ == "__main__":
    main()
