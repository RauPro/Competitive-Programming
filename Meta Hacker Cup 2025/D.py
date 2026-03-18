import os
import sys
from collections import *
from heapq import *
from math import gcd

input = lambda: sys.stdin.readline().rstrip("\r\n")
flush = lambda: sys.stdout.flush()
print = lambda *args, **kwargs: sys.stdout.write(' '.join(map(str, args)) + kwargs.get("end", "\n")) and flush()
sys.setrecursionlimit(100000)
def ints(): return map(int, input().split())
MOD = 10**9 + 7

MAX_EXP = 60 
fact = [1] * (MAX_EXP + 1)
invfact = [1] * (MAX_EXP + 1)
for i in range(1, MAX_EXP + 1):
    fact[i] = (fact[i - 1] * i) % MOD
invfact[MAX_EXP] = pow(fact[MAX_EXP], MOD - 2, MOD)
for i in range(MAX_EXP - 1, -1, -1):
    invfact[i] = (invfact[i + 1] * (i + 1)) % MOD

def nCr_mod_small_k(n, k, mod=MOD):
    if k < 0: return 0
    if k > MAX_EXP: return 0

    n_mod = n % mod
    numerator = 1
    for i in range(k):
        term = (n_mod - i + mod) % mod
        numerator = (numerator * term) % mod
    return (numerator * invfact[k]) % mod

def memodict(f):
    class memodict(dict):
        def __missing__(self, key):
            ret = self[key] = f(key)
            return ret
    return memodict().__getitem__

def pollard_rho(n):
    if n & 1 == 0: return 2
    if n % 3 == 0: return 3
    s = ((n - 1) & (1 - n)).bit_length() - 1
    d = n >> s
    for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
        p = pow(a, d, n)
        if p == 1 or p == n - 1 or a % n == 0: continue
        for _ in range(s):
            prev = p
            p = (p * p) % n
            if p == 1: return gcd(prev - 1, n)
            if p == n - 1: break
        else:
            x, y, c = 2, 2, 1
            while True:
                x = (x * x + c) % n
                y = (y * y + c) % n
                y = (y * y + c) % n
                f = gcd(abs(x - y), n)
                if f == 1: continue
                if f != n: return f
                c += 1
    return n

@memodict
def prime_factors(n):
    if n <= 1: return Counter()
    f = pollard_rho(n)
    return Counter([n]) if f == n else prime_factors(f) + prime_factors(n // f)

total_ways = 0
prime_factors_B = []
N_val, A_val, B_val = 0, 0, 0

def calculate_ways(exponents, N):
    res = 1
    for exp in exponents:
        res = (res * nCr_mod_small_k(N + exp - 1, exp)) % MOD
    return res

def generate_divisors_and_count(k, current_divisor, p1_exponents):
    global total_ways
    if k == len(prime_factors_B):
        p2_exponents = [prime_factors_B[i][1] - p1_exponents[i] for i in range(len(prime_factors_B))]
        ways1 = calculate_ways(p1_exponents, N_val)
        ways2 = calculate_ways(p2_exponents, N_val)
        total_ways = (total_ways + (ways1 * ways2)) % MOD
        return

    p, exp = prime_factors_B[k]
    current_p_power = 1
    for i in range(exp + 1):
        if current_divisor > A_val // current_p_power: break
        p1_exponents.append(i)
        generate_divisors_and_count(k + 1, current_divisor * current_p_power, p1_exponents)
        p1_exponents.pop()
        current_p_power *= p

def solve():
    global total_ways, prime_factors_B, N_val, A_val, B_val
    N_val, A_val, B_val = ints()
    prime_factors.__self__.clear()
    if B_val == 1:
        return 1 if A_val >= 1 else 0
    factors_B = prime_factors(B_val)
    prime_factors_B = sorted(factors_B.items())
    total_ways = 0
    generate_divisors_and_count(0, 1, [])
    return total_ways

def main():
    t = int(input())
    for i in range(1, t + 1):
        ans = solve()
        print(f"Case #{i}: {ans}")

if __name__ == "__main__":
    main()