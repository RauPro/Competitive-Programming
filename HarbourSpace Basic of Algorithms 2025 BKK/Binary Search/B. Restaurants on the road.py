import sys, bisect

input = lambda: sys.stdin.readline().rstrip("\r\n")
flush = lambda: sys.stdout.flush()
print = lambda *args, **kwargs: sys.stdout.write(' '.join(map(str, args)) + kwargs.get("end", "\n")) and flush()
def ints(): return map(int, input().split())
def strs(): return input().split()
def chars(): return list(input().strip())
def mat(n): return [list(ints()) for _ in range(n)]

def can(mid, a, k):
    ans = [a[0]]
    index = 1
    while len(ans) < k and index < len(a):
        if a[index] - ans[-1] >= mid:
            ans.append(a[index])
        index += 1
    return len(ans) == k

def main():
    n, k = ints()
    a = list(ints())
    lo, hi = 0, int(10**9) + 1
    while lo < hi:
        mid = (lo + hi) // 2
        if can(mid, a, k):
            lo = mid + 1
        else:
            hi = mid
    ans = [a[0]]
    index = 1
    while len(ans) < k and index < len(a):
        if a[index] - ans[-1] >= lo - 1:
            ans.append(a[index])
        index += 1
    print(" ".join(map(str, ans)))



if __name__ == "__main__":
    main()
