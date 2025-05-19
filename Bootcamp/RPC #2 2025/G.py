from collections import Counter
from copy import deepcopy
from symbol import continue_stmt

n, a = int(input()),  list(input().split())
last = [int(it[-1]) % 5 for it in a]
freq = Counter(last)
def one(freq_):
    counter = min(freq[3], freq[4])
    ans = 2 * counter
    freq_[3] -= counter
    freq_[4] -= counter
    ans += 2 * (freq_[4] // 3)
    ans += (freq_[3] // 2)
    return 0.01 * (ans + (1 * freq_[1]) + 2 * freq_[2])

def second(freq_):
    counter = (freq_[4] // 3)
    ans = 2 * counter
    freq_[4] -= counter
    counter = min(freq_[3], freq_[4])
    ans += 2 * counter
    freq_[3] -= counter
    freq_[4] -= counter
    ans += (freq_[3] // 2)
    return 0.01 * (ans + (1 * freq_[1]) + 2 * freq_[2])

total = sum([float(it) for it in a])

#print(one(deepcopy(freq)), second(deepcopy(freq)))
ans = (total - max(one(deepcopy(freq)), second(deepcopy(freq))))

#print(total, ans)

print(f"{ans:.2f}")