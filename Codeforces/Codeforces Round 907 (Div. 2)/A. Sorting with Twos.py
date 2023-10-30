def check_sorted(a):
    if len(a) == 1:
        return True
    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:
            return False
    return True


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    limit = 0

    ans = False
    if check_sorted(a):
        print("YES")
    else:
        for i in range(len(a) - 1):
            if 2 ** i > len(a):
                limit = i - 1
                break
            else:
                max_v = max(a[:2 ** i])
                for i_ in range(2**i):

                    a[i_] -= max_v
        print("YES" if check_sorted(a) else "NO")