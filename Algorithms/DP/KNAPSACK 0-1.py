def knapSack( W, wt, val, n):
    ans = 0

    def kns(index, remW):
        if index == n or remW == 0:
            return 0
        if wt[index] > remW:
            return kns(index + 1, remW)
        return max(kns(index + 1, remW), val[index] + kns(index + 1, remW - wt[index]))

    ans = kns(0, W)
    return ans

n = int(input())
w = int(input())
vals = list(map(int, input().split()))
wt = list(map(int, input().split()))

print(knapSack(w, wt, vals, n))