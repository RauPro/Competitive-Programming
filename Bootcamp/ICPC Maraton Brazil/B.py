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
    n,m = ints()
    solve(n,m)

def solve(n, m):
    graph = {}
    for i in range(n):
        movie = list(map(int, input().split()))[1:]
        for j in movie:
            if j not in graph:
                graph[j] = set()
            for k in movie:
                if j != k:
                    graph[j].add((k, i + 1))

    q = int(input())
    for _ in range(q):
        start, end = map(int, input().split())
        visited = set()
        parent = {}
        queue = deque([(start, None)])
        visited.add(start)

        while queue:
            u, _ = queue.popleft()
            if u == end:
                break
            for v, movie in graph.get(u, []):
                if v not in visited:
                    visited.add(v)
                    parent[v] = (u, movie)
                    queue.append((v, movie))

        if end in visited:
            path = []
            u = end
            while u != start:
                path.append(u)
                u, movie = parent[u]
                path.append(movie)
            path.append(start)
            path.reverse()
            print(len(path) // 2 + 1)
            print(*path)
        else:
            print(-1)


if __name__ == "__main__":
    main()
