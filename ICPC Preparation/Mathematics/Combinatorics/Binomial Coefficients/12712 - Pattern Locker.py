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
MOD = 10000000000007
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

factors = []
inv = []

def factorization(n):
    global factors, inv
    factors = [1] * (n + 1)
    inv = [1] * (n + 1)
    for i in range(2, n + 1):
        factors[i] = (i * factors[i - 1])
        inv[i] = modInverse(factors[i], MOD)


def extEuclid(a, b):
    xx, yy = 0, 1
    x, y = 1, 0
    while b != 0:
        q = a//b
        a, b = b, a%b
        x, xx = xx, x-q*xx
        y, yy = yy, y-q*yy
    return a, x, y

def mod(a, m):
  return ((a % m) + m) % m
def modInverse(b, m):
    d, x, y = extEuclid(b, m)
    if d != 1:
        return -1
    return mod(x, m)

def nPr(n, k):
    if n < k:
        return 0
    if n == k:
        return factors[n]
    return (factors[n] * inv[n - k]) % MOD
    return (factors[n] // factors[n - k])
def main():
    global factors
    #max_ = 100 * 100 + 1
    #factors = [0] * max_
    #factorization(max_ - 1)
    t = int(input())
    res = []
    for _ in range(t):
        n, min_, max_ = ints()
        ans = 1
        n = n*n
        total = 0
        for i in range(1, min_):
            ans *= (n-i + 1)
            ans %= MOD
        for i in range(min_, max_ + 1):
            ans *= (n-i + 1)
            ans %= MOD
            total += ans % MOD
        res.append(f"Case {_+1}: {total % MOD}")
    print("\n".join(res))


if __name__ == "__main__":
    main()
