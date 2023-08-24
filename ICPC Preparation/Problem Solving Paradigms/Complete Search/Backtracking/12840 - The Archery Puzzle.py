def coinChange(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    combinations = [None] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin < 0:
                continue

            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                if combinations[i - coin] is None:
                    combinations[i] = [coin]
                else:
                    combinations[i] = [coin] + combinations[i - coin]

    if dp[amount] == float('inf'):
        return -1, []
    else:
        return dp[amount], combinations[amount]

def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        array = input()
        array = [int(v) for v in array.split()]
        array.reverse()
        #print(array)
        count, ans = coinChange(array, m)
        #sorted(ans)
        #ans.reverse()
        # print(_)
        if count == -1:
            print("Case "+ str(_+1) + ": impossible")
        else:
            print("Case " + str(_+1) + ": [" + str(len(ans))+ "] " + " ".join(map(str, ans)))


if __name__ == '__main__':
    main()
