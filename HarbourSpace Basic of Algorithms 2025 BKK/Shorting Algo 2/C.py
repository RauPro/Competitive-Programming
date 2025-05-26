import sys, bisect

input = lambda: sys.stdin.readline().rstrip("\r\n")
flush = lambda: sys.stdout.flush()
print = lambda *args, **kwargs: sys.stdout.write(' '.join(map(str, args)) + kwargs.get("end", "\n")) and flush()
def ints(): return map(int, input().split())
def strs(): return input().split()
def chars(): return list(input().strip())
def mat(n): return [list(ints()) for _ in range(n)]

def main():
    n = int(input())
    segments = []
    for i in range(n):
        x, y = ints()
        segments.append((x, y))
    segments.sort()
    ans = []
    i = 0
    while i < n:
        if i + 1 < n and segments[i][1] < segments[i + 1][0] or i == n - 1: ans.append(segments[i]); i+= 1
        else:
            start = segments[i][0]
            cur = segments[i][1]
            while i + 1 < n and cur >= segments[i + 1][0]:
                i += 1
                cur = max(cur, segments[i][1])
            ans.append((start, cur))
            i+= 1
    print(sum([it[1] - it[0] for it in ans]))
if __name__ == "__main__":
    main()
