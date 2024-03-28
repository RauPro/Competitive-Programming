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


INF = float('inf')
MOD = 1000000007  # Modulo por defecto, cambiar si se necesita otro


def add(x, y, mod=MOD): return (x + y) % mod


def sub(x, y, mod=MOD): return (x - y) % mod


def mul(x, y, mod=MOD): return (x * y) % mod


dr = (1, 0, -1, 0)
dc = (0, 1, 0, -1)
R, C = 0, 0
grid = []


def floodfill(r, c, c2):
    global visited, grid
    ans = grid[r][c]
    grid[r][c] = c2
    for d in range(4):
        if 0 <= r + dr[d] < R and 0 <= c + dc[d] < C and grid[r + dr[d]][c + dc[d]] != c2:
            ans += floodfill(r + dr[d], c + dc[d], c2)
    return ans


def main():
    global R, C, grid
    t = int(input())
    for _ in range(t):
        n, m = ints()
        R = n
        C = m
        grid = []
        for i in range(n):
            grid.append(list(ints()))
        print(solve(n, m))


def solve(n, m):
    ans = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] != 0:
                ans = max(ans, floodfill(i, j, 0))
    return (ans)

if __name__ == "__main__":
    main()
