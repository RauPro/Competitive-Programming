import sys, bisect
from collections import Counter
from itertools import accumulate
input = lambda: sys.stdin.readline().rstrip("\r\n")
flush = lambda: sys.stdout.flush()
print = lambda *args, **kwargs: sys.stdout.write(' '.join(map(str, args)) + kwargs.get("end", "\n")) and flush()
def ints(): return map(int, input().split())
def strs(): return input().split()
def chars(): return list(input().strip())
def mat(n): return [list(ints()) for _ in range(n)]
def counting_sort(a):
    freq = Counter(a)
    for i in range(1, max(a) + 1):
        freq[i] += freq[i - 1]
    ans = [0] * len(a)
    for x in reversed(a):
        freq[x] -= 1
        ans[freq[x]] = x
    return ans
def main():
    n = int(input())
    print(*counting_sort(list(ints())))
if __name__ == "__main__":
    main()
