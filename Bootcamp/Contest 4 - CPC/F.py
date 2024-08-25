from functools import lru_cache

@lru_cache(maxsize=None)
def ways(index, pf, pd):
    if index == n:
        return 0
    if pf * 3 >= 50 or pd * 3 >= 50 or pf * 3 + pd * 3 >= 90:
        return 0
    ans = 0
    if (pf + F[index]) * 3 < 50 and (pd + D[index]) * 3 < 50 and ((pf + F[index]) * 3) + ((pd + D[index]) * 3) < 90: ans = ways(index + 1, pf + F[index], pd + D[index]) + 1
    return max(ways(index + 1, pf, pd), ans)


F, D = [], []
n = int(input())
for i in range(n):
    idex, pf, pd = map(int, input().split())
    F.append(pf)
    D.append(pd)
#print(ways(0, 0 , 0))
print(80 - (n - ways(0, 0 , 0)))