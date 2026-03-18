import sys
from itertools import accumulate
input = lambda: sys.stdin.readline().rstrip("\r\n")
flush = lambda: sys.stdout.flush()
print = lambda *args, **kwargs: sys.stdout.write(' '.join(map(str, args)) + kwargs.get("end", "\n")) and flush()
def ints(): return map(int, input().split())
def strs(): return input().split()
def chars(): return list(input().strip())
def mat(n): return [list(ints()) for _ in range(n)]

def main():
    n, k = ints()
    a = list(ints())
    # https://codeforces.com/blog/entry/78762
    diff = [0] * (n + 1)
    for _ in range(k):
        x, l, r = ints()
        diff[l - 1] += x;diff[r] -= x
    print(*(v + add for v, add in zip(a, accumulate(diff))))


if __name__ == "__main__":
    main()
