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
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = []
        for i in range(n):
            a.append(list(ints()))
        print(solve(n, a))


def solve(n ,a ):
    ans = []
    for i in range(n):
        min_ = INF
        for j in range(n):
            row = j+i
            col = j
            if row >= n:
                break
            if a[row][col] < 0:
                min_ = min(min_, a[row][col])
        if min_ != INF:
            ans.append(abs(min_))
    for i in range(1, n):
        min_ = INF
        for j in range(n):
            col = j + i
            row = j
            if col >= n:
                break
            if a[row][col] < 0:
                min_ = min(min_, a[row][col])
        if min_ != INF:
            ans.append(abs(min_))
    return sum(ans)



if __name__ == "__main__":
    main()
