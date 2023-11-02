"""
3 4 4 3
0 1 2 0
1 0 2 0
0 1 2 0
0 1 2 2
4 2 3 4
1 0 3
2 1 2
8 4 2 1
0 7
1 6
2 5
3 4
0 0 0 0
"""
import copy
input = __import__('sys').stdin.readline
def make_battle(grid, h):
    grid_mirror = copy.deepcopy(grid)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for direction in directions:
                if 0 <= i + direction[0] < len(grid) and 0 <= j + direction[1] < len(grid[0]):
                    if grid[i + direction[0]][j + direction[1]] == grid[i][j] + 1:
                        grid_mirror[i + direction[0]][j + direction[1]] = grid[i][j]
                    elif grid[i][j] == h - 1 and grid[i + direction[0]][j + direction[1]] == 0:
                        grid_mirror[i + direction[0]][j + direction[1]] = grid[i][j]


    #print(grid_mirror, grid)
    return grid_mirror


if __name__ == "__main__":
    while True:
        h, r, c, k = map(int, input().split())
        if h == r == c==k == 0:
            break
        grid = []
        for _ in range(r):
            grid.append(list(map(int, input().split())))
        for _ in range(k):
            grid = make_battle(grid, h)
        for i in range(len(grid)):
            print(*grid[i])
