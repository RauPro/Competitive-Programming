n = int(input())
m = int(input())

mat = [input() for _ in range(n)]
memo = [[-1] * m for _ in range(n)]


def paths(i, j):
    if i == 0 and j == 0:
        return 1
    if mat[i][j] == '#':
        return 0
    if memo[i][j] != -1:
        return memo[i][j]
    ans = 0
    if i - 1 >= 0:
        ans += paths(i - 1, j)
    if j - 1 >= 0:
        ans += paths(i, j - 1)
    memo[i][j] = ans
    return ans


print(paths(n - 1, m - 1))
