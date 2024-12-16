import sys
import threading

def main():
    import sys

    T = int(sys.stdin.readline())
    for _ in range(T):
        N = int(sys.stdin.readline())
        A = list(map(int, sys.stdin.readline().split()))
        n = N
        for k in range(n // 2):
            p = 2 * k
            q = 2 * k + 1
            pair_sum = A[p] + A[q]
            if pair_sum < 0:
                A[p] *= -1
                A[q] *= -1
        # Apply Kadane's algorithm
        max_so_far = A[0]
        current_max = A[0]
        for i in range(1, N):
            current_max = max(A[i], current_max + A[i])
            max_so_far = max(max_so_far, current_max)
        print(max_so_far)

threading.Thread(target=main).start()