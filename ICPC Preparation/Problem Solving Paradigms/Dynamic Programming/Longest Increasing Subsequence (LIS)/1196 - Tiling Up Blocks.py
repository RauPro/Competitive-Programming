import sys
import bisect


def tallest_tiling_blocks(blocks):
    blocks.sort(key=lambda x: (x[0], x[1]))
    dp = []
    for block in blocks:
        m = block[1]
        idx = bisect.bisect_right(dp, m)
        if idx == len(dp):
            dp.append(m)
        else:
            dp[idx] = m
    return len(dp)


def main():
    for line in sys.stdin:
        n = int(line.strip())
        if n == 0:
            break
        blocks = []
        for _ in range(n):
            l, m = map(int, sys.stdin.readline().strip().split())
            blocks.append((l, m))
        print(tallest_tiling_blocks(blocks))
    print("*")


if __name__ == "__main__":
    main()

"""
def tallest_stack(blocks):
    # Initialize a 2D DP array with dimensions (101 x 101)
    dp = [[0] * 101 for _ in range(101)]
    
    for l, m in blocks:
        # Find the maximum stack height for all blocks with l' <= l and m' <= m
        max_prev = 0
        for i in range(1, l + 1):
            for j in range(1, m + 1):
                if dp[i][j] > max_prev:
                    max_prev = dp[i][j]
        # Update the DP table for the current block
        dp[l][m] = max_prev + 1
    
    # Find the overall maximum stack height
    return max(max(row) for row in dp)

def process_input():
    results = []
    while True:
        try:
            n = int(input())
            if n == 0:
                break
            blocks = []
            for _ in range(n):
                l, m = map(int, input().split())
                blocks.append((l, m))
            # Sort blocks by l ascending and then m ascending
            blocks.sort()
            result = tallest_stack(blocks)
            results.append(result)
        except EOFError:
            break
    return results

if __name__ == "__main__":
    results = process_input()
    for res in results:
        print(res)
    print('*')
"""

