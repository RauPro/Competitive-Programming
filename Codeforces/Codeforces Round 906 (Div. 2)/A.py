from collections import defaultdict


def can_be_good(a):
    mapper = defaultdict(lambda: 0)

    for num in a:
        if num in mapper:
            mapper[num] += 1
        else:
            mapper[num] = 1

    if len(mapper) == 1:
        print("YES")
    elif len(mapper) > 2:
        print("NO")
    else:
        num1 = list(mapper.values())
        if num1[0] == num1[1]:
            print("YES")
        elif num1[0] + 1 == num1[1] or num1[0] == num1[1] + 1:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        nums = list(map(int, input().split()))
        can_be_good(nums)