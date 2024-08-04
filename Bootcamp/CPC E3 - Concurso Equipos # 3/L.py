def preprocess(s):
    n = len(s)
    distinct_count = [0] * n
    last_position = {}
    count = 0

    for i in range(n):
        if s[i] not in last_position:
            count += 1
        last_position[s[i]] = i
        distinct_count[i] = count

    return distinct_count

def min_substring_with_distinct(s, l, r, distinct_count):
    target_count = distinct_count[r - 1] if l == 1 else distinct_count[r - 1] - distinct_count[l - 2]
    char_count = {}
    min_len = float('inf')
    left = l - 1
    distinct_in_window = 0

    for right in range(l - 1, r):
        if s[right] not in char_count or char_count[s[right]] == 0:
            distinct_in_window += 1
        char_count[s[right]] = char_count.get(s[right], 0) + 1

        while distinct_in_window == target_count:
            min_len = min(min_len, right - left + 1)
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                distinct_in_window -= 1
            left += 1

    return min_len

def solve(n, s, queries):
    distinct_count = preprocess(s)
    results = []

    for l, r in queries:
        result = min_substring_with_distinct(s, l, r, distinct_count)
        results.append(result)

    return results

n = int(input())
s = input().strip()
q = int(input())
queries = []

for _ in range(q):
    l, r = map(int, input().split())
    queries.append((l, r))


results = solve(n, s, queries)

for result in results:
    print(result)
