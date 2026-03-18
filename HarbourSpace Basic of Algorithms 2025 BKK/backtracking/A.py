import sys
from functools import lru_cache
input = lambda: sys.stdin.readline().rstrip("\r\n")
flush = lambda: sys.stdout.flush()
print = lambda *args, **kwargs: sys.stdout.write(' '.join(map(str, args)) + kwargs.get("end", "\n")) and flush()
def ints(): return map(int, input().split())
def strs(): return input().split()
def chars(): return list(input().strip())
def mat(n): return [list(ints()) for _ in range(n)]
def main():
    n = int(input())
    x, y = map(int, input().split())
    x, y = x-1, y-1
    visited = [[False] * n for _ in range(n)]
    path = []
    moves = [(1,2), (1,-2), (-1,2), (-1,-2), (2,1), (2,-1), (-2,1), (-2,-1)]
    def is_valid(r, c):
        return 0 <= r < n and 0 <= c < n and not visited[r][c]
    def count_neighbors(r, c):
        count = 0
        for dr, dc in moves:
            nr, nc = r + dr, c + dc
            if is_valid(nr, nc):
                count += 1
        return count
    def dfs(r, c, count):
        visited[r][c] = True
        path.append((r, c))
        if count == n*n:
            return True
        next_moves = []
        for dr, dc in moves:
            nr, nc = r + dr, c + dc
            if is_valid(nr, nc):
                next_moves.append((count_neighbors(nr, nc), nr, nc))
        next_moves.sort()
        for _, nr, nc in next_moves:
            if dfs(nr, nc, count + 1):
                return True
        path.pop()
        visited[r][c] = False
        return False
    if dfs(x, y, 1):
        for r, c in path:
            print(r+1, c+1)
    else:
        print("-1")
if __name__ == "__main__":
    main()