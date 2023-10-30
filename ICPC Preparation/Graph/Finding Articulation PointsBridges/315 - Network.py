import sys
from enum import Enum
class flag(Enum):
  UNVISITED = -1

AL = []
dfs_num = []
dfs_low = []
dfs_parent = []
articulation_vertex = []
dfsNumberCounter = 0
dfsRoot = 0
rootChildren = 0

def articulationPointAndBridge(u):
  global AL
  global dfs_num, dfs_parent, dfs_low, articulation_vertex
  global dfsNumberCounter, dfsRoot, rootChildren

  dfs_low[u] = dfs_num[u] = dfsNumberCounter
  dfsNumberCounter += 1
  for v in AL[u]:
    if dfs_num[v] == flag.UNVISITED.value:
      dfs_parent[v] = u
      if u == dfsRoot:
        rootChildren += 1

      articulationPointAndBridge(v)

      if dfs_low[v] >= dfs_num[u]:
        articulation_vertex[u] = True
      #if dfs_low[v] > dfs_num[u]:
        #print(' Edge (%d, %d) is a bridge' % (u, v))
      dfs_low[u] = min(dfs_low[u], dfs_low[v])
    elif v != dfs_parent[u]:
      dfs_low[u] = min(dfs_low[u], dfs_num[v])


def main():
  global AL
  global dfs_num, dfs_parent, dfs_low, articulation_vertex
  global dfsNumberCounter, dfsRoot, rootChildren
  while True:
    V = int(input())
    if V == 0: break
    AL = [[] for _ in range(V)]
    while True:
      tkn = list(map(int, input().split()))
      if len(tkn) == 1 and tkn[0] == 0: break
      k = tkn[0]-1
      for i in range(1, len(tkn)):
        v = tkn[i] - 1
        AL[k].append(v)
        AL[v].append(k)
    #print(AL)
    #print('Articulation Points & Bridges (the input graph must be UNDIRECTED)')
    dfs_num = [flag.UNVISITED.value] * V
    dfs_low = [0] * V
    dfs_parent = [-1] * V
    articulation_vertex = [False] * V
    dfsNumberCounter = 0
    #print('Bridges:')
    for u in range(V):
      if dfs_num[u] == flag.UNVISITED.value:
        dfsRoot = u
        rootChildren = 0
        articulationPointAndBridge(u)
        articulation_vertex[dfsRoot] = (rootChildren > 1)

    #print('Articulation Points:', )
    #for u in range(V):
      #if articulation_vertex[u]:
        #print(' Vertex %d' % u)
    print(articulation_vertex.count(True))
main()