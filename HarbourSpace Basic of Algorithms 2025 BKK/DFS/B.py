import sys
from types import GeneratorType
input = lambda: sys.stdin.readline().rstrip("\r\n")
flush = lambda: sys.stdout.flush()
print = lambda *args, **kwargs: sys.stdout.write(' '.join(map(str, args)) + kwargs.get("end", "\n")) and flush()
def ints(): return map(int, input().split())
def strs(): return input().split()
def chars(): return list(input().strip())
def mat(n): return [list(ints()) for _ in range(n)]
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        to = f(*args, **kwargs)
        while True:
            if type(to) is GeneratorType:
                stack.append(to)
                to = next(to)
            else:
                stack.pop()
                if not stack:
                    break
                to = stack[-1].send(to)
        return to

    return wrappedfunc


sys.setrecursionlimit(1000000000)
def main():
    n, m = ints()
    mx = [list(input()) for i in range(n)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    def floodfill(u, v):
        nonlocal mx
        #print(u, v,mx[u][v] )
        ans = mx[u][v] == '1'
        if mx[u][v] == '0': return 0
        mx[u][v] = '0'
        for x, y in zip(dx, dy):
            #print(x, y)
            if (u + x >= n or y + v >= m) or u + x < 0 or y + v < 0: continue
            ans += floodfill(u + x, v + y)
        return ans
    anns = 0
    for i in range(n):
        for j in range(m):
            if mx[i][j] == '0': continue
            k = floodfill(i, j)
            anns += k != 0
    print(anns)



if __name__ == "__main__":
    main()