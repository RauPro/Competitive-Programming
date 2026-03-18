import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")
flush = lambda: sys.stdout.flush()
print = lambda *args, **kwargs: sys.stdout.write(' '.join(map(str, args)) + kwargs.get("end", "\n")) and flush()
def ints(): return map(int, input().split())
def strs(): return input().split()
def chars(): return list(input().strip())
def mat(n): return [list(ints()) for _ in range(n)]

def main():
    n = int(input())
    AL = [[] for _ in range(n + 1)]
    op = [None] * (n + 1)
    a = [0] * (n + 1)
    for i in range(1, n + 1):
        _ = input().split()
        if _[0] in "+*":
            op[i] = _[0]
            l, r = map(int, _[1:])
            AL[i] = [l, r]
        else:
            a[i] = int(_[0])
    def dfs(u):
        if not AL[u]:
            return str(a[u]), None, a[u]
        res_strings = []
        res_values = []
        child_ops = []
        for v in AL[u]:
            s, o, val = dfs(v)
            res_strings.append(s)
            child_ops.append(o)
            res_values.append(val)
        if op[u] == '*':
            for i in range(len(AL[u])):
                if child_ops[i] == '+':
                    res_strings[i] = f'({res_strings[i]})'
        s = op[u].join(res_strings)
        v = sum(res_values) if op[u] == '+' else 1
        if op[u] == '*':
            for val in res_values:
                v *= val
        return s, op[u], v
    ans = dfs(1)
    print(f"{ans[0]}={ans[2]}")
if __name__ == "__main__":
    main()