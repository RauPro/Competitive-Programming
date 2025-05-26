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
    n = int(input())
    queries = []
    a = []
    for i in range(n):
        s = input().split()
        if s[0] == 'add':
            x = int(s[1])
            queries.append(('add', x))
            a.append(x)
        else:
            queries.append(('get',))
    sorted_a = sorted(a)
    index = {v:i for i,v in enumerate(sorted_a)}
    a_  = sorted_a
    freq = [0] * len(sorted_a)
    n = len(sorted_a)
    total = 0
    ans = []
    for q in queries:
        if q[0] == 'add':
            i = index[q[1]]
            freq[i] += 1
            total += 1
            if i < n: n = i
        else:
            if total == 0: ans.append('-1')
            else:
                while freq[n] == 0: n += 1
                ans.append(str(a_[n]))
                freq[n] -= 1
                total -= 1
    print("\n".join(ans))

if __name__ == "__main__":
    main()
