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
        max_L = 0.0
        min_U = float('inf')
        n = int(input())
        for i in range(1, n + 1):
            ai, bi = ints()
            L_i = i / bi
            max_L = max(max_L, L_i)
            if ai > 0:
                U_i = i / ai
                min_U = min(min_U, U_i)
            else:
                pass
        if max_L <= min_U + 1e-9:
            print(f"Case #{_ + 1}: {max_L:.10f}")
        else:
            print(f"Case #{_ + 1}: -1")


def solve(n ,k, a ):
    ans = 0
    a.sort()
    for i in range(1, n):
        if i == n-1:
            ans+=a[0]
        else:
            ans += a[0]*2

    ans += a[0] if n == 1 else 0
    return "YES" if ans <= k else "NO"



if __name__ == "__main__":
    main()
