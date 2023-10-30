def process(a1, a2, a, n):
    d = a2 - a1
    cur = a2
    res = 0
    for i in range(2, n):
        if abs(cur + d - a[i]) > 1:
            return float('inf')
        if abs(cur + d - a[i]) != 0:
            res += 1
        cur += d
    return res

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    if n <= 2:
        print("0")
    else:
        res = float('inf')
        d1 = [-1, 0, 1]
        d2 = [-1, 0, 1]
        for i in d1:
            for j in d2:
                add = (i != 0) + (j != 0)
                res = min(res, process(a[0] + i, a[1] + j, a, n) + add)
        if res == float('inf'):
            res = -1
        print(res)
