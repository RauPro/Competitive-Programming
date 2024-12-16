from math import log
n = int(input())
ans = 1
n_ = n
while n_ > 1:
    n_ //= 3
    ans += 1

ans -=1
print(ans if 1 == n_ else -1)