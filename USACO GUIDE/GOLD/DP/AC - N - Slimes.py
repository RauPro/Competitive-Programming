def min_total_cost(N, a):
    # Initialize prefix sums
    prefix_sum = [0] * (N + 1)
    for i in range(N):
        prefix_sum[i + 1] = prefix_sum[i] + a[i]

    # Initialize DP table
    dp = [[0] * (N + 1) for _ in range(N + 1)]

    # Fill DP table
    for length in range(2, N + 1):  # length of the sequence
        for i in range(1, N - length + 2):  # starting index
            j = i + length - 1  # ending index
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + prefix_sum[j] - prefix_sum[i - 1]
                if cost < dp[i][j]:
                    dp[i][j] = cost
            print(i, j, cost)
    return dp[1][N]


# Example usage:
if __name__ == "__main__":
    import sys
    N = int(input())
    a = list(map(int, input().split()))
    print(min_total_cost(N, a))