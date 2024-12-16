n, m = map(int, input().split())
AM = [[int(1e9 + 5) for j in range(n)] for i in range(n)]
EL = []
for i in range(m):
    u, v, w = map(int, input().split())
    EL.append((u-1, v-1, w))
    AM[u - 1][v - 1] = w
    AM[v - 1][u - 1] = w

#print(AM)
ans = 0
for k in range(n):
    for i in range(n):
        for j in range(n):
            if AM[i][k] + AM[k][j] <= AM[i][j] and i != j:
                AM[i][j] = AM[i][k] + AM[k][j]

for u, v, w in EL:
    ans += any(AM[u][i] + AM[i][v] <= w and u != i and v!= i for i in range(n))
print(ans)