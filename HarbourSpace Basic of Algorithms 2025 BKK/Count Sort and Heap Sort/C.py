import sys, bisect, heapq
from itertools import accumulate
from collections import defaultdict
input = lambda: sys.stdin.readline().rstrip("\r\n")
flush = lambda: sys.stdout.flush()
print = lambda *args, **kwargs: sys.stdout.write(' '.join(map(str, args)) + kwargs.get("end", "\n")) and flush()
def ints(): return map(int, input().split())
def strs(): return input().split()
def chars(): return list(input().strip())
def mat(n): return [list(ints()) for _ in range(n)]
minh, maxh, cnt = [], [], {}
n = int(input())
mapper= defaultdict(int)
for _ in range(n):
    s = strs()
    if s[0] == 'add':
        x = int(s[1])
        heapq.heappush(minh, x); heapq.heappush(maxh, -x)
        mapper[x] += 1
    else:
        if s[0] == "getMin":
            if len(minh ) == 0: print(-1); continue
            x = minh[0]
            while mapper[x] == 0 and len(minh ) != 0:
                x = heapq.heappop(minh)
            if len(minh) == 0 and mapper[x] == 0: print(-1); continue
            mapper[x] -= 1
            print(x)

        else:
            if len(maxh) == 0: print(-1); continue
            x = maxh[0] * -1
            while mapper[x] == 0 and len(maxh) != 0:
                x = heapq.heappop(maxh) * -1
            if len(maxh) == 0 and mapper[x] == 0: print(-1); continue
            mapper[x] -= 1
            print(x)