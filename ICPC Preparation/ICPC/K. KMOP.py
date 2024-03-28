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


def isVowel(c):
    return c in "AEIOUY"


def vowel_index(s):
    for i in range(len(s)):
        if isVowel(s[i]):
            return i + 1
    return len(s)


def main():
    n = int(input())
    words = []
    for _ in range(n):
        words.append(input())
    if len(words) < 3:
        print(len(words))
    else:
        last = ''
        ans = 0
        counter_c = 0
        for i in range(len(words)):
            if i == n - 1:
                ans += 1
                break
            index_i1 = vowel_index(words[i])
            index_i2 = 0
            index_i3 = 0
            if i < n - 1:
                index_i2 = vowel_index(words[i + 1])
            if i < n - 2:
                index_i3 = vowel_index(words[i + 2])
            last = isVowel(words[i][0])
            if not last:
                if i < n - 2 and counter_c == 0:
                    if isVowel(words[i + 2][0]):
                        ans += 1
                        counter_c += 1
                    elif isVowel(words[i + 1][0]) or (len(words[i + 1]) > 1 and isVowel(words[i + 1][1])):
                        ans += 1
                        counter_c += 1
                    elif isVowel(words[i][0]) or (len(words[i]) > 1 and isVowel(words[i][1])) or (
                            len(words[i]) > 2 and isVowel(words[i][2])):
                        ans += index_i1
                        counter_c = 0
                    else:
                        print('*')
                        exit()
                elif i < n - 1:
                    if counter_c == 0 and (
                            isVowel(words[i + 1][0]) or (len(words[i + 1]) > 1 and isVowel(words[i + 1][1]))):
                        ans += 1
                        counter_c += 1
                    elif (isVowel(words[i + 1][0]) and counter_c == 1) or counter_c == 0:
                        ans += 1
                        counter_c += 1
                    elif isVowel(words[i][0]) or (len(words[i]) > 1 and isVowel(words[i][1])) or (
                            len(words[i]) > 2 and isVowel(words[i][2])):
                        ans += index_i1
                        counter_c = 0
                        last = False
                elif isVowel(words[i][0]) or (len(words[i]) > 1 and isVowel(words[i][1])) or (
                        len(words[i]) > 2 and isVowel(words[i][2])):
                    ans += index_i1
                    counter_c = 0
            else:
                ans += 1
                counter_c = 0
            # print(ans)
        print(ans if ans >= n else '*')


if __name__ == "__main__":
    main()
