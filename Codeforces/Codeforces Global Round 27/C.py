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
        a = [0] * n
        if n & 1:
            print(n)
            a[n - 1], a[n - 2], a[n - 3], a[n - 4] = n, n - (n & (-n)), ((n & (-n)) + (2 if n & (-n) == 1 else 1)), n & (-n)
        else:
            pow_ = 2 ** n.bit_length() - 1
            print(pow_, )
            if n == 2 ** (n.bit_length() - 1):
                a[n - 1], a[n - 2], a[n - 3], a[n - 4], a[n - 5] = n, n - 1, n - 2, 3, 1
            else:
                a[n - 1], a[n - 2], a[n - 3] = 2 ** (n.bit_length() - 1) - 1, n - 1, n

        mapper = Counter(a)
        index = 0
        for i in range(1, n + 1):
            if i not in mapper:
                a[index] = i
                index += 1
        print(*a)


if __name__ == "__main__":
    main()
