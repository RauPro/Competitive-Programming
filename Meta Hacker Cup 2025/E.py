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


def ints(): return map(int, input().split())


def solve(n, a):
    prefix_xor = [0] * (n + 1)
    for i in range(n): prefix_xor[i + 1] = prefix_xor[i] ^ a[i]
    counts = Counter(prefix_xor)
    total_len_sum = n * (n + 1) * (n + 2) // 6
    total_savings = 0
    for v in counts:
        c = counts[v]
        if c > 1:
            total_savings += c * (c - 1) * (c + 1) // 6
    return total_len_sum - total_savings


def main():
    t = int(input())
    for i in range(1, t + 1):
        n = int(input())
        a = list(ints())
        result = solve(n, a)
        print(f"Case #{i}: {result}")


if __name__ == "__main__":
    main()