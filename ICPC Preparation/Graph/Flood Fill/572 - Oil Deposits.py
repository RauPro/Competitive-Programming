dr = (1, 1, 0, -1, -1, -1, 0, 1)
dc = (0, 1, 1, 1, 0, -1, -1, -1)
R, C = 0, 0
visited = []


def floodfill(r, c, c1, c2, grid):
    global visited
    if (r < 0) or (r >= R) or (c < 0) or (c >= C): return 0
    if grid[r][c] != c1: return 0
    ans = 1
    grid[r][c] = c2
    for d in range(8):
        ans += floodfill(r + dr[d], c + dc[d], c1, c2, grid)
    return ans


if __name__ == "__main__":
    while True:
        m, n = map(int, input().split())
        R = m
        C = n
        if m == 0: break
        grid = []
        for _ in range(m):
            s = list(input())
            grid.append(s)
        deposits = 0
        for i in range(m):
            for j in range(n):
                deposits += (floodfill(i, j, '@', '*', grid) != 0)
        print(deposits)
