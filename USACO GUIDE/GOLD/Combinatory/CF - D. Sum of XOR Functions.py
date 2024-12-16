# Contribution Technique
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

def main():
    n = int(input())
    a = list(ints())
    s = [0] * (n+1)
    for i in range(n):
        s[i+1] = s[i] ^ a[i]
    ans = 0
    s1 = [[0, 0] for i in range(30)]
    s2 = [[0, 0] for i in range(30)]

    #print(s1, s2)

    for i in range(n+1):
        for j in range(30):
            x = s[i] >> j & 1
            ans += (i * s1[j][not x] - s2[j][not x]) * (1 << j)
            #print(ans)
            s1[j][x] +=1
            s2[j][x] += i
            # print(s1, s2)
    print(ans % MOD)

if __name__ == "__main__":
    main()
