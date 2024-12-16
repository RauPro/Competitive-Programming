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
    b = list(ints())
    a_ans = []
    for i in range(n):
        a_ans.append(((a[i] * ((n-i) * (i +1))), i))
    a_ans.sort()
    b.sort(reverse=True)
    b_ans = [0] * n

    for i in range(n):
        #print(a_ans[i][1])
        b_ans[a_ans[i][1]] = b[i]
    #print(a, b_ans)
    ans = 0
    for i in range(n):
        ans += a[i] * b_ans[i] * ((n-i) * (i +1))
        #print(a[i], b_ans[i])
    print(ans % MOD)

if __name__ == "__main__":
    main()
