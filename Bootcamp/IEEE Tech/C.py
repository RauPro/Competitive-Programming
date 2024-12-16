from collections import defaultdict
n = int(input())
AL = defaultdict(list)
nodes = set()
for i in range(n):
    c = list(map(str, input().split()))
    if c[1] == "->":
        AL[c[0]].append(c[2])
    else:
        AL[c[0]].append(c[2])
        AL[c[2]].append(c[0])
    nodes.add(c[0])
    nodes.add(c[2])

memo = {}
visited = {node: 0 for node in nodes}
def dfs(node):
    if visited[node] == 2:
        return memo[node]
    if visited[node] == 1:
        return 0
    visited[node] = 1
    total_reachable = 1
    for neighbor in AL[node]:
        total_reachable += dfs(neighbor)
    visited[node] = 2
    memo[node] = total_reachable
    return total_reachable

for node in list(AL):
    if visited[node] == 0:
        dfs(node)
ans = [it for it in memo.keys() if memo[it]>= n]
print("\n".join(sorted(ans)), memo)