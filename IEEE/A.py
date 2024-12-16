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
from enum import Enum

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
starts = []
visited = []


AL = []
dfs_num = []
ts = []
DAG = []

class flag(Enum):
  UNVISITED = -1
  VISITED = -2

def toposort(u):
  global AL
  global dfs_num
  global ts
  global DAG

  dfs_num[u] = flag.VISITED.value
  for v in DAG[u]:
    if dfs_num[v] == flag.UNVISITED.value:
      toposort(v)
  ts.append(u)

depth_list = []
def main():
    global starts, AL, visited, dfs_num, DAG, ts
    n = int(input())
    starts = list(ints())
    AL = [[] for i in range(n+1)]
    for i in range(n-1):
        u, v = ints()
        AL[u].append(v)
        AL[v].append(u)
    DAG = [[] for i in range(n+1)]
    for u in range(1, n+1):
        for v in AL[u]:
            if starts[u-1] < starts[v-1]:
                DAG[u].append(v)
            elif starts[v-1] > starts[u-1]:
                DAG[v].append(u)

    visited = [False] * (n+1)
    dfs_num = [flag.UNVISITED.value] * (n+1)
    for u in range(1, n+1):
        if dfs_num[u] == flag.UNVISITED.value:
            toposort(u)
    ts = ts[::-1]
    dp = [1] * (n+1)
    print(ts)
    for u in ts:
        for v in DAG[u]:
            if dp[u] > dp[v] + 1:
                dp[u] += dp[v] + 1

    print(dp)


def solve(n ,a ):
    pass



if __name__ == "__main__":
    main()
