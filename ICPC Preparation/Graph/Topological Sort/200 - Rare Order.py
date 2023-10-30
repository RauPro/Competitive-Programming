from collections import defaultdict

def dfs(u):
    visited[u] = True

    for v in AdjList[u]:
        if not visited[v]:
            dfs(v)

    finishOrder.append(u)

if __name__ == "__main__":
    AdjList = defaultdict(list)
    visited = [False for _ in range(30)]
    appeared = [False for _ in range(30)]
    finishOrder = []

    ps = input()
    while True:
        s = input()
        if s == "#":
            break

        for i in range(min(len(s), len(ps))):
            if ps[i] != s[i]:
                appeared[ord(ps[i]) - ord('A')] = True
                appeared[ord(s[i]) - ord('A')] = True
                AdjList[ord(ps[i]) - ord('A')].append(ord(s[i]) - ord('A'))
                break

        ps = s
    #print(AdjList)
    for i in range(26):
        if not visited[i] and appeared[i]:
            dfs(i)

    for i in reversed(finishOrder):
        print(chr(i + ord('A')), end='')
    print()
