dr = (1, 0, -1, 0)
dc = (0, 1, 0, -1)
R, C = 0, 0
visited = False

al = 0
usable = []


def floodfill(r, c, c1, c2, c3, grid):
    global visited
    if (r < 0) or (r >= R) or (c < 0) or (c >= C): return 0
    if grid[r][c] != c1 and grid[r][c] != c2 and grid[r][c] != 'P': return 0
    # if visited and grid[r][c] == '.': return 0
    ans = 0
    if grid[r][c] == 'G':
        # visited = True
        ans += 1
    grid[r][c] = c3
    if usable[r][c]:
        for d in range(4):
            ans += floodfill(r + dr[d], c + dc[d], c1, c2, c3, grid)
    return ans


if __name__ == "__main__":
    while True:
        try:
            w, h = map(int, input().split())
            R = h
            C = w
            grid = []
            for _ in range(h):
                grid.append(list(input()))
            ans = 0
            indexR = 0
            indexC = 0
            usable = [[True for p in range(C)] for q in range(R)]
            for r in range(h):
                for c in range(w):
                    for d in range(4):
                        indexc = c + dc[d]
                        indexr = r + dr[d]
                        if (indexr < 0) or (indexr >= R) or (indexc < 0) or (indexc >= C): continue
                        if grid[indexr][indexc] == 'T': usable[r][c] = False

            for i in range(h):
                for j in range(w):
                    if grid[i][j] == 'P':
                        indexC = j
                        indexR = i
                    elif grid[i][j] == 'T':
                        grid[i][j] = '#'

            al = floodfill(indexR, indexC, 'G', '.', "#", grid)
            print(al)

        except ValueError:
            break
