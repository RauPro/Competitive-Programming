import sys
import random

input = sys.stdin.readline
rd = random.randint(10 ** 9, 2 * 10 ** 9)
t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    g = [[] for _ in range(n)]
    for i in range(n - 1):
        g[p[i] - 1].append(i + 1)
    # 找树中最长链
    from collections import deque
    q = deque([(0, 0)])
    d = [0] * n
    while q:
        x, dd = q.popleft()
        d[dd] += 1
        for y in g[x]:
            q.append((y, dd + 1))
    ans = 0
    rem = 0
    print(d)
    for i in range(n - 1,-1,-1):
        x = max(0,min(rem, d[i] - 1))
        d[i] -= x
        rem -= x
        ans += d[i] // 2 + x
        rem += d[i] % 2
    print(ans)