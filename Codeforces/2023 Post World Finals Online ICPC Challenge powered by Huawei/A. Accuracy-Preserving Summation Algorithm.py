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

def check_condition(x):
    exp = 0
    if x == 0.0:
        return 0.0, exp
    while abs(x) >= 1.0:
        x /= 2.0
        exp += 1
    while abs(x) < 0.5:
        x *= 2.0
        exp -= 1
    return x, exp

def sum_sequence(seq):
    result = {'type': '', 'val': []}
    if len(seq) == 1:
        result['type'] = 'd'
        result['val'].append(1)
    elif len(seq) == 2:
        result['type'] = 'd'
        result['val'].extend([1, 2])
    elif len(seq) == 3:
        result['type'] = 'd'
        result['val'].extend([1, 2, 3])
    else:
        for factor in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]:
            if len(seq) % factor == 0:
                result['type'] = 'd'
                result['val'].extend(list(range(1, len(seq) + 1)))
                break
        else:
            result['type'] = 'f'
            sum_val = 0.0
            for i in seq:
                value, exp = check_condition(i)
                sum_val += value
                result['val'].append(exp)
            result['val'].append(int(sum_val))
    return result


def solve():
    in_ = list(map(float, input().split()))
    seq = in_[1:]

    result = sum_sequence(seq)

    print(f"{{{result['type']}:", end='')
    print(",".join(map(str, result['val'])), end='}\n')



if __name__ == "__main__":
    solve()




