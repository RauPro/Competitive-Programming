import sys, bisect

input = lambda: sys.stdin.readline().rstrip("\r\n")
flush = lambda: sys.stdout.flush()
print = lambda *args, **kwargs: sys.stdout.write(' '.join(map(str, args)) + kwargs.get("end", "\n")) and flush()
def ints(): return map(int, input().split())
def strs(): return input().split()
def chars(): return list(input().strip())
def mat(n): return [list(ints()) for _ in range(n)]

def main():
    n, q = ints()
    a = list(ints())
    for _ in range(q):
        x = int(input())
        lo, hi = 0, n - 1
        ans_lo = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if a[mid] < x:
                lo = mid + 1
            else:
                if a[mid] == x:
                    ans_lo = mid
                hi = mid - 1
        lo, hi = 0, n - 1
        ans_hi = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if a[mid] <= x:
                if a[mid] == x:
                    ans_hi = mid
                lo = mid + 1
            else:
                hi = mid - 1
        print("-1 -1" if ans_lo == -1 else f"{ans_lo + 1} {ans_hi + 1}")
"""
this is what i used in real problem :P
lo = bisect.bisect_left(a, x)
hi = bisect.bisect_right(a, x)
print(f"{lo + 1} {hi}" if lo < n and a[lo] == x else f"-1 -1")"""



if __name__ == "__main__":
    main()
