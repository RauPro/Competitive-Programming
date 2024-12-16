t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 2
    total = 0
    index = 0
    while ans < a[-1]:
        if ans == a[index]:
            index += 1
            continue
        if a[index] - ans < 5:
            ans += a[index] - ans
            total += 1
            index += 1
        else:
            ans+= 5
            total += 1


    print(f"Case {_ +1}: {(total)}")