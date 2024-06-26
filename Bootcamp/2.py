def bacteria_count(n):
    MOD = 10**9 + 7
    dp = [0] * 21
    dp[0] = 1
    for i in range(1, n+1):
        dp[i%21] = dp[(i-1)%21]
        if i >= 2:
            dp[i%21] += dp[(i-2)%21]
        if i >= 4:
            dp[i%21] += 2 * dp[(i-4)%21]
        if i >= 20:
            dp[i%21] -= dp[(i-20)%21]
        dp[i%21] %= MOD
    return dp[n%21]

T = int(input())
for _ in range(T):
    N = int(input())
    print(bacteria_count(N))
