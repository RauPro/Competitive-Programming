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
from io import BytesIO, IOBase
from types import GeneratorType
from enum import Enum
input = lambda: sys.stdin.readline().rstrip("\r\n")
flush = lambda: sys.stdout.flush()
print = lambda *args, **kwargs: sys.stdout.write(' '.join(map(str, args)) + kwargs.get("end", "\n")) and flush()

sys.setrecursionlimit(100000)

def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        to = f(*args, **kwargs)
        while True:
            if type(to) is GeneratorType:
                stack.append(to)
                to = next(to)
            else:
                stack.pop()
                if not stack:
                    break
                to = stack[-1].send(to)
        return to

    return wrappedfunc


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



# region fastio

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._file = file
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)


# endregion


def main():
    while True:
        n, m = ints()
        if n == m == 0: break
        AL = [[] for i in range(n)]
        for i in range(m):
            u, v = ints()
            AL[u].append(v)
            AL[v].append(u)

        class flag(Enum):
            UNVISITED = -1

        dfs_num = []
        dfs_low = []
        dfs_parent = []
        articulation_vertex = []
        dfsNumberCounter = 0
        dfsRoot = 0
        rootChildren = 0
        ans = []
        def articulationPointAndBridge(u):
            nonlocal AL
            nonlocal dfs_num, dfs_parent, dfs_low, articulation_vertex
            nonlocal dfsNumberCounter, dfsRoot, rootChildren

            dfs_low[u] = dfs_num[u] = dfsNumberCounter
            dfsNumberCounter += 1
            for (v) in AL[u]:
                if dfs_num[v] == flag.UNVISITED.value:
                    dfs_parent[v] = u
                    if u == dfsRoot:
                        rootChildren += 1

                    articulationPointAndBridge(v)

                    if dfs_low[v] >= dfs_num[u]:
                        articulation_vertex[u] = True
                    if dfs_low[v] > dfs_num[u]:
                        ans.append(u)
                        ans.append(v)
                    dfs_low[u] = min(dfs_low[u], dfs_low[v])
                elif v != dfs_parent[u]:
                    dfs_low[u] = min(dfs_low[u], dfs_num[v])
        V = n
        dfs_num = [flag.UNVISITED.value] * V
        dfs_low = [0] * V
        dfs_parent = [-1] * V
        articulation_vertex = [False] * V
        dfsNumberCounter = 0
        for u in range(V):
            if dfs_num[u] == flag.UNVISITED.value:
                dfsRoot = u
                rootChildren = 0
                articulationPointAndBridge(u)
        ans = [len(ans) // 2] + ans
        print(*ans)

if __name__ == "__main__":
    main()
