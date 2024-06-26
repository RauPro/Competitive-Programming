from collections import deque, defaultdict


def bfs(tree, start, n):
    distances = [-1] * (n + 1)
    queue = deque([start])
    distances[start] = 0

    while queue:
        node = queue.popleft()
        current_distance = distances[node]

        for neighbor in tree[node]:
            if distances[neighbor] == -1:
                distances[neighbor] = current_distance + 1
                queue.append(neighbor)

    return distances


def solve():
    import sys
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        tree = defaultdict(list)
        a, b = map(int, input().split())
        for __ in range(n - 1):
            x, y = map(int, input().split())
            tree[x].append(y)
            tree[y].append(x)

        distances_from_a = bfs(tree, a, n)
        distances_from_b = bfs(tree, b, n)

        max_steps = 0
        for i in range(1, n + 1):
            if distances_from_a[i] <= distances_from_b[i]:
                max_steps = max(max_steps, distances_from_b[i])

        results.append(max_steps)

    for result in results:
        print(result)

solve()