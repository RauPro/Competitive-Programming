from heapq import heappop, heappush
n, m, t = map(int, input().split())
AL = [[] for i in range(n + 1)]
for i in range(m):
    x, y, l, w1, w2 = map(int, input().split())
    AL[x].append((y, l, w1, w2))
    AL[y].append((x, l, w1, w2))
#t, dist
pq =  [(0.0, 1)]
INF = int(1e9)
times = [INF] * int(10e5 + 5)
times[1] = 0
while pq:
    time, u = heappop(pq)
    if time > times[u]: continue
    for v, l, w1, w2 in AL[u]:
        new_time = l / (w1 if time < t else w2)
        if time < t and new_time + time > t:
            new_time = time + (l - (t - time)) * w1
            new_time /= w2
        """ new_time = 0
        if time < t:
            new_time = l / w1
            if new_time + time >= t:
                tiempo_delta = t - time
                distancia_delta = tiempo_delta * w1
                distancia_theta = l - distancia_delta
                tiempo_theta = distancia_theta / w2
                new_time = tiempo_theta + tiempo_delta
        else:
            new_time = l / w2
        new_time += time"""
        if new_time < times[v]:
            times[v] = new_time
            heappush(pq, (new_time, v))
print(times[n])

