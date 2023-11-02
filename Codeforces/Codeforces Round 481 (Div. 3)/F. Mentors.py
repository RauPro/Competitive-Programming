input = __import__('sys').stdin.readline

# Binary Search first element greater than target
def binary_search(arr, target):
    l, r = 0, len(arr) - 1
    ans = -1
    while l <= r:
        mid = (l + r) // 2
        val, idx = arr[mid]
        if val > target:
            ans = mid
            r = mid - 1
        else:
            l = mid + 1
    return arr[ans][1]

if __name__ == "__main__":
    n, k = map(int, input().split())
    programers = list(map(int, input().split()))
    programers = [(pop, i) for i, pop in enumerate(programers)]
    programers.sort()
    print(programers)
    pairs = [[] for _ in range(n)]
    for _ in range(k):
        a, b = map(int, input().split())
        pairs[a - 1].append(b-1)
        pairs[b - 1].append(a-1)
    ans = [0] * n
    for i in range(n):
        index = binary_search(programers, programers[i][0])
        print(index)
    print(*ans)
