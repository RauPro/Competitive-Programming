import heapq
from collections import deque
def get_id(i, j, m):
    return i * m + j

def get_coords(id, m):
    return divmod(id, m)

n, m = map(int, input().split())
grid = [input() for _ in range(n)]
MAX_N = n * m
AL = [[] for _ in range(MAX_N)]
s = t = -1

for i in range(n):
    for j in range(m):
        current_id = get_id(i, j, m)
        cell = grid[i][j]
        if cell == "S":
            s = current_id
        if cell == "T":
            t = current_id
        if cell != "#":
            for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] != "#":
                    neighbor_id = get_id(ni, nj, m)
                    AL[current_id].append(neighbor_id)

INF = int(1e9)
dist = [INF] * MAX_N
steps = [INF] * MAX_N
dist[s] = 0
steps[s] = 0

pq = deque()
pq.append((0, s, 0, -1, -1))

while pq:
    w, u, step_, dir, p = pq.popleft()
    if w > dist[u]:
        continue
    for v in AL[u]:
        if p == v: continue
        u_i, u_j = get_coords(u, m)
        v_i, v_j = get_coords(v, m)
        dif_row = u_i - v_i
        dif_col = u_j - v_j

        if dir == 1 and dif_col == -1 and dif_row == 0:
            new_step = step_ + 1
            cur = dir
        elif dir == 2 and dif_col == 1 and dif_row == 0:
            new_step = step_ + 1
            cur = dir
        elif dir == 3 and dif_col == 0 and dif_row == 1:
            new_step = step_ + 1
            cur = dir
        elif dir == 4 and dif_col == 0 and dif_row == -1:
            new_step = step_ + 1
            cur = dir
        else:
            new_step = 1
            if dif_col == 0 and dif_row == 1:
                cur = 3
            elif dif_col == 0 and dif_row == -1:
                cur = 4
            elif dif_col == 1 and dif_row == 0:
                cur = 2
            elif dif_col == -1 and dif_row == 0:
                cur = 1

        if new_step > 3:
            new_distance = dist[u] + 3
            new_step = 2
        else:
            new_distance = dist[u] + 1

        if new_distance > dist[v]:
            continue
        if new_distance == dist[v] and steps[v] < new_step:
            continue

        dist[v] = new_distance
        steps[v] = new_step
        pq.append((new_distance, v, new_step, cur, u))

print(dist[t] if dist[t] != INF else -1)