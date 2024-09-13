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


class DisjointSetUnion:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.num_sets = n

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a != b:
            if self.size[a] < self.size[b]:
                a, b = b, a

            self.num_sets -= 1
            self.parent[b] = a
            self.size[a] += self.size[b]

    def set_size(self, a):
        return self.size[self.find(a)]

    def __len__(self):
        return self.num_sets


def hash(a, b, m):
    return m * a + b

def can(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

dx = [1, 1, 0, -1, -1, -1, 0, 1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]


def main():
    t = int(input())
    for _ in range(t):
        n, m = ints()
        mx = [input() for _ in range(n)]
        print(solve(n, m, mx))



def solve(n, m, mx):
    uf = DisjointSetUnion(n * m)
    components = 0
    for x in range(n):
        for y in range(m):
            if mx[x][y] == '*':
                components+=1
            for d in range(8):
                nx, ny = x + dx[d], y + dy[d]
                if can(nx, ny,n, m) and mx[x][y] == mx[nx][ny]:
                    uf.union(hash(x, y, m), hash(nx, ny, m))
    cc = [[] for i in range(n * m + 5)]
    for v in range(n * m):
        cc[uf.find(v)].append(v)
    for x in range(n):
        for y in range(m):
            v = hash(x, y, m)
            if mx[x][y] == '.':
                continue
            if uf.size[uf.find(v)] != 3:
                return "NO"
            X, Y = zip(*[(c // m, c % m) for c in cc[uf.find(v)]])
            X, Y = sorted(set(X)), sorted(set(Y))
            if len(X) != 2 or len(Y) != 2 or X[1] - X[0] != 1 or Y[1] - Y[0] != 1:
                return "NO"
    return "YES"


if __name__ == "__main__":
    main()
