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
    n, k = ints()
    a = list(ints())
    print(solve(n,k,  a))


def can(a, k, mid, k_):
    sum_ = 0
    total = 0
    for it in a:
        if sum_ + it <= mid:
            sum_ += it
        elif it <= mid:
            total += 1
            sum_ = it
            if total > k_:
                return False
        else:
            return False
    return (total + (sum_ >= 1)) <= k_


def solve(n ,k, a):
    lo, hi = 1, 10e19
    #print(can(a, (len(a)+1) // k, 5, k))
    sub_array_length = (len(a)+1) // k
    while lo < hi:
        mid = (lo + hi) // 2
        if can(a, sub_array_length, mid, k):
            hi = mid
        else:
            lo = mid + 1
    return round(hi)

if __name__ == "__main__":
    main()
