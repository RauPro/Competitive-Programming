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



input = lambda: sys.stdin.readline().strip()


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
from bisect import bisect_left as lower_bound
from bisect import bisect_right as upper_bound


def main():
    t = int(input())
    res = []
    for _ in range(t):
        n, m, l = ints()
        seg = []
        for i in range(n):
            a, b = ints()
            seg.append((a,b))
        curr = 0
        curr_pow = 1
        ans = 0
        pq = []
        powers = []
        no_ans = False
        heapify(pq)
        for i in range(m):
            index, power = ints()
            powers.append((index, power))
        pointer_powers = 0
        for l, r in seg:
            to_pass = r-l + 2
            if pointer_powers < len(powers):
                #print(pointer_powers)
                while pointer_powers < len(powers) and powers[pointer_powers][0] < l:
                    heappush(pq, -powers[pointer_powers][1])
                    pointer_powers += 1
            if curr < n:
                while curr_pow < to_pass:
                    if len(pq) == 0:
                        no_ans = True
                        break
                    ans += 1
                    curr_pow += -heappop(pq)
                curr += 1
        res.append(ans if not no_ans else -1)
    print("\n".join(map(str, res)))

if __name__ == "__main__":
    main()
