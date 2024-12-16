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
from io import BytesIO, IOBase

input = lambda: sys.stdin.readline().rstrip("\r\n")
flush = lambda: sys.stdout.flush()
print = lambda *args, **kwargs: sys.stdout.write(' '.join(map(str, args)) + kwargs.get("end", "\n")) and flush()

sys.setrecursionlimit(100000)

def ints(): return map(int, input().split())


def strs(): return input().split()


def chars(): return list(input().strip())


def mat(n): return [list(ints()) for _ in range(n)]


INF = float('inf')
MOD = 998244353
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


def gcd(x, y):
    """greatest common divisor of x and y"""
    while y:
        x, y = y, x % y
    return x


def distinct_factors(n):
    factors = [1]
    while n > 1:
        p = SPF[n]
        for i in range(len(factors)):
            factors.append(factors[i] * p)
        while n % p == 0:
            n //= p
    return factors

def all_factors(n):
    """returns a sorted list of all distinct factors of n"""
    small, large = [], []
    for i in range(1, int(n**0.5) + 1, 2 if n & 1 else 1):
        if not n % i:
            small.append(i)
            large.append(n // i)
    if small[-1] == large[-1]:
        large.pop()
    large.reverse()
    small.extend(large)
    return small

def mobius_f(n):
    mobius = [0] * (n + 1)
    mobius[1] = -1
    for i in range(1, n + 1):
        if mobius[i]:
            mobius[i] = -mobius[i]
            for j in range(2 * i, n + 1, i):
                mobius[j] += mobius[i]
    return mobius

MAX_N = 1000000
mu  = None

SPF = [0] * (MAX_N + 1)
for i in range(2, MAX_N + 1):
    if SPF[i] == 0:
        SPF[i] = i
        for j in range(i * 2, MAX_N + 1, i):
            if SPF[j] == 0:
                SPF[j] = i
def main():
    global primes, mu
    #sieve(MAX_N)

    n = int(input())
    a = list(ints())
    mu = mobius_f(max(a) + 1)
    print(solve(n, a))


debug = False
def solve(n, a):
    dp = [0] * (MAX_N)

    if debug:print(distinct_factors(a[-1]))
    for it in (distinct_factors(a[-1])):
        if it > 1:
            dp[it] = 1
    ans = 0
    if debug:print(dp[:40])
    for i in range(n - 2, -1, -1):
        ans = 0
        if debug:print(distinct_factors(a[i]))
        for it in distinct_factors(a[i]):
            if it > 1:
                if debug:print(dp[it] * mu[it])
                ans -= (dp[it] %  MOD * mu[it] % MOD) % MOD
        for it in distinct_factors(a[i]):
            if it > 1:
                dp[it] += ans % MOD
    if debug: print(mu[:40])
    return ans % MOD


if __name__ == "__main__":
    main()