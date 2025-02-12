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
    n = int(input())
    nums = list(ints())
    prefix_num = []
    suffix_num = []
    cur = 0
    for i in range(n):
        if nums[i] != 0:
            cur = nums[i]
        prefix_num.append(cur)
    cur = 0
    for i in range(n-1, -1, -1):
        if nums[i] != 0:
            cur = nums[i]
        suffix_num.append(cur)
    suffix_num.reverse()
    in_array = Counter(nums)
    nums_to_take = [it for it in range(n, 0, -1) if it not in in_array]

    prefix_distance = []
    suffix_distance = []
    dist = 0
    for i in range(n):
        if nums[i] == 0:
            dist += 1
        else:
            dist = 0
        prefix_distance.append(dist)
    dist = 0
    for i in range(n-1, -1, -1):
        if nums[i] == 0:
            dist += 1
        else:
            dist = 0
        suffix_distance.append(dist)
    suffix_distance.reverse()
    #print(suffix_num, prefix_num, nums_to_take)
    #print(prefix_distance, suffix_distance)
    left = 0
    right = n-1
    ans = [0] * n
    cur = 0
    while left <= right:
        cur += 1
        if nums[left] == cur:
            ans[left] = cur
            left+=1
        elif nums[right] == cur:
            ans[right] = cur
            right -= 1
        elif suffix_num[left] < prefix_num[right] and suffix_distance[left] > 0 and cur not in in_array:
            ans[left] = cur
            left +=1
        elif prefix_num[right] != suffix_num[left]  and prefix_distance[right] > 0 and cur not in in_array:
            ans[right] = cur
            right -=1
        elif prefix_num[right] < suffix_num[left] and nums[right] != 0:
            ans[left] = cur
            left += 1
        elif prefix_num[right] == suffix_num[left]:
            if suffix_distance[left] > prefix_distance[right] > 0 or suffix_distance[left] == 0:
                ans[right] = cur
                right -=1
            else:
                ans[left] = cur
                left +=1
        else:
            break
    def check(ans):
        one_m = 0
        for i in range(n-1):
            if ans[i] > ans[i+1]:
                one_m = i
                break
        return (ans.count(0) == 0 and
                (all(ans[i] > ans[i+1] for i in range(one_m, n-1)) or
                all (ans[i] < ans[i+1] for i in range(n-1))) and all(ans[i] == nums[i] for i in range(n) if nums[i] != 0))
    #print(ans)
    print(" ".join(map(str, ans)) if check(ans) else "*")

if __name__ == "__main__":
    main()
