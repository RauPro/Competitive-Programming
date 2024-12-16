import sys
import threading


def main():
    import math

    Q = int(sys.stdin.readline())
    queries = [tuple(map(int, sys.stdin.readline().split())) for _ in range(Q)]

    # Precompute the triangle sizes (not strictly necessary since we can start with a large size)
    # Maximum size needed based on constraints (max x and y ≤ 1e9)
    max_coordinate = max(max(x for x, y in queries), max(y for x, y in queries))

    # Since the triangle size at each step N is S(N) = 3 * (2^(N-1)) - 1,
    # we can find minimal N such that S(N) ≥ max_coordinate
    # Let's compute S(N) up to N where S(N) ≥ 1e9
    sizes = []
    s = 2
    while s < max_coordinate:
        sizes.append(s)
        s = 2 * s + 1  # Based on the recursive formula
    sizes.append(s)  # Include the final size

    max_size = sizes[-1]

    def is_red(x, y, size):
        while size >= 2:
            if size == 2:
                return True  # All points are red in the smallest triangle
            mid = (size + 1) // 2
            if x == mid:
                # Middle row is blue
                return False
            elif x < mid:
                # Point is in the top triangle
                size = mid - 1
            else:
                # Point is in the bottom triangles
                if y <= mid - 1:
                    # Left bottom triangle
                    x -= mid
                    size = mid - 1
                elif y > mid:
                    # Right bottom triangle
                    x -= mid
                    y -= mid
                    size = mid - 1
                else:
                    # Middle inverted triangle area (blue)
                    return False
        # If we reach here, the point is red
        return True

    for x, y in queries:
        result = 1 if is_red(x, y, max_size) else 0
        print(result)


# To handle large recursion depths in threading
threading.Thread(target=main).start()