import sys, bisect, math

input = lambda: sys.stdin.readline().rstrip("\r\n")
flush = lambda: sys.stdout.flush()
print = lambda *args, **kwargs: sys.stdout.write(' '.join(map(str, args)) + kwargs.get("end", "\n")) and flush()
def ints(): return map(int, input().split())
def strs(): return input().split()
def chars(): return list(input().strip())
def mat(n): return [list(ints()) for _ in range(n)]

def main():
    a = list(ints())
    def pol(x):
        return a[0]*x**3 + a[1]*x**2 + a[2]*x + a[3]
    lo = -10000.0
    hi = 10000.0
    while hi - lo > 1e-9:
        mid = (lo + hi) / 2
        if pol(lo) * pol(mid) <= 0:
            hi = mid
        else:
            lo = mid
    print(f"{(lo + hi) / 2:.5f}")


if __name__ == "__main__":
    main()