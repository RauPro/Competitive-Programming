a = [5, 3 , 12, 54, 5, 5, 1, 2, 3, 3, 5]

print(len(a))
print("Average", (sum(a) / len(a)))

a.sort()

if len(a) % 2 == 0:
    index = len(a) // 2
    print("medium", ((a[index] + a[index-1]) / 2))
else:
    index = len(a) // 2
    print("medium", (a[index]))







