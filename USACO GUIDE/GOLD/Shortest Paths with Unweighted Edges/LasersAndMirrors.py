import sys
import math
import random
from collections import defaultdict


def main():
    input = sys.stdin.read
    data = input().split()

    index = 0
    T = int(data[index])
    index += 1
    results = []

    for case_num in range(1, T + 1):
        N = int(data[index])
        index += 1
        points = []

        for _ in range(N):
            x, y = int(data[index]), int(data[index + 1])
            points.append((x, y))
            index += 2

        if N <= 2:
            answer = 0
        else:
            line_counts = defaultdict(int)
            K = min(5000, N * (N - 1) // 2)  # Number of random pairs

            # Precompute random pairs
            pairs = set()
            while len(pairs) < K:
                i, j = random.sample(range(N), 2)
                pairs.add((i, j))

            for i, j in pairs:
                x1, y1 = points[i]
                x2, y2 = points[j]

                A = y2 - y1
                B = x1 - x2
                C = x2 * y1 - x1 * y2

                # Normalize the coefficients
                gcd = math.gcd(A, math.gcd(B, C))
                if gcd != 0:
                    A //= gcd
                    B //= gcd
                    C //= gcd

                # Ensure the first non-zero coefficient is positive
                if A < 0 or (A == 0 and B < 0):
                    A *= -1
                    B *= -1
                    C *= -1

                line_key = (A, B, C)
                line_counts[line_key] += 1

            # Get the top L lines
            L = 10
            top_lines = sorted(line_counts.items(), key=lambda x: -x[1])[:L]

            max_count = 0
            for line, _ in top_lines:
                A, B, C = line
                count = sum(1 for x, y in points if A * x + B * y + C == 0)
                max_count = max(max_count, count)

            answer = N - max_count

        results.append(f"Case #{case_num}: {answer}")

    sys.stdout.write("\n".join(results) + "\n")


if __name__ == "__main__":
    main()
