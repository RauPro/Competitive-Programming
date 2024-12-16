import sys
sys.setrecursionlimit(1 << 25)
N_and_rest = sys.stdin.read().split()
N = int(N_and_rest[0])
h_list = list(map(int, N_and_rest[1:N + 1]))
a_list = list(map(int, N_and_rest[N + 1:]))
N = len(h_list)
h_set = set(h_list)
h_sorted = sorted(h_set)
h_comp = {h: idx + 1 for idx, h in enumerate(h_sorted)}

h_comp_list = [h_comp[h] for h in h_list]

class FenwickTree:
    def __init__(self, size):
        self.N = size
        self.tree = [0] * (self.N + 2)

    def update(self, idx, value):
        while idx <= self.N:
            if self.tree[idx] < value:
                self.tree[idx] = value
            else:
                break
            idx += idx & -idx

    def query(self, idx):
        result = 0
        while idx > 0:
            if self.tree[idx] > result:
                result = self.tree[idx]
            idx -= idx & -idx
        return result

ft_size = len(h_comp)
ft = FenwickTree(ft_size + 2)

max_beauty = 0

for i in range(N):
    h_i = h_comp_list[i]
    a_i = a_list[i]
    max_prev = ft.query(h_i - 1)
    current = max_prev + a_i
    ft.update(h_i, current)
    if current > max_beauty:
        max_beauty = current

print(max_beauty)