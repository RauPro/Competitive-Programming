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
    moves = [(0, 1, 'L'), (0, -1, 'R'), (1, 0, 'U'), (-1, 0, 'D')]
    start = None
    points = []
    ans = ("NO",)
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'A':
                start = (i, j)
            elif (i == 0 or i == n - 1 or j == 0 or j == m - 1) and grid[i][j] == '.':
                points.append((i, j))
    if len(points) == 0 and (start[0] == 0 or start[0] == n - 1) and (start[1] == 0 or start[1] == m - 1):
        ans = ("YES", 0)
    for end_x, end_y in points:
        queue = deque([(end_x, end_y, '')])
        visited = [[False] * m for _ in range(n)]
        visited[end_x][end_y] = True
        current_path = int(1e9)
        if ans[0] == "YES":
            break
        while queue:
            x, y, path = queue.popleft()
            if grid[x][y] == 'A' and current_path != -1:
                ans = ("YES", len(path), path)
                # print(path)
                current_path = len(path)
                # break
            if grid[x][y] == 'M':
                if current_path == int(1e9) or current_path == len(path):
                    current_path = -1
                    ans = ("NO",)
                    break
            for dx, dy, d in moves:
                nx, ny = x + dx, y + dy
                if is_valid_move(nx, ny, n, m, grid, visited):
                    visited[nx][ny] = True
                    queue.append((nx, ny, path + d))
    # print(m_l)
    return ans


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
        if ans[1] != 0:
            print(ans[2][::-1])
    else:
        print(ans[0])