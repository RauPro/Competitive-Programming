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

class min_cost_max_flow:
  def __init__(self, V):
    self.V = V
    self.EL = []
    self.AL = [list() for _ in range(V)]
    self.vis = [False] * V
    self.total_cost = 0
    self.d = None
    self.last = None

  def SPFA(self, s, t):
    self.d = [INF] * self.V
    self.d[s] = 0
    self.vis[s] = True
    q = [s]
    while len(q) != 0:
      u = q[0]
      q.pop(0)
      self.vis[u] = False
      for idx in self.AL[u]:
        v, cap, flow, cost = self.EL[idx]
        if cap-flow > 0 and self.d[v] > self.d[u]+cost:
          self.d[v] = self.d[u]+cost
          if not self.vis[v]:
            q.append(v)
            self.vis[v] = True
    return self.d[t] != INF

  def DFS(self, u, t, f=INF):
    if u == t or f == 0:
      return f
    self.vis[u] = True
    for i in range(self.last[u], len(self.AL[u])):
      v, cap, flow, cost = self.EL[self.AL[u][i]]
      if not self.vis[v] and self.d[v] == self.d[u]+cost:
        pushed = self.DFS(v, t, min(f, cap-flow))
        if pushed != 0:
          self.total_cost += pushed * cost
          flow += pushed
          self.EL[self.AL[u][i]][2] = flow
          rv, rcap, rflow, rcost = self.EL[self.AL[u][i]^1]
          rflow -= pushed
          self.EL[self.AL[u][i]^1][2] = rflow
          self.vis[u] = False
          self.last[u] = i
          return pushed
    self.vis[u] = False
    return 0

  def add_edge(self, u, v, w, c, directed=True):
    if u == v:
      return
    self.EL.append([v, w, 0, c])
    self.AL[u].append(len(self.EL)-1)
    self.EL.append([u, 0 if directed else w, 0, -c])
    self.AL[v].append(len(self.EL)-1)

  def mcmf(self, s, t):
    mf = 0
    while self.SPFA(s, t):
      self.last = [0] * self.V
      f = self.DFS(s, t)
      while f != 0:
        mf += f
        f = self.DFS(s, t)
    return mf, self.total_cost

def main():
    case_= 1
    ans = []
    while True:
        try:
            n, m = ints()
            mfmc = min_cost_max_flow(511)
            mfmc.add_edge(505, 1, 2, 0)
            mfmc.add_edge(n, 510, 2, 0)
            for i in range(m):
                u, v, d, a = ints()
                mfmc.add_edge(u, v, 1, d)
                mfmc.add_edge(u, v, 1, d + a)
            ans.append(f"Case {case_}: {mfmc.mcmf(505, 510)[1]}")
            case_ += 1
        except:
            break
    print("\n".join(ans))
if __name__ == "__main__":
    main()
