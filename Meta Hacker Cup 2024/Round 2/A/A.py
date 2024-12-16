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
    peaks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 121, 232, 343, 454, 565, 676, 787, 898, 12321, 23432, 34543, 45654, 56765,
             67876, 78987, 1234321, 2345432, 3456543, 4567654, 5678765, 6789876, 123454321, 234565432, 345676543,
             456787654, 567898765, 12345654321, 23456765432, 34567876543, 45678987654, 1234567654321, 2345678765432,
             3456789876543, 123456787654321, 234567898765432, 12345678987654321]

    t = int(input())
    for _ in range(t):
        a,b,m = ints()
        count = 0
        for n in peaks:
            if a <= n <= b and n % m == 0:
                count += 1
        print(f'Case #{_+1}: {count}')

def solve(n ,a ):
    pass



if __name__ == "__main__":
    main()
