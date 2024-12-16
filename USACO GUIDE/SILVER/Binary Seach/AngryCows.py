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
from itertools import accumulate

input = lambda: sys.stdin.readline().strip()
flush = lambda: sys.stdout.flush()
print = lambda *args, **kwargs: sys.stdout.write(' '.join(map(str, args)) + kwargs.get("end", "\n")) and flush()

sys.setrecursionlimit(100000)


def ints(): return map(int, input().split())
def strs(): return input().split()
def chars(): return list(input().strip())
def mat(n): return [list(ints()) for _ in range(n)]

INF = float('inf')
MOD = 1000000007
abcd = "abcdefghijklmnopqrstuvwxyz"

def add(x, y, mod=MOD): return (x + y) % mod
def sub(x, y, mod=MOD): return (x - y) % mod
def mul(x, y, mod=MOD): return (x * y) % mod

def invmod(a, mod=MOD): return powmod(a, mod - 2, mod)

def lcm(a, b): return a * b // gcd(a, b)

RANDOM = getrandbits(32)

class Wrapper(int):
    def __init__(self, x):
        int.__init__(x)
    def __hash__(self):
        return super(Wrapper, self).__hash__() ^ RANDOM

# wx = Wrapper(x)
# cnt[wx] = cnt.get(wx, 0) + 1


def can(a, r, index):
    if a[index] - a[index - 1] > r * 2:
        return False
    n = len(a)
    # Explosión hacia la derecha
    radio = r - 1
    posicion = a[index]
    i = index
    while radio > 0:
        j = i
        # Avanzar lo más posible dentro del radio actual
        while j + 1 < n and a[j + 1] - posicion <= radio:
            j += 1
        if j == i:
            print("I BREACK XD", posicion, a[j], radio)
            break  # No se puede avanzar más hacia la derecha
        posicion = a[j]
        radio -= 1
        i = j
    if i != n - 1:
        print("Return 1", i, index, radio)
        return False  # No se alcanzó el último heno a la derecha

    # Explosión hacia la izquierda
    radio = r - 1
    posicion = a[index - 1]
    i = index - 1
    while radio > 0:
        j = i
        # Avanzar lo más posible dentro del radio actual
        while j - 1 >= 0 and posicion - a[j - 1] <= radio:
            j -= 1
        if j == i:
            break  # No se puede avanzar más hacia la izquierda
        posicion = a[j]
        radio -= 1
        i = j
    if i != 0:
        print("Return 2")
        return False  # No se alcanzó el primer heno a la izquierda

    return True  # Se alcanzaron todos los henos

def main():
    #sys.stdin = open('angry.in', 'r')
    #sys.stdout = open('angry.out', 'w')
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
    a.sort()
    cur_max = 0
    x1, x2 = 0, 0
    index_t = -1
    for i in range(n-1):
        if a[i+1] - a[i] >= cur_max:
            index_t = i + 1
            cur_max = a[i+1] - a[i]
            x1 = a[i]
            x2 = a[i+1]
    #print(x1,  x2)
    target = (x2 + x1) / 2

    q = [0] * n
    for i in range(n):
        if a[i] > target:
            q[i] = i - index_t
        else:
            q[i] = abs(i - index_t) - 1
    print(q)

    print(can(a, 24197.0, index_t))
    print(a[15121:15124])
    """lo, hi = 0, a[-1] + 1
    for i in range(1000):
        delta = (hi - lo) / 3
        m1 = lo + delta
        m2 = hi - delta
        if can(a, m1, index_t):
            hi = m2
        else:
            lo = m1

    print(round(hi, 1), lo)"""




if __name__ == "__main__":
    main()
