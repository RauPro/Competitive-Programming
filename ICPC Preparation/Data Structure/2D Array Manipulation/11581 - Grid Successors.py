def transform(g):
    """
    Transforms the grid g according to the rules given.
    """
    transformed = [[0]*3 for _ in range(3)]
    for r in range(3):
        for c in range(3):
            # Sum of adjacent cells modulo 2
            sum_adjacent = 0
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                rr, cc = r + dr, c + dc
                if 0 <= rr < 3 and 0 <= cc < 3:
                    sum_adjacent += g[rr][cc]
            transformed[r][c] = sum_adjacent % 2
    return transformed

def find_greatest_finite_index(g):
    """
    Computes the greatest index i for which the number of indices kg(f^i(g)) is finite.
    """
    seen = {}
    i = 0

    # Convert grid to tuple for easy hashing and comparison.
    current = tuple(tuple(row) for row in g)

    # Keep track of each unique grid configuration we've seen and at which step it was seen.
    seen[current] = i

    while True:
        # Perform the transformation.
        current = tuple(tuple(row) for row in transform([[cell for cell in row] for row in current]))
        i += 1

        if current in seen:
            # We've seen this configuration before, so we have a cycle.
            return seen[current] - 1  # The last index before the cycle starts.

        seen[current] = i


t = int(input())

for _ in range(t):

    g = []
    _ = input()
    for _ in range(3):
        g.append([int(x) for x in input()])

    # Find the greatest finite index for grid g.
    print(find_greatest_finite_index(g))
