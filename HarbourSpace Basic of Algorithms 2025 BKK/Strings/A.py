import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")
flush = lambda: sys.stdout.flush()
print = lambda *args, **kwargs: sys.stdout.write(' '.join(map(str, args)) + kwargs.get("end", "\n")) and flush()
def ints(): return map(int, input().split())
def strs(): return input().split()
def chars(): return list(input().strip())
def mat(n): return [list(ints()) for _ in range(n)]

def main():
    n, m = ints()
    match = {}
    for _ in range(n):
        s, f = strs();f = int(f)
        for i in range(len(s)):
            p = s[:i+1]
            if p not in match or match[p][0] < f: match[p] = (f, s)
    for _ in range(m):
        print(match[input()][1])

if __name__ == "__main__":
    main()