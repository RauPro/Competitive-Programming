
n = int(input())
a = list(map(int, input().split()))
frec = {0: 1}
bits = 0
ans = 0
for i in range(1, n):
    if a[i] > a[i-1]:
        bits += 1
    else:
        bits -= 1
    if bits in frec:
        ans += frec[bits]
        frec[bits] +=1
    else:
        frec[bits] = 1
#print(ans)
print(ans + n)