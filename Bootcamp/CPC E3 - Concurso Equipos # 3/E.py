


class UFDS:
    def __init__(self, n):
        self.p = list(range(n))
        self.ranks = [0] * n
        self.size = [1] * n
        self.numSet = n

    def findSet(self, i):
        return i if self.p[i] == i else self.findSet(self.p[i])
    def isSameSet(self, i, j):
        return self.findSet(i) == self.findSet(j)

    def numDisjointSets(self):
        return self.numSet

    def sizeOfSet(self, i):
        return self.size[self.findSet(i)]

    def unionSet(self, i, j):
        if self.isSameSet(i, j): return
        x = self.findSet(i)
        y = self.findSet(j)
        if self.ranks[x] > self.ranks[y]:
            aux = x
            x = y
            y = aux
        self.p[x] = y
        if self.ranks[x] == self.ranks[y]: self.ranks[y]+=1
        self.size[y] += self.size[x]
        self.numSet-=1




V, E = map(int, input().split())

ids = list(map(int, input().split()))
mapper = {}
id = {}
for i, it in enumerate(ids):
    mapper[it] = i+1
    id[i+1] = it

AL = [[] for i in range(V+1)]

UF = UFDS(int(1e7))

for i in range(E):
    u,v = map(int, input().split())
    AL[u].append(v)
    AL[v].append(u)

ans = 1
for u in range(1, V+1):
    sameSet = False
    if u not in mapper:
        break
    for v in AL[mapper[u]]:
        if id[v] < u:
            sameSet = UF.isSameSet(v, mapper[u])
            UF.unionSet(v, (mapper[u]))
    if sameSet == 1:
        ans = u


print(ans)