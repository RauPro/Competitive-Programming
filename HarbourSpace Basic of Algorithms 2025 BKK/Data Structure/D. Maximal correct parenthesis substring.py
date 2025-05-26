import sys, bisect

input = lambda: sys.stdin.readline().rstrip("\r\n")
flush = lambda: sys.stdout.flush()
print = lambda *args, **kwargs: sys.stdout.write(' '.join(map(str, args)) + kwargs.get("end", "\n")) and flush()
def ints(): return map(int, input().split())
def strs(): return input().split()
def chars(): return list(input().strip())
def mat(n): return [list(ints()) for _ in range(n)]

def main():
    s = input()
    stack = [-1]
    ans = 0
    l = r = 0
    for i, c in enumerate(s):
        if c == '(': stack.append(i)
        else:
            stack.pop()
            if not stack: stack.append(i)
            else:
                if (length := i - stack[-1]) > ans:
                    ans, l, r = length, stack[-1] + 1, i + 1
    print(f"{l} {r}" if ans else "-1 -1")



if __name__ == "__main__":
    main()
