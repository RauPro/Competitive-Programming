input = __import__('sys').stdin.readline
class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.parent[rootX] = rootY
            self.size[rootY] += self.size[rootX]

    def component_size(self, x):
        return self.size[self.find(x)]


# dfs to return total population of a component (city)
def dfs(node, adj, a, visited):
    visited[node] = True
    total = a[node]
    for child in adj[node]:
        if not visited[child]:
            total += dfs(child, adj, a, visited)
    return total


def can_connect(n, a, c):
    cities = [(pop, i) for i, pop in enumerate(a)]
    # cities.sort(reverse=True)
    # print(cities)
    dsu = UnionFind(n)
    adj = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            idx1, idx2 = cities[i][1], cities[j][1]
            if dsu.find(idx1) == dsu.find(idx2):
                continue

            visited = [False] * n
            total_population = dfs(idx1, adj, a, visited) + dfs(idx2, adj, a, visited)
            #print("dfs", dfs(idx1, adj, a, visited))
            #print(total_population, idx1 + 1, idx2 + 1)
            if total_population >= (idx1 + 1) * (idx2 + 1) * c:
                #print("Connecting", idx1 + 1, idx2 + 1)
                #a[idx1] += a[idx2]
                dsu.union(idx1, idx2)
                adj[idx1].append(idx2)
                adj[idx2].append(idx1)
    return dsu.component_size(0) == n


# Testing
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, c = map(int, input().split())
        nums = list(map(int, input().split()))
        print("YES" if can_connect(n, nums, c) else "NO")