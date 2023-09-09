dr = (1, 1, 0, -1, -1, -1, 0, 1)
dc = (0, 1, 1, 1, 0, -1, -1, -1)
R, C = 5, 5
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
    t = int(input())
    input()
    for _ in range(t):
        grid = []

        while True:
            try:
                line = input().strip()
                if not line:
                    break
                grid.append([int(cell) for cell in line])
            except EOFError:
                # This is to handle if there's no blank line after the last grid
                break
        #print(grid)
        ans = 0
        R = len(grid)
        for i in range(R):
            C = len(grid[i])
            for j in range(C):
                ans = max(floodfill(i, j, 1, 0, grid), ans)
        #print(grid)
        print(ans)
        if _ != t-1:
            print()