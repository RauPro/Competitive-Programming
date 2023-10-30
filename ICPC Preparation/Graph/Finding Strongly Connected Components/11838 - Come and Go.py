dfsNumberCounter = 0
numSCC = 0
AL = []
AL_T = []
dfs_num = []
dfs_low = []
S = []
visited = []
st = []
UNVISITED = -1


def tarjanSCC(u):
  global dfs_low, dfs_num, dfsNumberCounter, visited
  global AL, numSCC, st

  dfs_low[u] = dfs_num[u] = dfsNumberCounter
  dfsNumberCounter += 1
  st.append(u)
  visited[u] = True
  for v in AL[u]:
    if dfs_num[v] == UNVISITED:
      tarjanSCC(v)
    if visited[v]:
      dfs_low[u] = min(dfs_low[u], dfs_low[v])

  if dfs_low[u] == dfs_num[u]:
    numSCC += 1
    while True:
      v = st[-1]
      st.pop()
      visited[v] = False
      if u == v:
        break

if "__main__" == __name__:
    while True:
        n, m = map(int, input().split())
        if n == m == 0:
            break
        AL = [[] for _ in range(n)]
        for _ in range(m):
            v, w, p = map(int, input().split())
            v -= 1
            w -= 1
            AL[v].append(w)
            if p == 2:
                AL[w].append(v)

        dfs_num = [UNVISITED] * n
        dfs_low = [0] * n
        visited = [False] * n
        st = []
        dfsNumberCounter = 0
        numSCC = 0
        for u in range(n):
            if dfs_num[u] == UNVISITED:
                tarjanSCC(u)
        print(1 if numSCC == 1 else 0)