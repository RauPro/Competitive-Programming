n, m = map(int, input().split())
debt = [0] * (n+1)
cash_flow = 0
for i in range(m):
    u, v, w = map(int, input().split())
    debt[u] -= w
    debt[v] += w
    cash_flow += w
min_debt = min(debt)
cash_flow += (abs(min_debt))
print(n)
for i in range(1, n):
    cash_flow += debt[i]
    print(i, i+1, cash_flow)
print(n, 1, cash_flow + debt[n])

#print(min_debt, debt, cash_flow)

