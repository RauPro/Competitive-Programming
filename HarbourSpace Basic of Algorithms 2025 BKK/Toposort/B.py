import sys
from types import GeneratorType
from collections import deque
input = lambda: sys.stdin.readline().rstrip("\r\n")
flush = lambda: sys.stdout.flush()
print = lambda *args, **kwargs: sys.stdout.write(' '.join(map(str, args)) + kwargs.get("end", "\n")) and flush()
def ints(): return map(int, input().split())
def strs(): return input().split()
def chars(): return list(input().strip())
def mat(n): return [list(ints()) for _ in range(n)]

def main():
    n, m = ints()
    grid = [list(input()) for _ in range(n)]
    dxdy = [(-1,0), (1,0), (0,-1), (0,1)]
    q = deque()
    for i in range(n):
        for j in range(m):
            if (i == 0 or i == n-1 or j == 0 or j == m-1) and grid[i][j] == '.':
                grid[i][j] = '#'
                q.append((i, j, 0))
    while q:
        x, y, d = q.popleft()
        for dx, dy in dxdy:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < n and 0 <= ny < m) or grid[nx][ny] != '.' and grid[nx][ny] != 'X': continue
            if grid[nx][ny] == 'X':
                print(d + 1)
                return
            grid[nx][ny] = '#'
            q.append((nx, ny, d + 1))
    print(-1)

if __name__ == "__main__":
    main()
