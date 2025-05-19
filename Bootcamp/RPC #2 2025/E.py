n, k, p = map(int, input().split())
n = 0.1 * n
k = 0.1 * k
wrong = p/100
success = 1 - (p / 100)
#print(wrong, success)
continue_ = (0.1 + n - k) + (wrong * (0.1 + n + 0.3))
backspace = (0.2 + n - k) +  (success * (0.1 + n + 0.3))
reset = (0.1 + 0.3 + n)
#print(continue_, backspace, reset)
if continue_ < backspace and continue_ < reset:
    print("continue")
elif backspace < continue_  and backspace < reset:
    print("backspace")
else:
    print("restart")
