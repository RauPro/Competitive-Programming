from math import ceil, floor
a, b = map(int, input().split())
INF = int(1**9)
diff_a = [INF] * 101
diff_b = [INF] * 101
def claimed(num):
    total = 0
    for i in range(1, 101):
        if abs(i - num) < diff_a[i] and abs(i - num) < diff_b[i]:
            total += 1
    return total


for i in range(1, 101):
    diff_a[i] = abs(i - a)
    diff_b[i] = abs(i - b)

winne = -1
total = 0
for i in range(1, 101):
    if i != a and i != b:
        if total < claimed(i):
            total = claimed(i)
            winne = i
print(winne)
#print(claimed(69),claimed(32))
