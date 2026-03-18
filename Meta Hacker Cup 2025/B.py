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

def can(h, n, a):
    i = 0
    while i < n:
        flag = False
        j = i
        while True:
            if a[j] <= h:
                flag = True
            if j + 1 >= n or abs(a[j + 1] - a[j]) > h:
                break
            j += 1
        if not flag:
            return False
        i = j + 1
    return True

def solve(n, a):
    lo = 0
    hi = 10**9 + 7
    ans = hi
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if can(mid, n, a):
            ans = mid
            hi = mid - 1
        else:
            lo = mid + 1
            
    return ans

def main():
    t = int(input())
    for i in range(1, t + 1):
        n = int(input())
        a = list(ints())
        print(f"Case #{i}: {solve(n, a)}")

if __name__ == "__main__":
    main()