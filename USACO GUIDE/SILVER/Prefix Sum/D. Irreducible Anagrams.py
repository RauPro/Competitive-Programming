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
    s = input()
    n = int(input())
    prefix_sum = [[0] * 27 for i in range(len(s)+1)]
    #print(prefix_sum)
    for i in range(1, len(s)+1):
        prefix_sum[i] = prefix_sum[i-1].copy()
        prefix_sum[i][ord(s[i-1]) - ord('a')] += 1
    #print(prefix_sum)

    for _ in range(n):
        l, r = ints()
        dif = 0
        for i in range(27):
            dif += 1 if (prefix_sum[r][i] - prefix_sum[l-1][i]) > 0 else 0

        #print(dif)
        print("Yes" if r == l or s[l-1] != s[r-1] or dif > 2 else "No")






if __name__ == "__main__":
    main()
