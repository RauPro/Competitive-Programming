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

def can(mid, x, y, x1, y1, n, s):
    all_contain = mid // n
    for c in s:
        if c == 'U':
            y += 1 * (all_contain)
        if c == 'D':
            y -= 1 * (all_contain)
        if c == 'L':
            x -= 1 * (all_contain)
        if c == 'R':
            x += 1 * (all_contain)

    for i in range(mid % n):
        c = s[i]
        if c == 'U':
            y += 1
        if c == 'D':
            y -= 1
        if c == 'L':
            x -= 1
        if c == 'R':
            x += 1

    return abs(x - x1) + abs(y - y1) <= mid


def main():
    x, y = ints()
    x1, y1 = ints()
    n = int(input())
    s = input()
    lo, hi = 0, int(10e19 + 5)
    ans = -1
    while lo < hi:
        mid = (lo + hi) // 2
        if can(mid, x, y, x1, y1, n, s):
            hi = mid
            ans = hi
        else:
            lo = mid + 1
    print(ans)


if __name__ == "__main__":
    main()
