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
total_cc = 0
visited = []
AL = []

class BitArray:
    """implements bitarray using bytearray"""
    def __init__(self, size):
        self.bytes = bytearray((size >> 3) + 1)

    def __getitem__(self, index):
        return (self.bytes[index >> 3] >> (index & 7)) & 1

    def __setitem__(self, index, value):
        if value:
            self.bytes[index >> 3] |= 1 << (index & 7)
        else:
            self.bytes[index >> 3] &= ~(1 << (index & 7))


def dfs(u):
    global visited, total_cc, memo
    visited[u] = 1
    ans = 1
    for v in AL[u]:
        if not visited[v]:
            ans += dfs(v)
    return ans

def main():
    global visited, total_cc, AL
    n, m = ints()
    mx = [list(ints()) for i in range(n)]
    AL = [[] for i in range(n * m + 5)]
    for i in range(n):
        for j in range(m):
            if i < n - 1:
                if mx[i][j] < mx[i + 1][j]:
                    AL[mx[i][j]].append(mx[i + 1][j])
                else:
                    AL[mx[i + 1][j]].append(mx[i][j])
            if j < m - 1:
                if mx[i][j] < mx[i][j + 1]:
                    AL[mx[i][j]].append(mx[i][j + 1])
                else:
                    AL[mx[i][j + 1]].append(mx[i][j])
    ans = 0
    visited = BitArray(10000 + 1)
    for u in range(n*m):
        ans = max(ans, dfs(u))
        #total_cc = 0
        #visited = BitArray(10000 + 1)
    print(ans)


if __name__ == "__main__":
    main()
