import os
import sys

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

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(ints())
        print(solve(n, a))

def isSpecial(a, k):
    l = 0
    r = 1
    sum_ = a[0]
    while l < r and r < len(a):
        sum_ += a[r]
        if sum_ > k:
            sum_ -= a[l]
            l += 1
            if r-l != 0:
                if sum_ == k:
                    return True
                sum_ -= a[r]
            else:
                r += (r - l == 0)
            continue
        if sum_ == k:
            return True
        if sum_ < k:
            r += 1

    return False
def solve(n ,a ):
    ans = 0
    for it in a:
        ans+=isSpecial(a, it)
    return ans



if __name__ == "__main__":
    main()
