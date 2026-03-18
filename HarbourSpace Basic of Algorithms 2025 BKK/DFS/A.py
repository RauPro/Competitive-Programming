import sys
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
    n, m = ints()
    AL = [[] for _ in range(n + 1)]
    for i in range(m):
        u, v = ints()
        AL[u].append(v)
    visited = [False] * (n + 1)

    @bootstrap
    def dfs(u, p):
        nonlocal visited
        visited[u] = True
        for v in AL[u]:
            if visited[v]:
                print('NO'); exit()
            if v != p:
                yield dfs(v, u)
        yield
    dfs(1, -1)
    visited[0] = True
    print('YES' if all(visited) else 'NO')

if __name__ == "__main__":
    main()