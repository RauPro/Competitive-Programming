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


def can_place(a,b,c, len_side):
    to_place = [a,b,c]
    chars_ = ["A", "B", "C"]
    index= 0
    matrix = [["z" for j in range(len_side)] for i in range(len_side)]
    for i in range(len_side):
        for j in range(len_side):
            if matrix[i][j] == "z":
                if index == 3: return matrix, False
                for i_ in range(to_place[index][0]):
                    for j_ in range(to_place[index][1]):
                        if i + i_ >= len_side or j + j_ >= len_side:
                            return matrix, False
                        matrix[i+i_][j + j_] = chars_[index]
                index += 1

    return matrix, True


def main():
    rectangles = list(ints())
    area = sum([rectangles[l] * rectangles[l+1] for l in range(0,5, 2)])
    len_side = sqrt(area)
    if ceil(len_side) != floor(len_side):
        print(-1)
        exit(0)
    len_side = int(len_side)
    a_list = [(rectangles[0], rectangles[1]), (rectangles[1], rectangles[0])]
    b_list = [(rectangles[2], rectangles[3]), (rectangles[3], rectangles[2])]
    c_list = [(rectangles[4], rectangles[5]), (rectangles[5], rectangles[4])]

    for a in a_list:
        for b in b_list:
            for c in c_list:
                matrix, can = can_place(a,b,c, len_side)
                if can:
                    print(len_side)
                    for m in matrix:
                        print("".join(m))
                    exit(0)
    print(-1)

if __name__ == "__main__":
    main()
