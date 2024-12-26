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
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(ints())
        print(solve(n, a))

def minmax_kadane(a):
    prefix = min_pref = max_pref = 0
    min_kadane, max_kadane = INF, -INF
    for it in a:
        prefix += it
        max_kadane, min_kadane = max(max_kadane, prefix - min_pref), min(min_kadane, prefix - max_pref)
        min_pref, max_pref = min(min_pref, prefix), max(max_pref, prefix)
    return min(min_kadane, 0), max(max_kadane, 0)

def suffix_(a):
    if len(a) == 0: return 0, 0
    prefix = [0] + list(accumulate(a))
    total = prefix[-1]
    min_pref, max_pref = INF, -INF
    for i in range(len(a) + 1):
        min_pref = min(min_pref,  prefix[i])
        max_pref = max(max_pref, prefix[i])
    return total - max_pref, total - min_pref

def prefix_(a):
    if not a: return 0, 0
    prefix = min_pref = max_pref = 0
    for x in a:
        prefix += x
        min_pref = min(min_pref, prefix)
        max_pref = max(max_pref, prefix)
    return min_pref, max_pref

def solve(n, a):
    res = []
    pos =  next((i for i, v in enumerate(a) if v not in (-1, 1)), -1)
    if pos == -1:
        l, r = minmax_kadane(a)
        res.append(str(r - l + 1))
        res.append(" ".join(map(str, range(l, r + 1))) + " ")
    else:
        x = a[pos]
        left, right = a[:pos], a[pos + 1:]
        l_min, l_max = minmax_kadane(left)
        r_min, r_max = minmax_kadane(right)
        l_suffix, r_suffix = suffix_(left)
        l_prefix, r_prefix = prefix_(right)
        intervals = sorted([(l_min, l_max), (r_min, r_max), (l_suffix + x + l_prefix, r_suffix + x + r_prefix)])
        merged = []
        cur_start, cur_end = intervals[0]
        for l, r in intervals[1:]:
            if l <= cur_end + 1:
                cur_end = max(cur_end, r)
            else:
                merged.append((cur_start, cur_end))
                cur_start, cur_end = l, r
        merged.append((cur_start, cur_end))
        res.append(str(sum(e - s + 1 for s, e in merged)))
        res.append(" ".join(str(it) for interval in merged for it in range(interval[0], interval[1]+1)))
    return "\n".join(res)

if __name__ == "__main__":
    main()
