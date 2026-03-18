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

    status = [0] * (n + 1)
    parent = [-1] * (n + 1)
    cycle_start = -1
    cycle_end = -1
    @bootstrap
    def dfs(node):
        nonlocal cycle_start, cycle_end
        status[node] = 1

        for neighbor in AL[node]:
            if cycle_start != -1:
                break

            if status[neighbor] == 0:
                parent[neighbor] = node
                yield dfs(neighbor)
            elif status[neighbor] == 1:
                cycle_start = neighbor
                cycle_end = node

        status[node] = 2
        yield
    for i in range(1, n + 1):
        if status[i] == 0 and cycle_start == -1:
            dfs(i)

    if cycle_start != -1:
        cycle = []
        current = cycle_end
        while current != cycle_start:
            cycle.append(current)
            current = parent[current]
        cycle.append(cycle_start)
        print(" ".join(map(str, reversed(cycle))))
    else:
        print("-1")

if __name__ == "__main__":
    main()