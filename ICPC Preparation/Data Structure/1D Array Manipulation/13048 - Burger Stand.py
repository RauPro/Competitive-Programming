def validate_index(index, st):
    bus_driveway = st[index] == 'D' or st[index] == 'B' or st[index] == 'S'
    bus_5 = False
    bus_10 = False
    if index + 1 < len(st):
        bus_5 = st[index + 1] == 'B' or st[index + 1] == 'S'
    if index + 2 < len(st):
        bus_10 = st[index + 2] == 'B'
    if index - 1 >= 0:
        bus_5 = bus_5 or st[index - 1] == 'S'
    return bus_driveway or bus_5 or bus_10

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = input()
        ans = 0

        for i in range(len(s)):
            ans += not validate_index(i, s)
        print("Case {}:".format(_ + 1), ans)
