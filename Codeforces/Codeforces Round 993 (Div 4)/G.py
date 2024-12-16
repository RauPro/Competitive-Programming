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

UNVISITED = -1
def main():
    global a
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(ints())
        print(solve(n, a))

dfsNumberCounter = 0
numSCC = 0
AL = []
AL_T = []
dfs_num = []
dfs_low = []
S = []
visited = []
st = []
in_cycle = []
a  = []

def tarjanSCC(u):
    global dfsNumberCounter, numSCC
    dfs_num[u] = dfs_low[u] = dfsNumberCounter
    dfsNumberCounter += 1
    st.append(u)
    visited[u] = True
    for v in AL[u]:
        if dfs_num[v] == UNVISITED:
            tarjanSCC(v)
        if visited[v]:
            dfs_low[u] = min(dfs_low[u], dfs_low[v])
    if dfs_low[u] == dfs_num[u]:
        # Found an SCC
        numSCC += 1
        scc = []
        while True:
            v = st.pop()
            visited[v] = False
            scc.append(v)
            if u == v:
                break
        if len(scc) > 1 or a[u] == u:
            for node in scc:
                #print(node)
                in_cycle[node] = True

def solve(n ,a ):
    global dfs_low, dfs_num, dfsNumberCounter, visited, AL, AL_T, in_cycle, numSCC, st
    a = [it - 1 for it in a]
    AL = [[] for i in range(n)]
    AL_T = [[] for _ in range(n)]
    for i in range(n):
        AL[i].append(a[i])
        AL_T[a[i]].append(i)
    dfs_num = [UNVISITED] * n
    dfs_low = [0] * n
    visited = [False] * n
    st = []
    dfsNumberCounter = 0
    numSCC = 0
    in_cycle = [False] * n
    for v in range(n):
        if dfs_num[v] == UNVISITED:
            tarjanSCC(v)
    dist = [INF] * n
    q = deque()

    for i in range(n):
        if in_cycle[i]:
            dist[i] = 0
            q.append(i)
    while q:
        u = q.popleft()
        for v in AL_T[u]:
            if dist[v] == INF:
                dist[v] = dist[u] + 1
                q.append(v)
    ans = max([d for d in dist if d != INF], default=0)
    #print(ans, "ANS")
    return ans  + 2
if __name__ == "__main__":
    main()
