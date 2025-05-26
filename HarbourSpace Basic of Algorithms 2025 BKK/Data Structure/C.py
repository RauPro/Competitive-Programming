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
    p = []
    b = []
    k = []
    invalid = False
    for it in s:
        if it == '(':
            p.append('(')
        if it == '[':
            b.append('[')
        if it == '{':
            k.append('{')
        if it == '}':
            if not k:
                invalid = True
                continue
            k.pop()
        if it == ')':
            if not p:
                invalid = True
                continue
            p.pop()
        if it == ']':
            if not b:
                invalid = True
                continue
            b.pop()
    print("YES" if not p and not b and not k and not invalid else "NO")


if __name__ == "__main__":
    main()
