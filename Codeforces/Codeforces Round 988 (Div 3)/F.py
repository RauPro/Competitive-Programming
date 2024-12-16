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

def local_ans(x, y, mod=MOD): return (x + y) % mod
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
# count[wx] = count.get(wx, 0) + 1


def can(mid, n, m, k, h, x):
    local_ans = defaultdict(int)
    for i in range(n):
        r = m - (h[i] + mid- 1) // mid
        lower_bound = x[i] - max(0, r)
        local_ans[lower_bound] += 1
        upper_bound = x[i] + max(0, r) + (1 if r >= 0 else 0)
        local_ans[upper_bound] -= 1
    kill = 0
    for p in sorted(local_ans.keys()):
        kill += local_ans[p]
        if kill >= k:
            return True

    return False


def main():
    t = int(input())
    res = []
    for _ in range(t):
        n, m, k = ints()
        h = list(ints())
        x = list(ints())
        lo, hi, ans = 1, int(1e9), -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if can(mid, n, m, k, h, x):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        res.append(str(ans))
    print("\n".join(res))



if __name__ == "__main__":
    main()