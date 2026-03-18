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
    n, m = ints()
    a = list(ints())
    @lru_cache(None)
    def can_win(current_marbles):
        if current_marbles == 0: return False
        for move_val in a:
            if current_marbles >= move_val:
                if not can_win(current_marbles - move_val): return True
        return False
    print("First" if can_win(n) else "Second")
if __name__ == "__main__":
    main()