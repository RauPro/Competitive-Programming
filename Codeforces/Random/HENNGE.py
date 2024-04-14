def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print(sum_squares(0, a, 0))


def sum_squares(n ,a , i):
    if i == len(a):
        return n
    if a[i] > 0:
        return sum_squares(n + a[i] ** 2, a, i + 1)
    else:
        return sum_squares(n, a, i + 1)


if __name__ == "__main__":
    main()
