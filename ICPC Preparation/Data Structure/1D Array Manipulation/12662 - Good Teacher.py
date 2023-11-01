def near_value_of_index(arr, index):
    min_distL = int(1e9)
    min_distR = int(1e9)
    elementL = ""
    elementR = ""
    for i in range(index, len(arr)):
        if arr[i] != '?':
            min_distL = i - index
            elementL = arr[i]
            break
    for i in range(index, -1, -1):
        if arr[i] != '?':
            min_distR = index - i
            elementR = arr[i]
            break
    if min_distL > 0 and min_distL == min_distR:
        ans = ["middle of"]
        print(" ".join(ans), elementR, "and", elementL)
    elif min_distL > min_distR:
        ans = ["right of"] * min_distR
        print(" ".join(ans), elementR)
    elif min_distL < min_distR:
        ans = ["left of"] * min_distL
        print(" ".join(ans), elementL)
    return min(min_distL, min_distR), elementR if min_distL > min_distR else elementL
if __name__ == "__main__":
    n = int(input())
    arr = list(map(str, input().split()))
    t = int(input())
    for _ in range(t):
        index = int(input())
        min_dist, element = near_value_of_index(arr, index-1)
        if min_dist == 0:
            print(element)