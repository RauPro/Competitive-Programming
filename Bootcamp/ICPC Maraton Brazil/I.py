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

# wx = Wrapper(x)
# cnt[wx] = cnt.get(wx, 0) + 1

def main():
    n = int(input())
    f = list(ints())
    q = int(input())
    solve(n, f,q)


_sieve_size = 0
bs = []
primes = []


def sieve(upperbound):
    global _sieve_size, bs, primes

    _sieve_size = upperbound + 1
    bs = [True] * 10000010
    bs[0] = bs[1] = False
    for i in range(2, _sieve_size):
        if bs[i]:
            for j in range(i * i, _sieve_size, i):
                bs[j] = False
            primes.append(i)


def isPrime(N):
    global _sieve_size, primes
    if N <= _sieve_size:
        return bs[N]
    for p in primes:
        if p * p > N:
            break
        if N % p == 0:
            return False
    return True


def primeFactors(N):
    global primes

    factors = []
    for p in primes:
        if p * p > N:
            break
        while N % p == 0:
            N //= p
            factors.append(p)
    if N != 1:
        factors.append(N)

    return factors
def solve(n, foods, q):
    sieve(1000001)
    food_prime_factors = [set(primeFactors(food)) for food in foods]
    for i in range(q):
        allergy = int(input())
        allergy_prime_factors = set(primeFactors(allergy))
        ans = [food for food in food_prime_factors if not food & allergy_prime_factors]
        print(pow(2, len(ans), MOD))



if __name__ == "__main__":
    main()
