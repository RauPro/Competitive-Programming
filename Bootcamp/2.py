from collections import defaultdict, deque


def build_graph(N, M, movies):
    graph = defaultdict(list)
    for i, actors in enumerate(movies, 1):
        for actor in actors:
            graph[actor].append(i)
    return graph


def bfs(graph, root, M):
    parent = [-1] * (M + 1)
    level = [-1] * (M + 1)
    queue = deque([(root, 0)])
    parent[root] = root
    level[root] = 0

    while queue:
        node, depth = queue.popleft()
        for movie in graph[node]:
            for neighbor in movies[movie - 1]:
                if level[neighbor] == -1:
                    parent[neighbor] = node
                    level[neighbor] = depth + 1
                    queue.append((neighbor, depth + 1))

    return parent, level


def find_path(x, y, parent, level):
    path = []
    while level[x] > level[y]:
        path.append(x)
        x = parent[x]
    while level[y] > level[x]:
        path.append(y)
        y = parent[y]
    while x != y:
        path.append(x)
        path.append(y)
        x = parent[x]
        y = parent[y]
    path.append(x)
    return path


def solve_query(x, y, parent, level, graph):
    path = find_path(x, y, parent, level)
    if len(path) == 1:
        return [path[0]]

    result = []
    for i in range(len(path) - 1):
        result.append(path[i])
        common_movies = set(graph[path[i]]) & set(graph[path[i + 1]])
        result.append(next(iter(common_movies)))
    result.append(path[-1])
    return result


# Read input
N, M = map(int, input().split())
movies = [list(map(int, input().split()))[1:] for _ in range(N)]
graph = build_graph(N, M, movies)

# Build the tree
root = next(iter(graph))
parent, level = bfs(graph, root, M)

# Process queries
Q = int(input())
for _ in range(Q):
    x, y = map(int, input().split())
    path = solve_query(x, y, parent, level, graph)

    if len(path) == 1 and path[0] != x:
        print(-1)
    else:
        print(len(path))
        print(*reversed(path))
