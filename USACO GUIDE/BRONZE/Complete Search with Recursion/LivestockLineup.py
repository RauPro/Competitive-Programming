from itertools import permutations
import sys

def main():
    sys.stdin = open('lineup.in', 'r')
    sys.stdout = open('lineup.out', 'w')
    n = int(input())
    constraints = []
    for _ in range(n):
        words = input().strip().split()
        cow1 = words[0]
        cow2 = words[-1]
        constraints.append((cow1, cow2))
    cows = ["Beatrice", "Belinda", "Bessie", "Betsy", "Blue", "Buttercup", "Sue", "Bella"]
    cows.sort()
    for perm in permutations(cows):
        valid = True
        for cow1, cow2 in constraints:
            idx1 = perm.index(cow1)
            idx2 = perm.index(cow2)
            if abs(idx1 - idx2) != 1:
                valid = False
                break
        if valid:
            for cow in perm:
                print(cow)
            break


if __name__ == "__main__":
    main()