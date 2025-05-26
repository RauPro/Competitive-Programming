import sys, bisect
from collections import Counter

input = lambda: sys.stdin.readline().rstrip("\r\n")
flush = lambda: sys.stdout.flush()
print = lambda *args, **kwargs: sys.stdout.write(' '.join(map(str, args)) + kwargs.get("end", "\n")) and flush()
def ints(): return map(int, input().split())
def strs(): return input().split()
def chars(): return list(input().strip())
def mat(n): return [list(ints()) for _ in range(n)]

def main():
    s = input()
    t = input()
    frec = Counter(t)
    for i, c in enumerate(s):
        frec[c] -= 1
        if i >= len(t): frec[s[i - len(t)]] += 1
        if not any(list(frec.values())): print(i - len(t) + 2); exit()
    print(-1)


if __name__ == "__main__":
    main()
