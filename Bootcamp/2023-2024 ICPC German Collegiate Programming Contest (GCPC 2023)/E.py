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
    n, m = ints()
    print(solve(n, m))


def shortest_cycle(n: int, gr):
    ans = INF
    for i in range(n):
        dist = [int(1e9)] * n
        par = [-1] * n
        dist[i] = 0
        q = deque()
        q.append(i)
        temp_ans = []
        while q:
            x = q[0]
            q.popleft()
            temp_ans.append(x)
            for child in gr[x]:
                if dist[child] == int(1e9):
                    dist[child] = 1 + dist[x]
                    par[child] = x
                    q.append(child)
                elif par[x] != child and par[child] != x:
                    ans = min(ans, dist[x] +
                              dist[child] + 1)

    if ans == INF:
        return -1
    else:
        return ans


def dfs(graph, marked, n, vert, start, count):
    marked[vert] = True
    if n == 0:
        marked[vert] = False
        if start in graph[vert]:
            count += 1
        return count
    for i in graph[vert]:
        if not marked[i]:
            count = dfs(graph, marked, n - 1, i, start, count)
    marked[vert] = False
    return count

def countCycles(graph, n, V):
    marked = [False] * V
    count = 0
    for i in range(V - (n - 1)):
        count = dfs(graph, marked, n - 1, i, i, count)
        marked[i] = True
    return int(count / 2)

def solve(n, m):
    AL = [[] for i in range(n+1)]
    for i in range(m):
        u, v = ints()
        AL[u-1].append(v-1)
        AL[v-1].append(u-1)
    return countCycles(AL, shortest_cycle(n, AL), n)

if __name__ == "__main__":
    main()
