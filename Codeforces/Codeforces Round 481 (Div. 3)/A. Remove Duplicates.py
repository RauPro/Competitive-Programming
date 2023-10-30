if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    set_arr = list(set(arr))
    ans = []
    for i in range(len(arr)-1, -1, -1):
        if arr[i] in set_arr:
            ans.append(arr[i])
            set_arr.remove(arr[i])

    reversed_ans = reversed(ans)
    print(len(ans))
    print(*reversed_ans)