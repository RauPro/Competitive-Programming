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

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        n+=1
        AL = [[] for i in range(n)]
        colored = [0] * n
        a, b= ints()
        colored[a] = 1
        for i in range(n-2):
            u,v = ints()
            AL[u].append((v))
            AL[v].append((u))
        solve(n, AL, b, a, colored)


def bfs_meet_in_middle(graph, start_a, start_b):
    queue_a = deque([start_a])
    queue_b = deque([start_b])
    visited_a = set([start_a])
    visited_b = set([start_b])
    steps = 0
    def expand(queue, visited_this, visited_other):
        for _ in range(len(queue)):
            current = queue.popleft()
            for neighbor in graph[current]:
                if neighbor in visited_other:
                    return True, neighbor
                if neighbor not in visited_this:
                    visited_this.add(neighbor)
                    queue.append(neighbor)
        return False, None
    while queue_a and queue_b:
        found, meeting_point = expand(queue_a, visited_a, visited_b)
        if found:
            return steps + 1, meeting_point
        found, meeting_point = expand(queue_b, visited_b, visited_a)
        if found:
            return steps + 1, meeting_point

        steps += 1

    return -1, None

ans = -1
visited = []
res = 0

def dfs(u, AL, counts):
    global ans, visited, res
    visited[u] = True
    counts['ida'] += 1
    ans+=1
    #print(f"Visitando {u} (Ida)", ans)
    if counts['ida'] == n-1:
        res = ans
        return
    for neighbour in AL[u]:
        if not visited[neighbour]:
            dfs(neighbour, AL, counts)

    counts['regreso'] += 1
    ans += 1
    #print(f"Regresando de {u} (Regreso)", ans)


def bfs(graph, start, n):
    visited = [False] * n
    queue = deque([start])
    counts = {'descubierto': 0, 'procesado': 0}
    visited[start] = True
    counts['descubierto'] += 1
    #print(f"Descubriendo {start}")

    while queue:
        node = queue.popleft()
        counts['procesado'] += 1
        #print(f"Procesando {node}")
        for neighbour in graph[node]:
            if not visited[neighbour]:
                visited[neighbour] = True
                queue.append(neighbour)
                counts['descubierto'] += 1
                #print(f"Descubriendo {neighbour}")

    return sum(list(counts.values()))-1
def solve(n ,AL, s, d, colored):
    steps, s = bfs_meet_in_middle(AL, s, d)
    if steps == -1:
        s = d
    #dfs(s, AL, counts)
    #print((counts["ida"] + counts["regreso"]) - steps)
    cr = bfs(AL, s,n )
    print(cr - steps if steps != -1 else cr - 1)



if __name__ == "__main__":
    main()
