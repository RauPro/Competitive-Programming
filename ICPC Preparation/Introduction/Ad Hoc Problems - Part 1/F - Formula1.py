from collections import defaultdict
while True:
    g, p = map(int, input().split())
    if g == p == 0:
        break
    grand_prix = []
    for i in range(g):
        road = list(map(int, input().split()))
        grand_prix.append(road)
    s = int(input())
    for _ in range(s):
        systems = list(map(int, input().split()))
        for i in range(p):
            systems.append(0)
        score = [0 for w in range(p+1)]
        systems = systems[1:]
        for i in range(g):
            for j in range(p):
                score[j] += systems[grand_prix[i][j] - 1]

        m = max(score)
        identifier = []
        ad_winner = defaultdict(lambda: False)
        for i in range(p):
            if score[i] == m and not ad_winner[i]:
                identifier.append(i+1)
                ad_winner[i] = True

        print(identifier)