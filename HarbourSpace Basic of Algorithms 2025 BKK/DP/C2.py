import sys
from functools import lru_cache
input = lambda: sys.stdin.readline().rstrip("\r\n")
flush = lambda: sys.stdout.flush()
print = lambda *args, **kwargs: sys.stdout.write(' '.join(map(str, args)) + kwargs.get("end", "\n")) and flush()
def ints(): return map(int, input().split())
def strs(): return input().split()
def chars(): return list(input().strip())
def mat(n): return [list(ints()) for _ in range(n)]
def main():
    n = int(input())
    prices = list(ints())
    no_stock, has_stock = 0, -prices[0]
    for price in prices[1:]:
        no_stock, has_stock = max(no_stock, has_stock + price), max(has_stock, no_stock - price)
    print(no_stock)

if __name__ == "__main__":
    main()