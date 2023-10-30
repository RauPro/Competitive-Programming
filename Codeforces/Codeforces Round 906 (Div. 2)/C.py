import sys

input = sys.stdin.readline
def solve():
    n = int(input())
    s = input()

    one_counter = s.count('1')
    zero_counter = n - one_counter
    if one_counter != zero_counter:
        print(-1)
        return

    l, r = 0, n - 1
    ans = []
    iter = 0
    while l < r and iter <= 300:
        if r >= len(s) or s[l] != s[r]:
            l += 1
            r -= 1
            continue

        if s[l] == '1':
            ans.append(l)
        else:
            ans.append(r + 1)

        s = s[:ans[-1]] + "01" + s[ans[-1]:]
        l += 1
        r += 1
        iter += 1
        if iter > 300:
            print(-1)
            return
    print(len(ans))
    print(*ans)

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        solve()
