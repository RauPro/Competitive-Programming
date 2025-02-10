n, x = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
local_ans = 0
for i in range(n-1):
    if a[i+1] - a[i] <= x:
        local_ans += 1
    else:
        ans = max(ans, local_ans)
        local_ans = 0
print(max(ans, local_ans) + 1)