n, m = map(int, input().split())
free_in_row = [0] * n
free_in_col = [0] * m
mx_row = [[] for i in range(2000 + 10)]
mx_col = [[] for i in range(2000 + 10)]
for i in range(n):
    s = input()
    free_in_row[i] += s.count('.')
    for j, it in enumerate(s):
        free_in_col[j] += it == '.'
        if it == '.':
            mx_row[i].append(j)
            mx_col[j].append(i)

ans = 0
#000 F > 3
ans += sum(free_in_row[i] * (free_in_row[i] - 1) * (free_in_row[i]-2) * (free_in_row[i] - 3)
           for i in range(n) if free_in_row[i] > 3)
#print(ans)
#001 F > 2 C > 1
for i in range(n):
    if free_in_row[i] > 2:
        total = 0
        for j in mx_row[i]:
            if free_in_col[j] > 1:
                total += free_in_col[j] - 1
        ans += total * (free_in_row[i] - 1) * (free_in_row[i] - 2)
#print(ans)
#010 F > 1 C > 1 diff F
for i in range(m):
    total = 0
    for j in mx_col[i]:
        if free_in_row[j] > 1:
            total += free_in_row[j] - 1
    for j in mx_col[i]:
        if free_in_row[j] > 1:
            ans += (free_in_row[j] - 1) * (total - (free_in_row[j] - 1))
#print(ans)
#011
for i in range(n):
    if free_in_row[i] > 1:
        for j in mx_row[i]:
            if free_in_col[j] > 2:
                ans += (free_in_row[i] - 1) * (free_in_col[j] - 1) * (free_in_col[j] - 2)
#print(ans)
#100
for i in range(n):
    if free_in_row[i] > 2:
        for j in mx_row[i]:
            if free_in_col[j] > 1:
                ans += (free_in_col[j] - 1) * (free_in_row[i] - 1) * (free_in_row[i] - 2)
#print(ans)
#101 C > 1 F > 1 diff C
for i in range(n):
    total = 0
    for j in mx_row[i]:
        if free_in_col[j] > 1:
            total += free_in_col[j] - 1
    for j in mx_row[i]:
        if free_in_col[j] > 1:
            ans += (free_in_col[j] - 1) * (total - (free_in_col[j] - 1))
#print(ans)

#110 C > 2 > 1
for i in range(m):
    if free_in_col[i] > 2:
        total = 0
        for j in mx_col[i]:
            if free_in_row[j] > 1:
                total += free_in_row[j] - 1
        ans += total * (free_in_col[i] - 1) * (free_in_col[i] - 2)
#print(ans)
#111 F > 3
ans += sum(free_in_col[j] * (free_in_col[j] - 1) * (free_in_col[j] - 2) * (free_in_col[j] - 3)
    for j in range(m) if free_in_col[j] > 3)
#print(free_in_col, free_in_row, ans)
print(ans)