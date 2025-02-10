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

def flood_fill(board, x, y, visited, stone_type):
    if not (0 <= x < 9 and 0 <= y < 9):
        return 0, None, True
    if visited[x][y]:
        return 0, None, True
    if board[x][y] != '.':
        return 0, None, True
    queue = [(x, y)]
    territory = [(x, y)]
    visited[x][y] = True
    border_stones = set()
    while queue:
        curr_x, curr_y = queue.pop(0)
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_x, new_y = curr_x + dx, curr_y + dy
            if 0 <= new_x < 9 and 0 <= new_y < 9:
                if board[new_x][new_y] == '.':
                    if not visited[new_x][new_y]:
                        queue.append((new_x, new_y))
                        territory.append((new_x, new_y))
                        visited[new_x][new_y] = True
                else:
                    border_stones.add((board[new_x][new_y]))
    if len(border_stones) == 1:
        owner = list(border_stones)[0]
        return len(territory), owner, True
    return 0, None, True

def main():
    t = int(input())
    for _ in range(t):
        board = []
        for i in range(9):
            row = list(input())
            board.append(row)
        black_points, white_points = None, None
        visited = [[False for i in range(9)] for j in range(9)]
        black_territory, white_territory = 0, 0
        black_stones, white_stones = 0, 0
        for i in range(9):
            for j in range(9):
                if board[i][j] == 'X':
                    black_stones += 1
                elif board[i][j] == 'O':
                    white_stones += 1
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.' and not visited[i][j]:
                    territory_size, owner, is_valid = flood_fill(board, i, j, visited, '.')
                    if is_valid and owner == 'X':
                        black_territory += territory_size
                    elif is_valid and owner == 'O':
                        white_territory += territory_size
        black_points = black_territory + black_stones
        white_points = white_territory + white_stones
        print(f"Black {black_points} White {white_points}")

def solve(n, a):
    pass

if __name__ == "__main__":
    main()
