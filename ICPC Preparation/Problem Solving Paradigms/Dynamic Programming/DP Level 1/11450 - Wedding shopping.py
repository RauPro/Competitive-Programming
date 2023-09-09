from collections import defaultdict
import sys
from functools import lru_cache
sys.setrecursionlimit(5000)




if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        m, c = map(int, input().split())
        g = [[] * 20 for i in range(c)]
        for case in range(c):
            g[case] = list(map(int, input().split()))


        @lru_cache(maxsize=None)
        def buy(dinero, g_i):
            if dinero < 0:
                return -1e9
            if g_i == c:
                return m - dinero
            ans = -1
            for model in range(1, g[g_i][0] + 1):
                ans = max(buy(dinero - g[g_i][model], g_i + 1), ans)
            return ans


        sol = buy(m, 0)
        if sol != -1:
            print(sol)
        else:
            print("no solution")
