from copy import deepcopy

ans = 1
grid = []
grid_acum = []
grid_aux = []

def find_and_replace(cur, c):
    global ans, grid, grid_acum, grid_aux
    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == c:
                acum_ways = 0
                if i > 0 and grid_aux[i-1][j] == cur:
                    grid_aux[i][j] = cur + grid[i][j]
                    acum_ways += grid_acum[i-1][j]
                    total += 1
                if j > 0 and grid_aux[i][j-1] == cur:
                    grid_aux[i][j] = cur + grid[i][j]
                    acum_ways += grid_acum[i][j - 1]
                    total +=1
                if i < len(grid) - 1 and grid_aux[i+1][j] == cur:
                    grid_aux[i][j] = cur + grid[i][j]
                    acum_ways += grid_acum[i + 1][j]
                    total += 1
                if j < len(grid[0]) - 1 and grid_aux[i][j+1] == cur:
                    grid_aux[i][j] = cur + grid[i][j]
                    acum_ways += grid_acum[i][j + 1]
                    total +=1
                if grid[i][j] == c:
                    grid_acum[i][j] = acum_ways




def main():
    global grid, grid_acum, grid_aux
    n, m = map(int, input().split())
    grid = [(list(input())) for i in range(n)]
    grid_aux = deepcopy(grid)
    grid_acum = [[1 if it == 'Y' else 0 for it in grid[i]] for i in range(n)]
    find_and_replace('Y', 'O')
    find_and_replace("YO", 'K')
    find_and_replace("YOK", 'O')
    find_and_replace("YOKO", 'H')
    find_and_replace("YOKOH", 'A')
    find_and_replace("YOKOHA", 'M')
    find_and_replace("YOKOHAM", 'A')
    ans = 0
    for i in range(n):
        for j in range(len(grid[0])):
            if grid_aux[i][j] == "YOKOHAMA":
                ans += grid_acum[i][j]
    #print(grid_aux)
    print(ans)
main()