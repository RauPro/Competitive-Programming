import sys
from functools import lru_cache
input = lambda: sys.stdin.readline().rstrip("\r\n")
flush = lambda: sys.stdout.flush()
print = lambda *args, **kwargs: sys.stdout.write(' '.join(map(str, args)) + kwargs.get("end", "\n")) and flush()
def ints(): return map(int, input().split())
def strs(): return input().split()
def chars(): return list(input().strip())
def mat(n): return [list(ints()) for _ in range(n)]
def main():
    n,m  = ints()
    a, b = list(ints()), list(ints())
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    print(dp[n][m])
    lcs_elements = []
    curr_n = n
    curr_m = m
    while curr_n > 0 and curr_m > 0:
        if a[curr_n - 1] == b[curr_m - 1]:
            lcs_elements.append(a[curr_n - 1])
            curr_n -= 1
            curr_m -= 1
        elif dp[curr_n - 1][curr_m] >= dp[curr_n][curr_m - 1]:
            curr_n -= 1
        else:
            curr_m -= 1
    lcs_elements.reverse()

    print(*(map(str, lcs_elements)))
if __name__ == "__main__":
    main()