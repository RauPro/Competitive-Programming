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

input = lambda: sys.stdin.readline().strip()
flush = lambda: sys.stdout.flush()
print = lambda *args, **kwargs: sys.stdout.write(' '.join(map(str, args)) + kwargs.get("end", "\n")) and flush()

sys.setrecursionlimit(100000)


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



def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(ints())
        print(solve(n, a))


def solve(n ,a ):
    compresedn = [a[0]]
    for it in a:
        if it == compresedn[-1]:
            continue
        else:
            compresedn.append(it)
    a = compresedn
    n = len(a)
    #print(compresedn)
    l = 0
    r = 1
    ans = 0
    for i in range(n):
        if ((i >= 1 and a[i-1] > a[i]) or i == 0) and ((i < n-1 and (a[i] < a[i+1]) or i == n-1)):
            ans += 1
    return "NO" if ans > 1 else "YES"


if __name__ == "__main__":
    main()
