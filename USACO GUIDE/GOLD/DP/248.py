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


#sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)



# endregion


def main():
    #sys.stdin = open('248.in', 'r')
    #sys.stdout = open('248.out', 'w')
    n = int(input())
    a = [int(input()) for i in range(n)]
    print(solve(n, a))


def solve(n ,a ):
    """@lru_cache(maxsize=None)
    def dfs(i, j):
        if i == j:
            return a[i]
        max_val = 0
        for k in range(i, j):
            left = dfs(i, k)
            right = dfs(k + 1, j)
            max_val = max(max_val, left, right)
            if left == right:
                max_val = max(max_val, left + 1)
        return max_val
    return dfs(0, n - 1)"""
    """dp = [[0 for i in range(n)]  for _ in range(n)]
    for i in range(n):
        dp[i][i] = a[i]
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = max(dp[i][k] for k in range(i, j))
            for k in range(i, j):
                if dp[i][k] == dp[k + 1][j]:
                    dp[i][j] = max(dp[i][j], dp[i][k] + 1)
    return max(max(row) for row in dp)"""

    """@lru_cache(maxsize=None)
    def dp(i, j):
        if i == j:
            return a[i]
        merged = -1
        for k in range(i, j):
            left = dp(i, k)
            right = dp(k + 1, j)
            if left != -1 and left == right:
                merged = left + 1
                break  # You can remove break if you want the smallest k
        return merged

    max_val = -1
    for i in range(n):
        for j in range(i, n):
            current = dp(i, j)
            if current > max_val:
                max_val = current

    return (max_val)"""
    dp = [[-1 for _ in range(n)] for _ in range(n)]

    ans = 0
    for length in range(1, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if i == j:
                dp[i][j] = a[i]
            else:
                for k in range(i, j):
                    if dp[i][k] != -1 and dp[i][k] == dp[k + 1][j]:
                        dp[i][j] = dp[i][k] + 1
                        break
            ans = max(ans, dp[i][j])

    return (ans)

if __name__ == "__main__":
    main()
