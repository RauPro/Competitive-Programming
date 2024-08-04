from heapq import heappop, heappush
from collections import defaultdict, deque

def process(u, taken, AL, pq):
    taken[u] = True
    for v, w in AL[u]:
        if not taken[v]:
            heappush(pq, (w, v, u))

def bfs(u, AL):
    visited = [False] * (len(AL) + 1)
    dist = [0] * (len(AL) + 1)
    queue = deque([u])
    visited[u] = True
    farthest_node = u

    while queue:
        node = queue.popleft()
        for v, w in AL[node]:
            if not visited[v]:
                visited[v] = True
                dist[v] = dist[node] + 1
                queue.append(v)
                if dist[v] > dist[farthest_node]:
                    farthest_node = v

    return farthest_node, dist[farthest_node]

def find_tree_diameter(AL):
    # First BFS to find one endpoint of the diameter
    farthest_node, _ = bfs(1, AL)
    # Second BFS from the farthest node found
    _, diameter = bfs(farthest_node, AL)
    return diameter

V, E = map(int, input().split())
AL = defaultdict(list)
for _ in range(E):
    u, v, w = map(int, input().split())
    AL[u].append((v, w))
    AL[v].append((u, w))

taken = [False] * (V + 1)
pq = []
process(1, taken, AL, pq)
mst_cost = 0
num_taken = 0
AL_ = defaultdict(list)

while pq and num_taken < V - 1:
    w, u, v = heappop(pq)
    if not taken[u]:
        mst_cost += w
        AL_[u].append((v, w))
        AL_[v].append((u, w))
        process(u, taken, AL, pq)
        num_taken += 1

diameter = find_tree_diameter(AL_)
print(mst_cost)
print(diameter)
