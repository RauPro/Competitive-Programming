from collections import Counter
from functools import lru_cache
n = int(input())
a = list(map(int, input().split()))
a.sort()
w = sum(a) // 2
if w * 2 != sum(a):
    print(-1)
    exit(0)

global_ans = []
memo = [[-1] * (100 * 101) for i in range(101)]

def knapsack(id, remW, ans):
    global global_ans
    if remW == 0:
        global_ans = ans
    if id == n or remW == 0:
        return 0
    if memo[id][remW] != -1:
        return memo[id][remW]
    if a[id] > remW:
        memo[id][remW] = knapsack(id + 1, remW, ans)
        return memo[id][remW]
    exclude = knapsack(id + 1, remW, ans)
    aux = ans.copy()
    aux.append(a[id])
    memo[id][remW] = knapsack(id + 1, remW - a[id], aux)
    rem = memo[id][remW]
    included = a[id] + rem
    if exclude < included:
        return included
    else:
        return exclude


cur_w = knapsack(0, w, [])
if cur_w * 2 != sum(a):
    print(-1)
    exit(0)

frec = Counter(global_ans)
bob = []
for it in a:
    if it in frec and frec[it] >= 1:
        frec[it] -= 1
        continue
    bob.append(it)
# print(cur_w, w, global_ans, bob)
i = 0
i_bob = 0
i_alice = 0
total_alice = 0
total_bob = 0
ans = []
while i != n:
    if total_alice <= total_bob and i_alice < len(global_ans):
        ans.append(global_ans[i_alice])
        total_alice += global_ans[i_alice]
        i_alice += 1

    else:
        ans.append(bob[i_bob])
        total_bob += bob[i_bob]
        i_bob += 1
    i += 1
print(*ans)