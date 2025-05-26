import sys, bisect

input = lambda: sys.stdin.readline().rstrip("\r\n")
flush = lambda: sys.stdout.flush()
print = lambda *args, **kwargs: sys.stdout.write(' '.join(map(str, args)) + kwargs.get("end", "\n")) and flush()
def ints(): return map(int, input().split())
def strs(): return input().split()
def chars(): return list(input().strip())
def mat(n): return [list(ints()) for _ in range(n)]


def next_greater_elements(arr):
    result = [-1] * len(arr)
    stack = []
    index = [0] * len(arr)
    for i, num in enumerate(arr):
        while stack and arr[stack[-1]] < num:
            val = stack.pop()
            result[val] = num
            index[val] = i
        stack.append(i)
    return index


def main():
    n = int(input())
    a = list(ints())
    index = next_greater_elements(a)
    print(*[a[i] if i != 0 else -1 for i in index])


if __name__ == "__main__":
    main()
