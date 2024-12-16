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
_sieve_size = 0
bs = []
primes = []


def sieve(upperbound):
  global _sieve_size, bs, primes

  _sieve_size = upperbound+1
  bs = [True] * 10000010
  bs[0] = bs[1] = False
  for i in range(2, _sieve_size):
    if bs[i]:
      for j in range(i*i, _sieve_size, i):
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


def numPF(N):
  global primes

  ans = 0
  for p in primes:
    if p * p > N:
      break
    while N % p == 0:
      N //= p
      ans += 1
  if N != 1:
    ans += 1

  return ans


def numDiffPF(N):
  global primes

  ans = 0
  for p in primes:
    if p * p > N:
      break
    if N % p == 0:
      ans += 1
    while N % p == 0:
      N //= p
  if N != 1:
    ans += 1

  return ans


def sumPF(N):
  global primes

  ans = 0
  for p in primes:
    if p * p > N:
      break
    while N % p == 0:
      N //= p
      ans += p
  if N != 1:
    ans += N

  return ans


def numDiv(N):
  global primes

  ans = 1
  for p in primes:
    if p * p > N:
      break
    power = 0
    while N % p == 0:
      N //= p
      power += 1
    ans = ans * (power + 1)
  if N != 1:
    return 2 * ans
  else:
    return ans


def sumDiv(N):
  global primes

  ans = 1
  for p in primes:
    if p * p > N:
      break
    multiplier = p
    total = 1
    while N % p == 0:
      N //= p
      total += multiplier
      multiplier *= p
    ans *= total
  if N != 1:
    ans *= N+1

  return ans


def EulerPhi(N):
  global primes

  ans = N
  for p in primes:
    if p * p > N:
      break
    if N % p == 0:
      ans -= ans // p
    while N % p == 0:
      N //= p
  if N != 1:
    ans -= ans // N

  return ans
def main():
    n = int(input())
    sieve(10000000)
    ans = []
    while n!= 0:
        ans.append(str(EulerPhi(n)))
        n = int(input())
    print('\n'.join(ans))


if __name__ == "__main__":
    main()
