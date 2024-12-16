t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = []
    for i in range(n):
        a.append(int(input()))


    def can(mid, a, k):
        total_cow = 1
        prev = 0
        index = 1
        while index < len(a):
            if a[index] - a[prev] >= mid:
                total_cow += 1
                prev = index
            index += 1
        return total_cow >= k


    lo, hi = 0, max(a) + 1
    a.sort()
    ans = -1
    while lo < hi:
        mid = (lo + hi) // 2
        if can(mid, a, k):
            lo = mid + 1
            ans = mid
        else:
            hi = mid
    print(ans)