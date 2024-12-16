# BISMILLAHIRRAHMANIRRAHIM
"""
manus tar shopner soman boro
Author :: Shakil Ahmed
.............AUST_CSE27.........
prob   ::
Type   ::
verdict::
"""

import sys
from math import inf

# Constants
dx = [1, 0]
dy = [0, 1]

# Helper functions
def valid(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

# Recursive DP function
def DP(r1, c1, r2, c2, n, m, inp, dp):
    if r1 >= n or r2 >= n or c1 >= m or c2 >= m:
        return 0
    if r1 == r2 and c1 == c2:
        return 0
    if dp[r1][c1][r2] != -1:
        return dp[r1][c1][r2]

    ret = 0
    ret = max(ret, DP(r1 + 1, c1, r2 + 1, c2, n, m, inp, dp))
    ret = max(ret, DP(r1 + 1, c1, r2, c2 + 1, n, m, inp, dp))
    ret = max(ret, DP(r1, c1 + 1, r2 + 1, c2, n, m, inp, dp))
    ret = max(ret, DP(r1, c1 + 1, r2, c2 + 1, n, m, inp, dp))

    dp[r1][c1][r2] = ret + inp[r1][c1] + inp[r2][c2]
    return dp[r1][c1][r2]


def DP_iterative(n, m, inp):
    # Initialize the 4D DP table with 0
    # Dimensions: r1, c1, r2, c2
    dp = [[[[0 for _ in range(m)] for __ in range(n)] for ___ in range(m)] for ____ in range(n)]

    # Iterate through all possible positions of r1 and c1
    for r1 in range(n):
        for c1 in range(m):
            for r2 in range(n):
                for c2 in range(m):
                    # Check for out-of-bounds indices
                    if r1 >= n or r2 >= n or c1 >= m or c2 >= m:
                        dp[r1][c1][r2][c2] = 0
                        continue
                    # If both pointers are on the same cell, avoid double-counting
                    if r1 == r2 and c1 == c2:
                        current_value = inp[r1][c1]
                    else:
                        current_value = inp[r1][c1] + inp[r2][c2]
                    # Initialize the maximum value for this state
                    ret = 0
                    # Explore all four possible previous states
                    # 1. Both pointers moved from above
                    if r1 > 0 and r2 > 0:
                        ret = max(ret, dp[r1 - 1][c1][r2 - 1][c2])
                    # 2. First pointer moved from above, second from the left
                    if r1 > 0 and c2  > 0:
                        ret = max(ret, dp[r1 - 1][c1][r2][c2 - 1])
                    # 3. First pointer moved from the left, second from above
                    if c1 > 0 and r2 > 0:
                        ret = max(ret, dp[r1][c1 - 1][r2 - 1][c2])
                    # 4. Both pointers moved from the left
                    if c1 > 0 and c2 > 0:
                        ret = max(ret, dp[r1][c1 - 1][r2][c2 - 1])
                    # Update the DP table with the current value and the best previous state
                    dp[r1][c1][r2][c2] = ret + current_value

    # The answer is in the state where both pointers are at the last cell
    return dp[n - 1][m - 1][n - 1][m - 1]


# Main function
def main():
    t = int(input())  # Number of test cases
    for cs in range(1, t + 1):
        input()
        n, m = map(int, input().split())  # Dimensions of the grid
        inp = []
        for _ in range(n):
            inp.append(list(map(int, input().split())))

        # Initialize DP table
        dp = [[[-1 for _ in range(n)] for _ in range(m)] for _ in range(n)]

        # Solve the problem
        #result = DP(0, 1, 1, 0, n, m, inp, dp) + inp[0][0] + inp[n - 1][m - 1]
        result = DP_iterative(n, m, inp)
        print(f"Case {cs}: {result}")

if __name__ == "__main__":
    main()