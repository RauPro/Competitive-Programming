

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
index_a = {}
index_b = {}

for i, it in enumerate(a):
    index_a[it] = i


for i, it in enumerate(b):
    index_b[it] = i

ans = 0
for i in range(n):
    if a[i] == i+1:
        continue
    to_find = i + 1
    if to_find != a[i]:
        ans+=1
        old_index = index_a[to_find]
        old_element = a[i]
        a[index_a[to_find]] = a[i]
        a[i] = to_find
        index_a[old_element] = old_index

for i in range(n):
    if b[i] == i+1:
        continue
    to_find = i + 1
    if to_find != b[i]:
        ans+=1
        old_index = index_b[to_find]
        old_element = b[i]
        b[index_b[to_find]] = b[i]
        b[i] = to_find
        index_b[old_element] = old_index
print(ans)
