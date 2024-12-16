n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
if n != 2 * m:
    a = ([0] * (2 * m - len(a))) + a
ans = a[0]
#print(a)
for i in range(m):
#    print(i, 2 * m - i-1)
    ans = max(ans, a[i] + a[2 * m - i-1])
print(ans)