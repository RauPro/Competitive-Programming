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

def can_visited_all(i, j,n,m, dir, total, mx):
    #dir
    # i + 1 -> N
    # i - i -> S
    # j + 1 -> W
    # j - 1 -> E
    visited = set()
    mirrors = set()
    while 0 <= i < n  and 0 <= j < m:
        if (i,j, dir) in visited and mx[i][j] != '.':
            break
        if mx[i][j] != '.' and (i,j) not in mirrors:
            total -= 1
        visited.add((i, j,dir))
        if mx[i][j] != '.':
            mirrors.add((i, j))

        if mx[i][j] == '/' and dir == 'N': # -> E
            dir = 'E'
            j-=1
        elif mx[i][j] == '/' and dir == 'E': # -> N
            dir = 'N'
            i+=1
        elif mx[i][j] == '/' and dir == 'W': # -> S
            dir = 'S'
            i-=1
        elif mx[i][j] == '/' and dir == 'S': # -> W
            dir = 'W'
            j+=1
        elif mx[i][j] == '\\' and dir == 'N': # -> W
            dir = 'W'
            j+=1
        elif mx[i][j] == '\\' and dir == 'E': # -> S
            dir = 'S'
            i-=1
        elif mx[i][j] == '\\' and dir == 'W': # -> N
            dir = 'N'
            i+=1
        elif mx[i][j] == '\\' and dir == 'S': # -> E
            dir = 'E'
            j-=1
        elif mx[i][j] == '.' and dir == 'S':
            i-=1
        elif mx[i][j] == '.' and dir == 'N':
            i+=1
        elif mx[i][j] == '.' and dir == 'E':
            j-=1
        elif mx[i][j] == '.' and dir == 'W':
            j+=1
    return total == 0

def main():
    n, m = ints()
    mx = []
    total = 0
    for i in range(n):
        mx.append(input())
        total += mx[i].count('/')
        total += mx[i].count('\\')
    #print(can_visited_all(1, 0, n, m, 'W', total, mx))
    north = []
    for i in range(m):
        if can_visited_all(0, i, n, m, 'N', total, mx):
            north.append(i + 1)
    south =  []
    for i in range(m):
        if can_visited_all(n - 1, i, n, m, 'S', total, mx):
            south.append(i + 1)

    east = []
    for i in range(n):
        if can_visited_all(i, m - 1, n, m, 'E', total, mx):
            east.append(i + 1)

    west = []
    for i in range(n):
        if can_visited_all(i, 0, n, m, 'W', total, mx):
            west.append(i + 1)
    #print(north, south, east, west)
    ans = []
    for it in north:
       ans.append('N' + str(it))
    for it in south:
       ans.append('S' + str(it))
    for it in west:
       ans.append('W' + str(it))
    for it in east:
       ans.append('E' + str(it))
    print(len(ans))
    print(' '.join(ans))
if __name__ == "__main__":
    main()
