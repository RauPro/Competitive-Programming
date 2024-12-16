def dfs(u, AL, can):
    stack = [u]
    while stack:
        u = stack.pop()
        for v in AL[u]:
            if can[v] is None:
                can[v] = True
                stack.append(v)

n = int(input())
AL = [[] for i in range(n + 1)]
labels = [0] * (n+1)
for i in range(n):
    l, m, *u = map(int, input().split())
    labels[i + 1] = l
    for u_ in u:
        AL[u_].append(i+1)

can = [None] * (n+1)

for u in range(1, n+1):
    if labels[u]:
        dfs(u, AL, can)

print(sum([1 for i, it in enumerate(can) if it and labels[i]]))
