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
factorial = []
def factorials(n):
    global factorial
    factorial[0] = 0
    factorial[1] = 1
    for i in range(2, n+1):
        factorial[i] = i * factorial[i-1]

def nCr(n, k):
    if n == k: return 1
    return factorial[n] // (factorial[k] * (factorial[n-k]))
def main():
    global factorial
    n, k = ints()
    factorial = [0] * (n+1)
    ans = 0
    factorials(n)
    #print(factorial)
    for i in range(1, k+1):
        ans += nCr(n, i) * solve(i)
    print(ans + 1)


@lru_cache(maxsize=None)
def solve(n):
    if n == 1: return 0
    if n == 2: return 1
    return (n-1) * (solve(n-1) + solve(n-2))



if __name__ == "__main__":
    main()
