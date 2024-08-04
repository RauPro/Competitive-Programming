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
    sys.stdin = open('tttt.in', 'r')
    sys.stdout = open('tttt.out', 'w')
    game = []
    for i in range(3):
        game.append(input())
    ans = set()
    for i in range(3):
        aux = list(set(sorted([_ for _ in game[i]])))
        if len(aux) != 3:
            ans.add(''.join(aux))

    for i in range(3):
        aux = list(set(sorted([game[0][i], game[1][i], game[2][i]])))
        if len(aux) != 3:
            ans.add(''.join(aux))
    aux = list(set(sorted([game[0][0], game[1][1], game[2][2]])))
    if len(aux) != 3:
        ans.add(''.join(aux))
    aux = list(set(sorted([game[0][2], game[1][1], game[2][0]])))
    if len(aux) != 3:
        ans.add(''.join(aux))
    ans_solo = 0
    for it in ans:
        if len(it) == 1:
            ans_solo +=1

    print(ans_solo)
    print(len(ans) - ans_solo)
if __name__ == "__main__":
    main()
