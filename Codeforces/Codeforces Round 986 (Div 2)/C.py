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

def can(n,m,v, mid, a, prefix, mapper):
    l, r = None, None
    for i in range(1, n+1):
        if prefix[i] - mid in mapper:
            r = i
            l = mapper[prefix[i] - mid]
    if r is None and l is None:
        return False
    sum_ = 0
    ans = 0
    for i in range(n):
        if i < l or i > r:
            sum_ += a[i]
            if sum_ >= v:
                ans+=1
                sum_ = 0
        else:
            sum_ = 0
    return ans >= m
def main():
    t = int(input())
    for _ in range(t):
        n, m, v = ints()
        a = list(ints())
        prefix = [0] * (n+1)
        cur = 0
        for i,it in enumerate(a):
            cur += it
            prefix[i+1] = prefix[i]
            if cur >= v:
                prefix[i + 1] = prefix[i] + 1
                cur = 0
        ans = 0
        prefix_sum = [0] + list(accumulate(a))
        for i, it in enumerate(prefix):
            if it == m:
                ans = max(ans, prefix_sum[n] - prefix_sum[i])
                break
        suffix = [0] * (n+1)
        cur = 0
        for i,it in enumerate(reversed(a)):
            cur += it
            suffix[i+1] = suffix[i]
            if cur >= v:
                suffix[i + 1] = suffix[i] + 1
                cur = 0
        suffix.reverse()
        mapper = {it: i for i, it in enumerate(suffix)}
        for i in range(n+1):
            x = m - prefix[i]
            if x in mapper:
                ans = max(ans, prefix_sum[mapper[x]] - prefix_sum[i])
        print(ans if suffix[0] >= m else -1)

if __name__ == "__main__":
    main()
