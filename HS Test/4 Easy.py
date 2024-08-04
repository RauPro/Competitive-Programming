from bisect import bisect_right

n, m = map(int, input().split())
c = list(map(int, input().split()))
a = list(map(int, input().split()))
c.sort()
ans = []
for it in a:
    index = bisect_right(c, it)
    ans.append(index)
print(*ans)