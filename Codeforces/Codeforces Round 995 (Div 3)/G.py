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


def main():
    n, q = ints()
    a = [strs() for i in range(q)]
    #print(a)
    print(solve(n, q, a))



def solve(n, q, a):
    e = [[0] * (q + 1) for _ in range(n)]
    s = [[0] * (q + 1) for _ in range(n)]
    for j in range(1, q + 1):
        i, g = int(a[j - 1][0]) - 1, a[j - 1][1]
        for k in range(n):
            e[k][j] = e[k][j - 1]
            s[k][j] = s[k][j - 1]
        (e if g == '+' else s)[i][j] += 1
    #print(s, e)
    matching = [[max(e[i][t] + 1 - s[j][t] for t in range(q + 1)) if i != j else 0 for j in range(n)] for i in range(n)]
    size = 1 << n
    dp_min = [[INF] * n for _ in range(size)]
    dp_ans = [[INF] * n for _ in range(size)]
    for last in range(n):
        mask = 1 << last
        dp_min[mask][last] = 1
        dp_ans[mask][last] = 1 + e[last][q]
    for mask in range(1, size):
        for last in range(n):
            if not (mask & (1 << last)):
                continue
            prev_mask = mask ^ (1 << last)
            if prev_mask == 0:
                continue
            for prev in range(n):
                if not (prev_mask & (1 << prev)):
                    continue
                next_min = dp_min[prev_mask][prev]
                next_ans = dp_ans[prev_mask][prev]
                new_min = next_min + matching[prev][last]
                cur = max(next_ans, new_min + e[last][q])
                if cur < dp_ans[mask][last] or (cur == dp_ans[mask][last] and new_min < dp_min[mask][last]):
                    dp_min[mask][last] = new_min
                    dp_ans[mask][last] = cur
    return min(dp_ans[ (1 << n) - 1][last] for last in range(n))

if __name__ == "__main__":
    main()
