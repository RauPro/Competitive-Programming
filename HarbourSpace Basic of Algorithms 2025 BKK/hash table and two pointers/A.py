import sys, bisect

input = lambda: sys.stdin.readline().rstrip("\r\n")
flush = lambda: sys.stdout.flush()
print = lambda *args, **kwargs: sys.stdout.write(' '.join(map(str, args)) + kwargs.get("end", "\n")) and flush()
def ints(): return map(int, input().split())
def strs(): return input().split()
def chars(): return list(input().strip())
def mat(n): return [list(ints()) for _ in range(n)]

def main():
    n, x = ints()
    a = sorted((v, i + 1) for i, v in enumerate(list(ints())))
    for i in range(n - 1):
        x_, left, right = x - a[i][0], i + 1, n - 1
        while left < right:
            s = a[left][0] + a[right][0]
            if s == x_: print(a[i][1], a[left][1], a[right][1]); exit()
            if s < x_: left += 1
            else: right -= 1
    print(-1, -1, -1)

if __name__ == "__main__":
    main()
