from itertools import accumulate
from bisect import bisect_left
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    prefix = [0] * (n)
    prefix[0] = 1
    for i in range(1, n):
        if a[i] != a[i-1]:
            prefix[i] = prefix[i-1] + 1
        else:
            prefix[i] = prefix[i - 1]
    prefix = [0] + prefix
    a = [ 0] + sorted(list(set(a)))
    prefix = sorted(list(set(prefix)))
    print(f"Case {_ + 1}:")
    for q in range(k):
        x, y = map(int, input().split())
        index_a = bisect_left(a, x)
        index_b = bisect_left(a, y)

        if index_b == n+1:
            index_b -= 1
        if a[index_b] > y:
            index_b -= 1

        print(prefix[index_b] - prefix[index_a - (1 if x != 0 else 0)])

