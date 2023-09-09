dr = (1, 0, -1, 0)
dc = (0, 1, 0, -1)
R, C = 0 , 0
visited = []


def floodfill(r, c, c1, c2,c3, grid):
    global visited
    if (r < 0) or (r >= R) or (c < 0) or (c >= C): return 0
    if grid[r][c] != c1 and grid[r][c] != c2: return 0
    ans = 1
    grid[r][c] = c3
    for d in range(4):
        ans += floodfill(r + dr[d], c + dc[d], c1, c2, c3, grid)
    return ans

if __name__ == "__main__":
    t= int(input())
    for _ in range(t):
        n = int(input())
        grid = []
        for i in range(n):
            grid.append(list(input()))

        ans = 0
        R = n
        C = n
        #print(grid)
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 'x':
                    ans += (floodfill(i, j, 'x','@','.',grid)!= 0)
        print("Case " + str(_+1)+ ":", ans)