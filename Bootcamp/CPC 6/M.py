n = int(input())
F = [0] * 5

for i in range(n):
    s = input()
    if s[0] == 'M': F[0] += 1
    if s[0] == 'A': F[1] += 1
    if s[0] == 'R': F[2] += 1
    if s[0] == 'C': F[3] += 1
    if s[0] == 'H': F[4] += 1
#print(F)
ans = 0
for i in range(5):
    for j in range(i+1, 5):
        for k in range(j+1, 5):
            ans += F[i] * F[j] * F[k]

print(ans)