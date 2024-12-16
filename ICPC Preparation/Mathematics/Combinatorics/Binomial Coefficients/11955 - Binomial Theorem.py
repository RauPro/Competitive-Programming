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

factors = []


def factorization(n):
    global factors
    factors[0] = 0
    factors[1] = 1
    for i in range(2, n + 1):
        factors[i] = i * factors[i - 1]


def bin_coeff(n):
    c = [[0 for i in range(n)] for i in range(n)]
    for n_ in range(1, n):
        c[n_][0] = c[n_][n_] = 1
        for k in range(1, n_):
            c[n_][k] = c[n_ - 1][k - 1] + c[n_-1][k]
    return c

def main():
    c = bin_coeff(51)
    t = int(input())
    for _ in range(t):
        s = list(input().split("+"))
        a = s[0][1:]
        s = s[1].split('^')
        b = s[0][:-1]
        exp = int(s[1])
        #print(a, b, exp)
        s = ""
        for k in range(exp+1):
            if k == 0:
                s += a + ("^" + str(exp - k) if exp - k > 1 else "")
            elif k == exp:
                s += b + ("^" + str(k) if k > 1 else "")
            elif k != 0:
                s += str(c[exp][k]) +"*" if c[exp][k] != 1 else ""
                if k == 1:
                    s += a + ("^" + str(exp - k) if exp - k > 1 else "") + "*"
                    s += b
                else:
                    s += a + ("^" + str(exp - k) if exp - k > 1 else "") + "*"
                    s+= b + "^" + str(k)
            s+="+"
        print(f"Case {_+1}: {s[:-1]}")

if __name__ == "__main__":
    main()
