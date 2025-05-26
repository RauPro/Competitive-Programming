import sys, bisect
from collections import defaultdict
from bisect import bisect_left, bisect_right
input = lambda: sys.stdin.readline().rstrip("\r\n")
flush = lambda: sys.stdout.flush()
print = lambda *args, **kwargs: sys.stdout.write(' '.join(map(str, args)) + kwargs.get("end", "\n")) and flush()
def ints(): return map(int, input().split())
def strs(): return input().split()
def chars(): return list(input().strip())
def mat(n): return [list(ints()) for _ in range(n)]
def main():
    n, m = ints()
    lo, hi = map(sorted, zip(*[ints() for _ in range(n)]))
    print(lo)
    print(hi)
    print((bisect_right(lo, 4), bisect_left(hi, 4)))
    print(*(bisect_right(lo, x) - bisect_left(hi, x) for x in ints()))
if __name__ == "__main__":
    main()
