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
from itertools import accumulate, combinations_with_replacement

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
n=  0
def main():
    global n
    t = int(input())
    ans_ = []
    for _ in range(t):
        n = int(input())
        ans_.append(solve(n))
    print("\n".join(ans_))


@lru_cache(maxsize=None)
def dfs(pos, diff_mod11):
    if pos > n:
        if diff_mod11 % 11 == 0:
            return ''
        else:
            return None
    elif pos == n:
        d = 6
        if pos % 2 == 1:
            new_diff_mod11 = (diff_mod11 + d) % 11
        else:
            new_diff_mod11 = (diff_mod11 - d) % 11
        res = dfs(pos + 1, new_diff_mod11)
        if res is not None:
            return str(d) + res
        else:
            return None
    else:
        for d in ['3', '6']:
            digit = int(d)
            if pos % 2 == 1:
                new_diff_mod11 = (diff_mod11 + digit) % 11
            else:
                new_diff_mod11 = (diff_mod11 - digit) % 11
            res = dfs(pos + 1, new_diff_mod11)
            if res is not None:
                return d + res
        return None
def solve(n):
    ans = dfs(1, 0)
    dfs.cache_clear()
    return ans if ans is not None else "-1"

if __name__ == "__main__":
    main()
