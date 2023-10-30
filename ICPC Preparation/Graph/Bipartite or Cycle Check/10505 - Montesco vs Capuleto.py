from collections import deque

def has(lst, e):
    return e in lst

def main():
    tc = int(input())
    while tc > 0:
        aux = input()
        V = int(input())
        AdjList = [[] for _ in range(V)]

        for u in range(V):
            neighbors = list(map(int, input().split()))
            E = neighbors[0]
            for j in range(1, E+1):
                v = neighbors[j] - 1
                if v < V:
                    if not has(AdjList[u], v):
                        AdjList[u].append(v)
                    if not has(AdjList[v], u):
                        AdjList[v].append(u)

        color = [10**9] * V
        isBipartite = True
        ans = 0

        for s in range(V):
            if color[s] != 10**9:
                continue

            isBipartite = True
            colorCount = [0, 0]
            q = deque()
            q.append(s)
            color[s] = 0
            colorCount[0] += 1

            while q:
                u = q.popleft()
                for v in AdjList[u]:
                    if color[v] == 10**9:
                        color[v] = 1 - color[u]
                        colorCount[color[v]] += 1
                        q.append(v)
                    elif color[v] == color[u]:
                        isBipartite = False

            if isBipartite:
                ans += max(colorCount[0], colorCount[1])

        print(ans)
        tc -= 1

if __name__ == "__main__":
    main()
