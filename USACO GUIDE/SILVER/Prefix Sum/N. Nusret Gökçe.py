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
    n, m = ints()
    a = list(ints())
    for i in range(n):
        if i == 0:
            if a[i] < a[i + 1] and a[i + 1] - a[i] > m:
                a[i] = a[i + 1] - m
        elif i == n - 1:
            if a[i] < a[i - 1] and a[i - 1] - a[i] > m:
                a[i] = a[i - 1] - m
        else:
            max_side = max(a[i + 1], a[i - 1])
            if a[i] < max_side and max_side - a[i] > m:
                a[i] = max_side - m
    for i in range(n-1, -1, -1):
        if i == 0:
            if a[i] < a[i + 1] and a[i + 1] - a[i] > m:
                a[i] = a[i + 1] - m
        elif i == n - 1:
            if a[i] < a[i - 1] and a[i - 1] - a[i] > m:
                a[i] = a[i - 1] - m
        else:
            max_side = max(a[i + 1], a[i - 1])
            if a[i] < max_side and max_side - a[i] > m:
                a[i] = max_side - m


    #ans = a if m != 0 else ([max(a)] * n)
    print(*a)

def solve(n ,a ):
    pass



if __name__ == "__main__":
    main()
