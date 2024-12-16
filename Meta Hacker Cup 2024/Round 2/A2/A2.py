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

# wx = Wrapper(x)
# cnt[wx] = cnt.get(wx, 0) + 1

def can(s):
    if len(s) % 2 == 0: return False;
    mid = (len(s) + 1) // 2
    s1,s2 = s[:mid], s[mid-1:]
    return all(s1[i+1] >= s1[i] for i in range(mid - 1)) and all(s2[i+1] <= s2[i] for i in range(mid - 1)) and s.count('0') == 0 and s.count(s[len(s) // 2]) == 1

def main():
    t = int(input())
    #print(can('122748322'))
    for _ in range(t):
        a,b,m = ints()
        count = 0
        for n in range(max(1, a), b+1):
            if can(str(n)) and n % m == 0:
                print(n)
                count += 1
        print(f'Case #{_+1}: {count}')

def solve(n ,a ):
    pass



if __name__ == "__main__":
    main()
