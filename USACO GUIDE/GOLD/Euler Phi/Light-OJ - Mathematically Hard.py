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


def phi_1_to_n(n):
    phi = list(range(n + 1))

    for i in range(2, n + 1):
        if phi[i] == i:
            for j in range(i, n + 1, i):
                phi[j] -= phi[j] // i

    return phi


def compute_totients_and_scores(max_n):
    phi = list(range(max_n + 1))
    score_sum = [0] * (max_n + 1)

    for i in range(2, max_n + 1):
        if phi[i] == i:  # i is a prime
            for j in range(i, max_n + 1, i):
                phi[j] *= (i - 1)
                phi[j] //= i

    for i in range(2, max_n + 1):
        score = phi[i] * phi[i]
        score_sum[i] = score_sum[i - 1] + score

    return score_sum

def main():
    t = int(input())
    score_sum = compute_totients_and_scores(10000000 + 5)
    ans = []
    for _ in range(t):
        a,b = ints()

        #print(phi[a:b+1])
        ans.append(f"Case {_+1}: {score_sum[b] - score_sum[a - 1]}")
    print('\n'.join(ans))



if __name__ == "__main__":
    main()
