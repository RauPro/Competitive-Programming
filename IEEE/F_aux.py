def maximize_number_greedy(N, K):
    num_list = list(str(N))
    n = len(num_list)
    def find_max_position(start):
        max_digit = '0'
        max_pos = start
        for i in range(n - 1, start - 1, -1):
            if num_list[i] > max_digit:
                max_digit = num_list[i]
                max_pos = i
        return max_pos
    k = K
    for i in range(n):
        if k <= 0:
            break
        max_pos = find_max_position(i)
        if num_list[i] != num_list[max_pos]:
            num_list[i], num_list[max_pos] = num_list[max_pos], num_list[i]
            k -= 1
    ans = ''.join(num_list)
    return ans

n, k= map(str, input().split())
N = n.strip()
K = int(k)

ans = maximize_number_greedy(N, K)
print(ans)