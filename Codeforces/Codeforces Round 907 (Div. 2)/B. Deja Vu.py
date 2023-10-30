input = __import__('sys').stdin.readline


def apply_modifications(n, q, array_a, queries_x):
    unique_add = [[] for _ in range(35)]
    additions = {x: 1 << (x - 1) for x in range(1, 31)}
    for i, x in enumerate(array_a):
        cnt = 0
        while x % 2 == 0:
            x = x // 2
            cnt += 1
        unique_add[cnt].append(i)

    for x in queries_x:
        val = additions[x]
        for v in range(x, 33):
            for i in unique_add[v]:
                unique_add[x - 1].append(i)
                array_a[i] += val
            unique_add[v] = []

    return array_a


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, q = map(int, input().split())
        array_a = list(map(int, input().split()))
        queries_x = list(map(int, input().split()))
        array_a = apply_modifications(n, q, array_a, queries_x)
        print(' '.join(map(str, array_a)))