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

# wx = Wrapper(x)
# cnt[wx] = cnt.get(wx, 0) + 1

def main():
    n, m, q = ints()
    mx = [[0] * (m+1)]
    for i in range(n):
        mx.append([0] + [it == '1' for it in input()])
    #print(mx)
    prefix = [[0] * (m+1) for i in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1] + (1 if mx[i][j] and not mx[i-1][j] and not mx[i][j-1] else
                                                                                 -1 if mx[i][j] and mx[i-1][j] and mx[i][j-1] else 0)
    #print(prefix)
    hor_prefix = [[0] * (m+1) for i in range(n+1)]
    ver_prefix = [[0] * (m + 1) for i in range(n + 1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            hor_prefix[i][j] = hor_prefix[i][j-1] + (mx[i][j] and not mx[i][j-1])
            ver_prefix[i][j] = ver_prefix[i-1][j] + (mx[i][j] and not mx[i-1][j])
    #print(ver_prefix)
    for i in range(q):
        a, b, c, d = ints()
        ans = mx[a][b] + (hor_prefix[a][d] - hor_prefix[a][b]) + (ver_prefix[c][b] - ver_prefix[a][b]) + (
                    prefix[c][d] - prefix[a][d] - prefix[c][b] + prefix[a][b])
        print(ans)
def solve(n ,a ):
    pass



if __name__ == "__main__":
    main()
