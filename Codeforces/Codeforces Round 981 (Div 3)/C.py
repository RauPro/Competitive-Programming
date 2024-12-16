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
        n = int(input())
        a = list(ints())
        print(solve(n, a))


def solve(n ,a ):
    #print(current_d)
    for i in range(n//2):
        change_to = n-(i + 1)
        current_ = 0
        current_ += a[i] == a[i+1]
        current_ += a[i] == a[i-1]
        current_ += a[change_to] == a[change_to - 1]
        if change_to != n-1:
            current_ += a[change_to] == a[change_to + 1]
        a[i],a[change_to] = a[change_to], a[i]
        current_a = 0
        current_a += a[i] == a[i + 1]
        current_a += a[i] == a[i - 1]
        current_a += a[change_to] == a[change_to - 1]
        if change_to != n-1:
            current_a += a[change_to] == a[change_to + 1]
        if current_a >= current_:
            a[i], a[change_to] = a[change_to], a[i]

    #print(a)
    current_d = sum(1 for i in range(n-1) if a[i] == a[i+1])
    a[0], a[n-1] = a[n-1], a[0]
    return current_d



if __name__ == "__main__":
    main()
