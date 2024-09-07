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



def main():
    t = int(input())
    for _ in range(t):
        b = list(ints())
        a = list(ints())
        print(solve(a, b))

def can(mid, a, c, d, n):
    return (sum(a[i % mid] for i in range(d) if i % mid < n)) >= c
def solve(a, b):
    n = b[0]
    c = b[1]
    d = b[2]
    a.sort()
    if a[-1]*d < c:
        return "Impossible"

    a.reverse()
    if sum(a[:d]) >= c:
        return "Infinity"

    ans = 0

    l = 1
    h = d
    #print(can(2, a, c, d))
    while l < h:
        mid = (l+h) // 2
        if can(mid, a, c, d, n):
            l = mid + 1
            ans = mid
        else:
            h = mid
    return(ans-1 if ans != 0 else 0)



if __name__ == "__main__":
    main()
