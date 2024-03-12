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
UNVISITED = -1

# Optimización de la recursión para Python
sys.setrecursionlimit(1000000000)


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



current_component = 0  # Nuevo global para rastrear el componente actual
ans=0
def kasaraju(u, npass, dfs_num, AL, AL_T, S):
    global id_component, current_component, ans
    dfs_num[u] = 1
    neighbour = AL[u] if npass == 1 else AL_T[u]
    for v in neighbour:
        if dfs_num[v] == UNVISITED:
            kasaraju(v, npass, dfs_num, AL, AL_T, S)
    if npass == 1:
        S.append(u)

def find_root(u,v, AL_T):
    global id_component, current_component, ans
    if id_component[v] != -1:
        return id_component[v] != u
    id_component[v] = u
    #print(id_component)
    in_ = False
    for j in AL_T[v]:
        in_ = find_root(u, j, AL_T) or in_
    return in_
    
def main():
    global id_component, current_component, ans
    n, m = ints()

    AL = [[] for _ in range(n)]
    AL_T=  [[] for _ in range(n)]
    for _ in range(m):
        u, v = ints()
        u -= 1
        v -= 1
        AL[u].append(v)
        AL_T[v].append(u)

    S = []
    
    dfs_num = [UNVISITED] * n
    id_component = [-1] * n
    for u in range(n):
        if dfs_num[u] == UNVISITED:
            kasaraju(u, 1, dfs_num, AL, AL_T, S)

    numSCC = 0
    dfs_num = [UNVISITED] * n
    for i in range(len(S)-1, -1, -1):
        if dfs_num[S[i]] == UNVISITED:
            current_component = S[i]  # Establecer el componente actual antes de comenzar la segunda pasada
            kasaraju(S[i], 2, dfs_num, AL, AL_T, S)
            numSCC += 1  # Incrementar después de procesar un componente
    #print(numSCC)
    #print(id_component)


    scc_out_edges = [0] * n
    for i in range(len(S) - 1, -1, -1):
        if id_component[S[i]] == -1:
            ans += not find_root(S[i], S[i], AL_T)
    print(ans)

if __name__ == "__main__":
    main()
