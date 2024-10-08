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
    t = int(input())
    for _ in range(t):
        n, k = ints()
        a = list(ints())
        print(solve(n, a, k))

def all_lights_on_at_time(time, a, k):
    for ai in a:
        if (time - ai) % (2 * k) >= k or time < ai:
            return False
    return True

def solve(n ,a , k):
    left, max_time = 0, max(a)
    low, lo = 0, 0
    high, hi = 2 * k - 1, 2 * k - 1
    for i in range(n):
        time = (max_time - a[i]) // k
        parity = True
        if time % 2:
            parity = False
        curr_time = k - ((max_time - a[i]) % k)
        if parity:
            high = min(high, curr_time - 1)
            lo = max(lo, curr_time + k)
        else:
            low = max(low, curr_time)
            hi = min(hi, curr_time + k - 1)
    lo = max(lo, low)
    high = min(high, hi)
    return -1 if low > high and lo > hi else low + max_time if low <= high else lo + max_time




if __name__ == "__main__":
    main()
