import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")
flush = lambda: sys.stdout.flush()
print = lambda *args, **kwargs: sys.stdout.write(' '.join(map(str, args)) + kwargs.get("end", "\n")) and flush()
def ints(): return map(int, input().split())
def strs(): return input().split()
def chars(): return list(input().strip())
def mat(n): return [list(ints()) for _ in range(n)]

def main():
    s = input()
    n = len(s)
    suffix_a = sorted(range(n), key=lambda i: s[i:])
    prefix_sum = 0
    for a, b in zip(suffix_a[1:], suffix_a[:-1]):
        l = 0
        while a+l < n and b+l < n and s[a+l] == s[b+l]: l += 1
        prefix_sum += l
    print(n * (n + 1) // 2 - prefix_sum)
if __name__ == "__main__":
    main()