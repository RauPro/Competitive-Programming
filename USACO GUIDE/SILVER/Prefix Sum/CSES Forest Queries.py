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
    mx = []
    for i in range(n):
        mx.append([1 if it == "*" else 0 for it in input()])
    solve(n,m, mx)


def solve(n ,m,mx ):
    #print(mx)
    prefix_sum = [[0] * (n+1) for i in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            prefix_sum[i][j] = prefix_sum[i-1][j] + prefix_sum[i][j-1] + mx[i-1][j-1] - prefix_sum[i-1][j-1]
    for i in range(m):
        x0, y0, x1, y1= ints()
        print(prefix_sum[x1][y1] - prefix_sum[x1][y0-1] - prefix_sum[x0-1][y1] + prefix_sum[x0-1][y0-1])
    #print(prefix_sum)


if __name__ == "__main__":
    main()
