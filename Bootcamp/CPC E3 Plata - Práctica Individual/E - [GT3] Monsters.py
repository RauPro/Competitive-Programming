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

input = lambda: sys.stdin.readline().strip()
flush = lambda: sys.stdout.flush()
print = lambda *args, **kwargs: sys.stdout.write(' '.join(map(str, args)) + kwargs.get("end", "\n")) and flush()

# Optimización de la recursión para Python
sys.setrecursionlimit(100000)


# Funciones para lectura de múltiples tipos de datos
def ints(): return map(int, input().split())

def is_valid_move(x, y, n, m, grid, visited):
    return 0 <= x < n and 0 <= y < m and grid[x][y] != '#' and not visited[x][y]


def find_path(n, m, grid):
    moves = [(0, 1, 'R'), (0, -1, 'L'), (1, 0, 'D'), (-1, 0, 'U')]
    start = None
    monsters = deque()
    visited = [[False] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'A':
                start = (i, j)
            elif grid[i][j] == 'M':
                monsters.append((i, j))
                visited[i][j] = True

    queue = deque([(*start, '')])
    visited[start[0]][start[1]] = True

    while queue:
        x, y, path = queue.popleft()

        if x == 0 or x == n - 1 or y == 0 or y == m - 1:
            return ("YES", len(path), path)

        for dx, dy, d in moves:
            nx, ny = x + dx, y + dy
            if is_valid_move(nx, ny, n, m, grid, visited):
                visited[nx][ny] = True
                queue.append((nx, ny, path + d))

    return ("NO",)


# Ejemplo de uso
n, m = 5, 8
grid = [
    "########",
    "#M..A..#",
    "#.#.M#.#",
    "#M#..#..",
    "#.######"
]

resultado = find_path(n, m, grid)


if __name__ == "__main__":
    n, m = ints()
    grid = []
    for i in range(n):
        grid.append(list(input()))

    ans = 0
    R = n
    C = m
    # print(grid)
    ans = find_path(n, m, grid)
    if ans[0] == "YES":
        print(ans[0])
        print(ans[1])
        print(ans[2])
    else:
        print(ans[0])