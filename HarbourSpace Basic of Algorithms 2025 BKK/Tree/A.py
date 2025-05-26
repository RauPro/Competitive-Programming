import sys, bisect
from collections import Counter
from types import GeneratorType
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
    n = int(input())
    AL = [[] for i in range( n + 1)]
    AL_R = [[] for i in range( n + 1)]
    for i in range(n-1):
        u = int(input())
        AL[u].append( i + 2)
        AL_R[ i + 2].append(u)
    a = list(ints())
    visited = [False] * (n + 1)
    lca = -1
    mapper = {}
    @bootstrap
    def dfs(u, path):
        nonlocal lca
        if u == 1:
            path.append(u)
            #print(path)
            for p in path:
                if p not in mapper:
                    mapper[p] = True
                else:
                    lca = p
                    break
            #print(*path, u)
        for v in AL_R[u]:
            path.append(u)
            yield dfs(v, path)
        yield
    u, v = ints()
    dfs(u, [])
    dfs(v, [])
    prefix_sum = a[:]
    @bootstrap
    def dfs_sum(u, p):
        nonlocal prefix_sum
        if p != -1:
            prefix_sum[u - 1] += prefix_sum[p - 1]
        for v in AL[u]:
            yield dfs_sum(v, u)
        yield
    dfs_sum(1, -1)
    #print(lca, prefix_sum)
    print(prefix_sum[u-1] + prefix_sum[v-1] - 2*prefix_sum[lca-1] + a[lca-1])


if __name__ == "__main__":
    main()
