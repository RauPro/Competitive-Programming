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

segments = set()
n = 0
res = 0

@lru_cache(maxsize=None)
def ways_(rem):
    global res
    if rem > n:
        return 0
    if rem == n:
        return 1
    total = 0
    for i in segments:
        total += ways(rem + i)  % 998244353
        #print(total, rem)
    return total % 998244353

def main():
    global segments, n
    n, m = ints()
    segments = []
    prefix = [0] * (n + 2)
    ways = [0] * (n + 2)
    for i in range(m):
        a, b = ints()
        segments.append((b+1, a))
    prefix[1] = 1
    ways[1] = 1
    for i in range(2, n+1):
        for j in range(m):
            l, r = segments[j]
            l = max(0, i - l)
            r = max(0, i- r)
            ways[i] = ways[i]  % 998244353 + (prefix[r] - prefix[l])  % 998244353
        prefix[i] = (ways[i] + prefix[i-1]) % 998244353
    print(ways[n] % 998244353)



if __name__ == "__main__":
    main()
