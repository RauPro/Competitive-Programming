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
import random

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


#sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)


# endregion

def hopcroft_karp(graph, n, m):
    """
    Maximum bipartite matching using Hopcroft-Karp algorithm, running in O(|E| sqrt(|V|))
    """
    assert (n == len(graph))
    match1 = [-1] * n
    match2 = [-1] * m

    # Find a greedy match for possible speed up
    for node in range(n):
        for nei in graph[node]:
            if match2[nei] == -1:
                match1[node] = nei
                match2[nei] = node
                break
    while 1:
        bfs = [node for node in range(n) if match1[node] == -1]
        depth = [-1] * n
        for node in bfs:
            depth[node] = 0

        for node in bfs:
            for nei in graph[node]:
                next_node = match2[nei]
                if next_node == -1:
                    break
                if depth[next_node] == -1:
                    depth[next_node] = depth[node] + 1
                    bfs.append(next_node)
            else:
                continue
            break
        else:
            break

        pointer = [len(c) for c in graph]
        dfs = [node for node in range(n) if depth[node] == 0]
        while dfs:
            node = dfs[-1]
            while pointer[node]:
                pointer[node] -= 1
                nei = graph[node][pointer[node]]
                next_node = match2[nei]
                if next_node == -1:
                    # Augmenting path found
                    while nei != -1:
                        node = dfs.pop()
                        match2[nei], match1[node], nei = node, nei, match1[node]
                    break
                elif depth[node] + 1 == depth[next_node]:
                    dfs.append(next_node)
                    break
            else:
                dfs.pop()
    return match1, match2


def main():
    n  = int(input())
    a = [None] * (n + 1)
    for i in range(1, n + 1):
        row = list(input())
        a[i] = ["#"] + row
    num = 0
    ans = 0
    X = [0] * (n + 1)
    Y = [0] * (n + 1)
    V = [None]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if a[i][j] != '1':
                continue
            num += 1
            group = []
            group.append(i)
            group.append(j)
            for k in range(1, n + 1):
                if a[i][k] != '0' and a[j][k] != '0':
                    group.append(k)
            V.append(group)
            for u in group:
                for v in group:
                    if u != v:
                        a[u][v] = '2'
            for u in group:
                if X[u] != 0:
                    Y[u] = num
                else:
                    X[u] = num
    AL_CLIQUE = [[] for i in range(100000)]
    for i in range(1, n + 1):
        if X[i] == 0:
            ans += 1
        elif Y[i] != 0:
            AL_CLIQUE[X[i]].append(Y[i])
            AL_CLIQUE[Y[i]].append(X[i])
        else:
            num += 1
            AL_CLIQUE[X[i]].append(num)
            AL_CLIQUE[num].append(X[i])
    n = num
    col = [0] * (n + 1)
    @bootstrap
    def color(u, c):
        if not col[u]:
            col[u] = c
            for v in AL_CLIQUE[u]:
                yield color(v, 3 - c)
        yield

    for u in range(1, n + 1):
        if col[u] == 0:
            color(u, 1)
    AL = [[] for _ in range(n + 1)]
    for u in range(1, n + 1):
        if col[u] == 1:
            for v in AL_CLIQUE[u]:
                if col[v] == 2:
                    AL[u].append(v)
    #print(AL, n+1)
    #print(hopcroft_karp(AL, n+1, n+1)[0])
    # print(ans + sum(1 for it in hopcroft_karp(AL, n+1, n+1)[1] if it != -1))
    match = [-1] * (n + 1)
    freeV = set()
    for L in range( n +  1):
        freeV.add(L)
    vis = []
    MCBM = 0
    def Aug(L):
        if vis[L]:
            return 0
        vis[L] = 1
        for R in AL[L]:
            if match[R] == -1 or Aug(match[R]):
                match[R] = L
                return 1
        return 0

    for L in range(n + 1):
        candidates = []
        for R in AL[L]:
            if match[R] == -1:
                candidates.append(R)
        if len(candidates) > 0:
            MCBM += 1
            freeV.remove(L)
            a = random.randrange(len(candidates))
            match[candidates[a]] = L

    for f in freeV:
        vis = [0] * (n + 1)
        MCBM += Aug(f)

    print(ans +  MCBM)
if __name__ == "__main__":
    main()
