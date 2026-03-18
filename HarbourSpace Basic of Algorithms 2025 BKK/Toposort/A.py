import sys
from types import GeneratorType
from collections import deque
input = lambda: sys.stdin.readline().rstrip("\r\n")
flush = lambda: sys.stdout.flush()
print = lambda *args, **kwargs: sys.stdout.write(' '.join(map(str, args)) + kwargs.get("end", "\n")) and flush()
def ints(): return map(int, input().split())
def strs(): return input().split()
def chars(): return list(input().strip())
def mat(n): return [list(ints()) for _ in range(n)]

def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        to = f(*args, **kwargs)
        while True:
            if type(to) is GeneratorType:
                stack.append(to)
                to = next(to)
            else:
                stack.pop()
                if not stack:
                    break
                to = stack[-1].send(to)
        return to

    return wrappedfunc

def main():
    n, m = ints()
    AL = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    for i in range(m):
        u, v = ints()
        AL[v].append(u)
        indegree[u] += 1
    #visited = [False] * (n + 1)
    """toposort = []
    state = [0] * (n + 1)
    cycle = False
    @bootstrap
    def dfs(u):
        nonlocal state, cycle
        if cycle: yield
        for v in AL[u]:
            if state[v] == 0:
                yield dfs(v)
                if cycle: yield
            elif state[v] == 1:
                cycle = True
                yield
        state[u] = 2
        toposort.append(u)
        yield
    for u in range(1, n + 1):
        if state[u] == 0:
            dfs(u)
            if cycle:
                print(-1)
                return
    print(*toposort[::-1])"""
    q = deque([u for u in range(1, n+1) if indegree[u] == 0])
    topo = []
    while q:
        x = q.popleft(); topo.append(x)
        for w in AL[x]:
            indegree[w] -= 1
            if indegree[w] == 0: q.append(w)
    if len(topo) < n: print(-1)
    else: print(*topo)
if __name__ == "__main__":
    main()