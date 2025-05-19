problems = list(map(int, input().split()))
hackers = list(map(int, input().split()))
ans = 0
cur = 0
for i in range(3):
    if hackers[i] > problems[cur]:
        ans += 1
        cur += 1
print(ans)