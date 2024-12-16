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


def compute_factorials(n, MOD):
    fact = [1] * (n + 1)
    inv_fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = fact[i - 1] * i % MOD
    inv_fact[n] = pow(fact[n], MOD - 2, MOD)
    for i in range(n - 1, -1, -1):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD
    return fact, inv_fact


def binom(n, k, fact, inv_fact):
    if k > n:
        return 0
    if (k == 0 or k == n):
        return 1
    return fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD

def main():
    N = int(input())

    A = set(list(ints())[1:])
    B = set(list(ints())[1:])
    total_numbers = list(range(1, 2 * N + 1))
    S = total_numbers

    dp_current = [0] * (N + 2)
    dp_next = [0] * (N + 2)
    dp_current[0] = 1

    for idx, num in enumerate(S):
        for k in range(N + 1):
            dp_next[k] = 0
        if num in A:
            for k in range(N):
                dp_next[k + 1] = (dp_next[k + 1] + dp_current[k]) % MOD
        elif num in B:
            for k in range(1, N + 1):
                dp_next[k - 1] = (dp_next[k - 1] + dp_current[k]) % MOD
        else:
            for k in range(N):
                dp_next[k + 1] = (dp_next[k + 1] + dp_current[k]) % MOD
            for k in range(1, N + 1):
                dp_next[k - 1] = (dp_next[k - 1] + dp_current[k]) % MOD

        dp_current, dp_next = dp_next, dp_current

    print(dp_current[0] % MOD)

main()