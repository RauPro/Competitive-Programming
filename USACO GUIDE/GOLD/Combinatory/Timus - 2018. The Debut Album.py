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

n, a, b = 0, 0, 0


def main():
    global n, a, b
    n, a, b = ints()
    dp1 = [0] * (n + 1)
    dp2 = [0] * (n + 1)
    prefix_a = [0] * (n + 2)
    prefix_b = [0] * (n + 2)
    dp1[0] = dp2[0] = 0
    prefix_a[0] = prefix_b[0] = 0
    dp1[0] = dp2[0] = 1
    prefix_a[1] = dp1[0]
    prefix_b[1] = dp2[0]
    for i in range(1, n + 1):
        l = max(0, i - a)
        r = i - 1
        dp1[i] = (prefix_b[r + 1] % MOD - prefix_b[l] % MOD) % MOD
        prefix_a[i + 1] = (prefix_a[i] % MOD + dp1[i] % MOD) % MOD
        l = max(0, i - b)
        r = i - 1
        dp2[i] = (prefix_a[r + 1] % MOD - prefix_a[l] % MOD) % MOD
        prefix_b[i + 1] = (prefix_b[i] % MOD + dp2[i] % MOD) % MOD
    ans = (dp1[n] % MOD + dp2[n] % MOD) % MOD
    print(ans % MOD)


@lru_cache(maxsize=None)
def solve(i, last, sec):
    if i == n:
        return 1
    if last == -1:
        return (solve(i + 1, 1, 1) % MOD + solve(i + 1, 2, 1) % MOD) % MOD
    ans = solve(i + 1, 3 - last, 1) % MOD
    if (last == 1 and sec < a) or (last == 2 and sec < b):
        ans += solve(i + 1, last, sec + 1) % MOD
    return ans % MOD


if __name__ == "__main__":
    main()
