if __name__ == "__main__":
    n = int(input())
    s = input()
    if s.count("xxx") == 0:
        print(0)
    else:
        ans = 0
        for i in range(len(s)-2):
            if s[i:i+3] == "xxx":
                ans +=1
        print(ans)