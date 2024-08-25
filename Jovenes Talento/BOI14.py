import os
import sys
from collections import *
from heapq import *
from math import gcd, floor, ceil, sqrt
from copy import deepcopy
from itertools import permutations, combinations, product
from bisect import bisect_left, bisect_right
from functools import lru_cache, reduce
import operator
from random import getrandbits

input = lambda: sys.stdin.readline().strip()
flush = lambda: sys.stdout.flush()
print = lambda *args, **kwargs: sys.stdout.write(' '.join(map(str, args)) + kwargs.get("end", "\n")) and flush()

sys.setrecursionlimit(100000)
MOD = 1000000007
MAX_NODES = 500010

def ints(): return map(int, input().split())
def strs(): return input().split()
def chars(): return list(input().strip())
def mat(n): return [list(ints()) for _ in range(n)]



AL = [[] for _ in range(MAX_NODES)]
visited = [0] * MAX_NODES
edge_visited = [0] * MAX_NODES
index_tracker = [0] * MAX_NODES
ans = [0] * MAX_NODES


def dfs(u, size):
    visited[u] = 1
    ans[size] = u

    while index_tracker[u] < len(AL[u]):
        v, edge_index = AL[u][index_tracker[u]]
        index_tracker[u] += 1

        if edge_visited[edge_index]:
            continue
        edge_visited[edge_index] = 1

        if not visited[v]:
            returned_node = dfs(v, size + 1)
            if returned_node == u:
                continue
            else:
                visited[u] = 0
                return returned_node
        else:
            prt = []
            for j in range(size, -1, -1):
                prt.append(ans[j])
                if ans[j] == v:
                    break
            print(*prt)
            visited[u] = 0
            return v
    return 0

def solve():
    n, m = ints()

    for i in range(m):
        u, v = ints()
        AL[u].append((v, i))
        AL[v].append((u, i))
        print(u,v, i)

    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i, 0)


def main():
    solve()


if __name__ == "__main__":
    main()
