import sys, bisect
from itertools import accumulate

input = lambda: sys.stdin.readline().rstrip("\r\n")
flush = lambda: sys.stdout.flush()
print = lambda *args, **kwargs: sys.stdout.write(' '.join(map(str, args)) + kwargs.get("end", "\n")) and flush()
def ints(): return map(int, input().split())
def strs(): return input().split()
def chars(): return list(input().strip())
def mat(n): return [list(ints()) for _ in range(n)]

def main():
    n, x = ints()
    s = 0; mapper = {0: 0}
    for i, v in enumerate(map(int, input().split()), 1):
        s += v
        if s - x in mapper: print(mapper[s - x] + 1, i); exit()
        mapper.setdefault(s, i)
    print(-1, -1)

if __name__ == "__main__":
    main()
