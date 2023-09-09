from collections import defaultdict
from collections import deque
import sys
input = sys.stdin.readline

def bfs(r, c, m, n, l, visited, mapper):
    dr = [m, -m, m, -m, n, n, -n, -n]
    dc = [n, n, -n, -n, m, -m, m, -m]
    q = deque()
    q.append((0, 0))
    visited[0][0] = True
    even, odds = 0, 0
    while len(q) > 0:
        x, y = q.popleft()
        adj = set()
        for _ in range(len(dr)):
            i = dr[_] + x
            j = dc[_] + y
            if 0 <= i < r and 0 <= j < c and not mapper[i][j]:
                adj.add((i, j))
        for a, b in adj:
            l[a][b] += 1
            if not visited[a][b]:
                visited[a][b] = True
                q.append((a, b))

    for i in range(r):
        for j in range(c):
            if (not mapper[i][j] and l[i][j] != 0) or (i == 0 and j == 0):
                if l[i][j] % 2 == 0:
                    even += 1
                else:
                    odds += 1
    return even, odds


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        r, c, m, n = map(int, input().split())
        visited = [[False for _a in range(c)] for _q in range(r)]
        mapper = [[False for _r in range(c)] for _d in range(r)]
        val = 0
        l = [[0 for q in range(c)] for z in range(r)]
        w = int(input())
        for _w in range(w):
            xi, yi = map(int, input().split())
            mapper[xi][yi] = True
        even, odds = bfs(r, c, m, n, l, visited, mapper)
        #print(l)
        print("Case " + str(_ + 1) + ":", even, odds)
