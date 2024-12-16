from functools import lru_cache
N, K = map(int, input().split())
length = N * K
a = list(map(int, input().split()))
b = list(map(int, input().split()))
@lru_cache(maxsize=None)
def dp(i, j):
    if i >= length or j >= length:
        return 0
    if (a[i] == b[j]):
        return 1 + dp(i + 1, j + 1)
    return max(dp(i + 1, j), dp(i, j + 1))
print(dp(0, 0))