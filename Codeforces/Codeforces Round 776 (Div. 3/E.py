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
        input()
        input()
        n, d = ints()
        a = list(ints())
        print(solve(n,d,a))


def calculate_mu(exam_days, d):
    # Calcula el valor de μ para una configuración dada
    new_exam_days = exam_days.copy()
    new_exam_days.sort()
    print(new_exam_days)
    current_mus = [new_exam_days[0] - 1] + [abs(new_exam_days[i] - new_exam_days[i + 1]) - 1 for i in range(0, len(new_exam_days)-2)] + [abs(new_exam_days[-2] - new_exam_days[-1]) -1]
    #print("Mus:", current_mus)
    return min(current_mus)

def backtrack(exam_days, d, current_index):
    if current_index == len(exam_days):
        print(exam_days)
        print(calculate_mu(exam_days, d))
        return 0

    original_day = exam_days[current_index]
    for day in range(1, d + 1):
        exam_days[current_index] = day
        backtrack(exam_days, d, current_index + 1)
        exam_days[current_index] = original_day


def solve(n, d,exam_days):
    return backtrack(exam_days, d, 0)


if __name__ == "__main__":
    main()
