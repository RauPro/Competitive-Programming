import sys, bisect
from collections import defaultdict
input = lambda: sys.stdin.readline().rstrip("\r\n")
flush = lambda: sys.stdout.flush()
print = lambda *args, **kwargs: sys.stdout.write(' '.join(map(str, args)) + kwargs.get("end", "\n")) and flush()
def ints(): return map(int, input().split())
def strs(): return input().split()
def chars(): return list(input().strip())
def mat(n): return [list(ints()) for _ in range(n)]

def merge(a, b):
    i, j = 0, 0
    ans = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]: ans.append(a[i]);i+=1
        else: ans.append(b[j]); j+= 1
    if i < len(a): ans.extend(a[i:])
    else: ans.extend(b[j:])
    return  ans

def merge_sort(blocks, l, r):
    if l == r: return blocks[l]
    mid = (l + r) // 2
    left = merge_sort(blocks, l, mid)
    right = merge_sort(blocks, mid + 1,  r)
    return merge(left, right)

def main():
    n = int(input())
    blocks = [list(ints()) for i in range(n)]
    print(*merge_sort(blocks, 0, n-1))
if __name__ == "__main__":
    main()
