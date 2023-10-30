t = int(input().strip())

for _ in range(t):
    n, m, k = map(int, input().strip().split())
    intervals = [list(map(int, input().strip().split())) for _ in range(m)]

    # Create a list where index i contains the number of days it will rain in city i
    city_rain_days = [0] * (n + 1)
    for l, r in intervals:
        for i in range(l, r + 1):
            city_rain_days[i] += 1

    # Calculate the number of cities that would be dry if it doesn't rain on a particular day
    day_effect = []
    for l, r in intervals:
        effect = 0
        for i in range(l, r + 1):
            if city_rain_days[i] == 1:
                effect += 1
        day_effect.append(effect)

    # Find the two days that give maximum combined effect
    max_dry = 0
    for i in range(m):
        for j in range(i + 1, m):
            max_dry = max(max_dry, day_effect[i] + day_effect[j])

    # The cities that are always dry are the ones which have 0 in city_rain_days
    always_dry = city_rain_days.count(0)

    print(max_dry + always_dry)
