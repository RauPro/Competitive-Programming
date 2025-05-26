import sys, bisect
from collections import defaultdict

input = lambda: sys.stdin.readline().rstrip("\r\n")
flush = lambda: sys.stdout.flush()
print = lambda *args, **kwargs: sys.stdout.write(' '.join(map(str, args)) + kwargs.get("end", "\n")) and flush()
def ints(): return map(int, input().split())
def strs(): return input().split()
def chars(): return list(input().strip())
def mat(n): return [list(ints()) for _ in range(n)]

def main():
    n, K = ints()
    pages = [set(strs()) for _ in range(n)]
    mapper = defaultdict(set)
    for i, p in enumerate(pages):
        for w in p:  mapper[w].add(i + 1)
    for _ in range(int(input())):
        el = [w for w in strs() if len(mapper[w]) <= K]
        if not el: print(-1)
        else:
            ans = mapper[el[0]].copy()
            for w in el[1:]: ans &= mapper[w]
            print(*sorted(ans) or [-1])

if __name__ == "__main__":
    main()
