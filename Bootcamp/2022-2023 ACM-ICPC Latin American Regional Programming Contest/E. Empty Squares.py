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
    n, k, e = ints()
    mapper = defaultdict(int)
    for it in range(1, n + 1):
        mapper[it] = (it) // 2 if it % 2 == 0 else (it + 1) // 2
    for i in range(k, n + 1):
        if k + k == i:
            continue
        mapper[i] -= 1
    r = n - (e + k)
    if mapper[e] == 0 and e != 0:
        e-=1
    if e!= 0:
        for i in range(e, n+1):
            if e + e == i or e + k == i:
                continue
            mapper[i] -= 1
    ans = r
    for i in range(r, -1, -1):
        ans = i
        if mapper[i] > 0:
            break
    assert (n - k - e - ans) <= 3
    print(n - k - e - ans)




if __name__ == "__main__":
    main()
