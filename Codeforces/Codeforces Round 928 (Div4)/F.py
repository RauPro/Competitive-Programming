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


component = 1
uned = 0
directions = [(0,0), (0,2), (1,1), (2,1), (2,2)]
def main():
    t = int(input())
    for _ in range(t):
        n = 7
        M = []
        for i in range(n):
            M.append(input())
        print(solve(n, M))


def validate_X(M, i, j, COLOR):
    global component, uned
    if (i + 2) >= 7 or (j +2 ) >= 7:
        return False
    if M[i][j+2] == 'B' and M[i+1][j+1] == 'B' and M[i+2][j] == 'B' and M[i+2][j+2] == 'B':
        X = [COLOR[i][j] , COLOR[i][j+2] , COLOR[i+1][j+1] , COLOR[i+2][j] , COLOR[i+2][j+2]]
        if COLOR[i][j] or COLOR[i][j+2] or COLOR[i+1][j+1] or COLOR[i+2][j] or COLOR[i+2][j+2]:
            for k in range(len(X)):
                if X[k] != 0:
                    uned += 1
                    COLOR[i][j] = X[k]
                    COLOR[i][j + 2] =  X[k]
                    COLOR[i + 1][j + 1] =  X[k]
                    COLOR[i + 2][j] =  X[k]
                    COLOR[i + 2][j + 2] =  X[k]
                    break
        else:
            COLOR[i][j] = component
            COLOR[i][j + 2] = component
            COLOR[i + 1][j + 1] = component
            COLOR[i + 2][j] = component
            COLOR[i + 2][j + 2] = component
            component += 1
        return True
    return False
def solve(n ,a ):
    global component, uned
    ans = 0
    COLOR = [[0 for i in range(7)] for j in range(7)]
    component = 1
    uned = 0
    for i in range(n):
        for j in range(n):
            if a[i][j] == 'B':
                ans += validate_X(a, i, j, COLOR)
    return ans-uned if uned % 2 !=0 or uned == 0 else ans - (uned-1)
    #print(COLOR)


if __name__ == "__main__":
    main()
