import heapq
import math
import sys, bisect
from itertools import accumulate
from collections import Counter
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
    n, m , k = ints()
    a = list(ints())
    b = list(ints())
    minh = []
    for i in range(len(a)):
        heapq.heappush(minh, (a[i] + b[0], i + 1, 1))
    for i in range(k):
        x = heapq.heappop(minh)
        print(x[1],x[2])
        if x[2] < m:
            heapq.heappush(minh,( b[x[2]] + a[x[1] - 1], x[1], x[2] + 1))



if __name__ == "__main__":
    main()
