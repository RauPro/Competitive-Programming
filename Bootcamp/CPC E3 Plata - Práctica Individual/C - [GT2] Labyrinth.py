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


AL_P = []
final_i, final_j = 0, 0
start_i, start_j = 0, 0


def main():
    global final_i, final_j, start_i, start_j
    n, m = ints()
    AL = []

    for i in range(n):
        AL.append([_ for _ in input()])
        if 'A' in AL[i]:
            start_i = i
            start_j = AL[i].index('A')
        if 'B' in AL[i]:
            final_i = i
            final_j = AL[i].index('B')
    solve(n, m, AL)


dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]

ans_dir = {
    "-10": "U",
    "01": "R",
    "0-1": "L",
    "10": "D"
}


def printPath(u):
    global ans_f
    new_p = p[u]
    dir[new_p[0]] = new_p[1]
    if new_p[0] == -1:
        ans_f.append(u)
        return
    printPath(p[u][0])
    ans_f.append(u)


def solve(n, m, AL):
    global final_j, final_i
    global AL_P, path
    path = [[(-1, -1) for a in range(m + 1)] for _ in range(n + 1)]
    vis = [[False for _ in range(m + 1)] for a in range(n + 1)]
    q = deque()
    q.append((start_i, start_j))
    while len(q) > 0:
        cx, cy = q.popleft()
        for d in range(4):
            if (0 <= cx + dx[d] < n and 0 <= cy + dy[d] < m) and not vis[cx + dx[d]][cy + dy[d]] and AL[cx + dx[d]][
                cy + dy[d]] != "#":
                q.append((cx + dx[d], cy + dy[d]))
                vis[cx + dx[d]][cy + dy[d]] = True
                path[cx + dx[d]][cy + dy[d]] = (dx[d], dy[d])

    if not vis[final_i][final_j]:
        print("NO")
        exit(0)
    print("YES")
    ans = []
    while final_i != start_i or final_j != start_j:
        ans.append((path[final_i][final_j]))
        final_i -= ans[-1][0]
        final_j -= ans[-1][1]
    print(len(ans))
    ans.reverse()
    for d in ans:
        new_d = str(d[0]) + str(d[1])
        print(ans_dir[new_d], end='')


if __name__ == "__main__":
    main()
