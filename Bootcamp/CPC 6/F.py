def hopcroft_karp(graph, n, m):
    """
    Maximum bipartite matching using Hopcroft-Karp algorithm, running in O(|E| sqrt(|V|))
    """
    assert (n == len(graph))
    match1 = [-1] * n
    match2 = [-1] * m

    # Find a greedy match for possible speed up
    for node in range(n):
        for nei in graph[node]:
            if match2[nei] == -1:
                match1[node] = nei
                match2[nei] = node
                break
    while 1:
        bfs = [node for node in range(n) if match1[node] == -1]
        depth = [-1] * n
        for node in bfs:
            depth[node] = 0

        for node in bfs:
            for nei in graph[node]:
                next_node = match2[nei]
                if next_node == -1:
                    break
                if depth[next_node] == -1:
                    depth[next_node] = depth[node] + 1
                    bfs.append(next_node)
            else:
                continue
            break
        else:
            break

        pointer = [len(c) for c in graph]
        dfs = [node for node in range(n) if depth[node] == 0]
        while dfs:
            node = dfs[-1]
            while pointer[node]:
                pointer[node] -= 1
                nei = graph[node][pointer[node]]
                next_node = match2[nei]
                if next_node == -1:
                    # Augmenting path found
                    while nei != -1:
                        node = dfs.pop()
                        match2[nei], match1[node], nei = node, nei, match1[node]
                    break
                elif depth[node] + 1 == depth[next_node]:
                    dfs.append(next_node)
                    break
            else:
                dfs.pop()
    return match1, match2


t = int(input())

for _ in range(t):
    n, *a = map(int, input().split())
    a_ = {a[i]: i+1 for i in range(n)}
    m, *b = map(int, input().split())
    b_ = {b[i]: n+i+1 for i in range(len(b))}

    AL = [[] for i in range(n + m + 1)]
    for i in range(len(a)):
        for j in range(len(b)):
            if b[j] == 0 or (a[i] and b[j] % a[i] == 0):
                AL[i].append(j + n)
                #AL[j + n].append(i)

    #print(hopcrfot_karp(AL, n+m + 5, n+m + 5))
    #print(sum(1 for it in hopcrfot_karp(AL, n+m + 5, n+m + 5)[0] if it != -1))
    print("Case " + str(_+1) + ": " + str((sum(1 for it in hopcroft_karp(AL, len(AL), len(AL))[1] if it != -1))))
