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
    n = int(input())
    a = list(ints())

    left = [-1] * n
    stack = []
    for i in range(n):
        while stack and a[stack[-1]] <= a[i]:
            stack.pop()
        if stack:
            left[i] = stack[-1]
        stack.append(i)
    #print(left)

    right = [-1] * n
    stack = []
    for i in range(n-1, -1, -1):
        while stack and a[stack[-1]] <= a[i]:
            stack.pop()
        if stack:
            right[i] = stack[-1]
        stack.append(i)
    #print(right)
    prefix_sum = [0]
    for i in range(n):
        prefix_sum.append(prefix_sum[-1] + a[i])

    max_area = 0
    for i in range(n):
        if left[i] != -1 and right[i] != -1:
            height = min(a[left[i]], a[right[i]])
            width = right[i] - left[i] - 1
            area = (height * width) - (prefix_sum[right[i]] - prefix_sum[left[i] + 1])
            max_area = max(max_area, area)
    print(max_area)



def solve(n ,a ):
    pass



if __name__ == "__main__":
    main()
