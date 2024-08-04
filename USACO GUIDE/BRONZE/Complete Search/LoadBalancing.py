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
    sys.stdin = open('balancing.in', 'r')
    sys.stdout = open('balancing.out', 'w')
    n, = ints()
    cows = []
    for i in range(n):
        a,b = ints()
        cows.append((a,b))
    #print(cows)
    x_values = sorted([x for x,y in cows])
    y_values = sorted([y for x,y in cows])
    best_M = INF
    for i in range(n-1):
        for j in range(n-1):
            a = (x_values[i] + x_values[i + 1]) // 2
            b = (y_values[j] + y_values[j + 1]) // 2
            q1 = q2 = q3 = q4 = 0
            if a % 2 != 0:
                a += 1
            if b % 2 != 0:
                b += 1
            for x, y in cows:
                if x < a and y < b:
                    q1 += 1
                elif x < a and y > b:
                    q2 += 1
                elif x > a and y < b:
                    q3 += 1
                elif x > a and y > b:
                    q4 += 1
            M = max(q1, q2, q3, q4)
            best_M = min(best_M, M)
    print(best_M)


if __name__ == "__main__":
    main()
