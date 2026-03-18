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
    n, target = ints()
    coins = sorted(list(ints()))
    INF = float('inf')
    dp = [INF] * (target + 1)
    choice = [-1] * (target + 1)
    dp[0] = 0
    for amt in range(1, target + 1):
        for coin in coins:
            if coin > amt: break
            if dp[amt - coin] != INF and dp[amt - coin] + 1 < dp[amt]:
                dp[amt] = dp[amt - coin] + 1
                choice[amt] = coin
    if dp[target] == INF: print("-1")
    else:
        print(dp[target])
        used, remaining = [], target
        while remaining > 0:
            coin = choice[remaining]
            used.append(coin)
            remaining -= coin
        print(' '.join(map(str, used)))
if __name__ == "__main__":
    main()