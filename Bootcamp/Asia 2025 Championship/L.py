r, c, n, p = map(int, input().split())
mx = []
start = None
for i in range(r):
    mx.append(list(map(int, input().split())))
    if p in mx[i]:
        start = [i, mx[i].index(p)]
ans = set()
steps = 0
original_p = p
while p != 0:
    if start[0] - 1 >= 0 and mx[start[0] - 1][start[1]] != 0 and mx[start[0] - 1][start[1]]+ steps <= n: ans.add(mx[start[0] - 1][start[1]]+ steps)
    if start[0] + 1 < r and mx[start[0] + 1][start[1]] != 0 and mx[start[0] + 1][start[1]]+ steps <= n: ans.add(mx[start[0] + 1][start[1]]+ steps)
    if start[1] - 1 >= 0 and mx[start[0]][start[1] - 1] != 0 and mx[start[0]][start[1] - 1] + steps <= n: ans.add(mx[start[0]][start[1] - 1] + steps)
    if start[1] + 1 < c and mx[start[0]][start[1] + 1] != 0 and mx[start[0]][start[1] + 1] + steps <= n: ans.add(mx[start[0]][start[1] + 1] + steps)
    if start[0] - 1 >= 0 and mx[start[0] - 1][start[1]] == p - 1:
        start[0] -= 1
    elif start[0] + 1 < r and mx[start[0] + 1][start[1]] == p - 1:
        start[0] += 1
    elif start[1] - 1 >= 0 and mx[start[0]][start[1] - 1] == p - 1:
        start[1] -= 1
    elif start[1] + 1 < c and mx[start[0]][start[1] + 1] == p - 1:
        start[1] += 1
    steps += 1
    p -= 1
print(f"{len(ans) - (original_p in ans)}/{n-1}")
