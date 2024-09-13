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

def main():
    n = int(input())
    a = list(ints())
    b = list(ints())
    print(solve(n, a, b))

def can(m, n, a, b):
    y0 = a[0] + b[0] * m
    x0 = max(0, a[0] - b[0] * m)
    for i in range(1, n):
        x1 = a[i] - b[i] * m
        y1 = a[i] + b[i] * m
        if x1 > y0 or y1 < x0:
            return False
        x0 = max(x0, x1)
        y0 = min(y0, y1)
    return True


def solve(n ,a , b):
    lo, hi = 0, 1e9
    #print(can(1.4, n, a, b))
    for i in range(100):
        delta = (hi-lo) / 3
        m1 = lo + delta
        m2 = hi - delta
        if can(m1, n, a, b):
            hi = m2
        else:
            lo = m1

    return (hi)



if __name__ == "__main__":
    main()
