import sys
from functools import lru_cache
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
    for i in range(2, n + 1):
        id = int(input())
        AL[id].append(i)
    @lru_cache(None)
    def dp(u):
        if not AL[u]: return False
        for v in AL[u]:
            if not dp(v): return True
        return False
    print("First" if dp(1) else "Second")
if __name__ == "__main__":
    main()