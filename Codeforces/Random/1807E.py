import os
import sys
from itertools import accumulate
from io import BytesIO, IOBase
from types import GeneratorType

input = lambda: sys.stdin.readline().rstrip("\r\n")
flush = lambda: sys.stdout.flush()
print = lambda *args, **kwargs: sys.stdout.write(' '.join(map(str, args)) + kwargs.get("end", "\n")) and flush()

sys.setrecursionlimit(100000)

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        solve(n, a)

def solve(n, a):
    prefix_sum = [0] + list(accumulate(a))
    lo = 0
    hi = n
    while lo < hi:
        mid = (lo + hi) // 2
        piles = [it + 1 for it in range(lo, mid + 1)]
        k = len(piles)
        print("?", k, *piles)
        ans = int(input())
        expected = prefix_sum[mid + 1] - prefix_sum[lo]
        if ans == expected:
            lo = mid + 1
        else:
            hi = mid
    print("!", lo + 1)

if __name__ == "__main__":
    main()