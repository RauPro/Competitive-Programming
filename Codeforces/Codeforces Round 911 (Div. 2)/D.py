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

# Para mejorar el rendimiento de la entrada/salida
input = lambda: sys.stdin.readline().strip()
flush = lambda: sys.stdout.flush()
print = lambda *args, **kwargs: sys.stdout.write(' '.join(map(str, args)) + kwargs.get("end", "\n")) and flush()

# Optimización de la recursión para Python
sys.setrecursionlimit(100000)


# Funciones para lectura de múltiples tipos de datos
def ints(): return map(int, input().split())
def strs(): return input().split()
def chars(): return list(input().strip())
def mat(n): return [list(ints()) for _ in range(n)]  # Matriz de n x m donde m es el número de enteros en una línea


# Constantes útiles
INF = float('inf')
MOD = 1000000007  # Modulo por defecto, cambiar si se necesita otro
SIZE = 100001

# Algunas funciones útiles
def add(x, y, mod=MOD): return (x + y) % mod
def sub(x, y, mod=MOD): return (x - y) % mod
def mul(x, y, mod=MOD): return (x * y) % mod


# Fast power - a^b % mod
def powmod(a, b, mod=MOD):
    res = 1
    a = a % mod
    while b > 0:
        if b % 2:
            res = mul(res, a, mod)
        a = mul(a, a, mod)
        b //= 2
    return res


# Inverso multiplicativo de a modulo m (cuando m es primo)
def invmod(a, mod=MOD): return powmod(a, mod - 2, mod)


# GCD y LCM
def lcm(a, b): return a * b // gcd(a, b)


# Factorial con memoización
@lru_cache(maxsize=None)
def factorial(n): return n * factorial(n - 1) if n else 1


# Combinaciones con memoización (nCr)
@lru_cache(maxsize=None)
def comb(n, r):
    if r == 0 or r == n: return 1
    return comb(n - 1, r - 1) + comb(n - 1, r)


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(ints())
        prime_factors = PrimeFactorCalculator(SIZE)
        print(solve(n, a, prime_factors))

class PrimeFactorCalculator:
    def __init__(self, max_number):
        self.factors_of_each_number = [[] for _ in range(max_number + 1)]
        for current_number in range(1, max_number + 1):
            for factor in range(current_number, max_number + 1, current_number):
                self.factors_of_each_number[factor].append(current_number)

def solve(n, numbers, prime_factors):
    frequency_count = Counter(numbers)
    prefix_sum = [0] * (SIZE + 1)
    answer = 0
    remaining_numbers = n
    for i in range(1, SIZE + 1):
        factors_list = prime_factors.factors_of_each_number[i]
        frequency_of_i = frequency_count[i]
        remaining_numbers -= frequency_of_i

        if frequency_of_i:
            number_of_factors = len(factors_list)
            factor_counts = [0] * number_of_factors

            for factor_index in range(number_of_factors - 1, -1, -1):
                factor = factors_list[factor_index]
                current_sum = prefix_sum[factor]

                for k in range(factor_index + 1, number_of_factors):
                    if factors_list[k] % factor == 0:
                        current_sum -= factor_counts[k]

                answer += current_sum * factor * frequency_of_i * remaining_numbers
                answer += current_sum * factor * frequency_of_i * (frequency_of_i - 1) // 2
                factor_counts[factor_index] = current_sum

            answer += frequency_of_i * (frequency_of_i - 1) // 2 * i * remaining_numbers
            answer += frequency_of_i * (frequency_of_i - 1) * (frequency_of_i - 2) // 6 * i

            for factor in factors_list:
                prefix_sum[factor] += frequency_of_i

    return answer



if __name__ == "__main__":
    main()
