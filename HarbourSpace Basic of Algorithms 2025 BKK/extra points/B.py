import sys
from bisect import bisect_left, bisect_right
input = lambda: sys.stdin.readline().rstrip("\r\n")
flush = lambda: sys.stdout.flush()
print = lambda *args, **kwargs: sys.stdout.write(' '.join(map(str, args)) + kwargs.get("end", "\n")) and flush()
def ints(): return map(int, input().split())
def strs(): return input().split()
def chars(): return list(input().strip())
def mat(n): return [list(ints()) for _ in range(n)]



def main():
    n = int(input())
    a = []
    for _ in range(n):
        q, x = strs()
        if q == "add":
            a = a[:bisect_left(a, x)] + [x] + a[bisect_left(a, x):]
        elif q == "delete":
            a = a[:bisect_left(a, x)] + a[bisect_right(a, x):]
        elif q == "next":
            print(a[bisect_right(a, x)] if bisect_right(a, x) < len(a) else "-")
        elif q == "prev":
            print(a[bisect_left(a, x) - 1] if bisect_left(a, x) > 0 else "-")

if __name__ == "__main__":
    main()