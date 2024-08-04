from math import factorial
from functools import lru_cache
mod = int(1e9 + 7)

def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n - 1)



@lru_cache(maxsize=None)
def f(i, r, g, b):
    if r < 0 or g < 0 or b < 0:
        return 0
    if i == 0:
        return 1
    ans = 0
    # 1 color
    ans += f(i - 1, r - i, g, b) + f(i - 1, r, g - i, b) + f(i - 1, r, g, b - i)
    # 2 colors
    if i % 2 == 0:
        ans += (fact(i) // fact(i // 2) // fact(i // 2)) * (
            f(i - 1, r - i // 2, g - i // 2, b) +
            f(i - 1, r - i // 2, g, b - i // 2) +
            f(i - 1, r, g - i // 2, b - i // 2)
        )
    # 3 colors
    if i % 3 == 0:
        ans += (fact(i) // fact(i // 3) // fact(i // 3) // fact(i // 3)) * (
            f(i - 1, r - i // 3, g - i // 3, b - i // 3)
        )
    return ans

def solve():
    n,r,g,b = map(int, input().split())
    print(f(n, r, g, b) % mod)

if __name__ == "__main__":
    solve()
