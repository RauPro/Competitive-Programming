n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
k = int(input())
MOD = int(1e9 + 7)
p = 131
def prepareP(n):
    P = [0] * n
    P[0] = 1
    for i in range(1, n):
        P[i] = P[i-1] * p % MOD
    return P
def computeRollingHash(T: str):
    P = prepareP(len(T))
    h = [0] * len(T)
    for i in range(len(T)):
        if i == 0:
            h[i] = h[i-1]
        h[i] = h[i] + (T[i] * P[i] % MOD) % MOD


for i in range(k):
    a, b = map(int, input().split())
