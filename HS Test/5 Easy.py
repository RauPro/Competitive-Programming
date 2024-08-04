n, k = map(int, input().split())
s = input() + ' '
c = list(map(str, input().split()))

ans = 0
frec = 0
for it in s:
    if it in c:
        frec += 1
    else:
        ans += ((frec * (frec+1)) // 2)
        frec = 0
print(ans)