from math import gcd
n = int(input())
a = list(map(int, input().split()))

a.sort()

def max_ans(i):
    max_ = a[i]
    ans = 0
    for j in range(n - 1):
        if i == j: continue;
        ans += gcd(max_, a[j])
    return ans

ans_ = 0
for i in range(n):
    ans_ = max(ans_, max_ans(i))
print(ans_)