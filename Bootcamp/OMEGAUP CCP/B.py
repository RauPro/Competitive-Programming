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


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def main():
    n, m = ints()
    x0, y0 = ints()
    matrix = []
    for i in range(n):
        matrix.append(list(ints()))
    #print(matrix)
    print(solve(n, m, x0, y0, matrix))



def solve(N, M, x0, y0, m):
    visited = [[False] * M for _ in range(N)]
    queue = deque([(x0 - 1, y0 - 1, 0)])
    visited[x0 - 1][y0 - 1] = True #FLOOFILL using BFS
    while queue:
        x, y, steps = queue.popleft()
        if (x == 0 and m[x][y] & 2 == 0) or \
                (x == N - 1 and m[x][y] & 8 == 0) or \
                (y == 0 and m[x][y] & 1 == 0) or \
                (y == M - 1 and m[x][y] & 4 == 0):
            return steps
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and \
                    ((i == 0 and m[x][y] & 2 == 0 and m[nx][ny] & 8 == 0) or
                     (i == 1 and m[x][y] & 4 == 0 and m[nx][ny] & 1 == 0) or
                     (i == 2 and m[x][y] & 8 == 0 and m[nx][ny] & 2 == 0) or
                     (i == 3 and m[x][y] & 1 == 0 and m[nx][ny] & 4 == 0)):
                queue.append((nx, ny, steps + 1))
                visited[nx][ny] = True
    return -1


if __name__ == "__main__":
    main()
