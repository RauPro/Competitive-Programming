from itertools import accumulate
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = map(int, input().split())
    prefix = [0] + list(accumulate(a))
    total = prefix[-1]
    for i in range(m):
        sd, sm, ed, em = map(int, input().split())
        arrival_day = prefix[sm - 1] + sd
        depart_day = prefix[em - 1] + ed
        ans = 0
        if depart_day >= arrival_day:
            ans = depart_day - arrival_day + 1
        else:
            ans = total - arrival_day + depart_day + 1
        print(ans)