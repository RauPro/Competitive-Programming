from collections import defaultdict

input = __import__('sys').stdin.readline

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        friend1 = list(map(int, input().split()))
        friend2 = list(map(int, input().split()))
        friend3 = list(map(int, input().split()))
        friend1, friend2, friend3 = set(friend1[1:]), set(friend2[1:]), set(friend3[1:])
        #print(friend1, friend2, friend3)
        mapper = defaultdict(lambda : [])
        for problem in friend1:
            if  problem not in friend2 and problem not in friend3:
                mapper[1].append(problem)
        for problem in friend2:
            if  problem not in friend1 and problem not in friend3:
                mapper[2].append(problem)
        for problem in friend3:
            if  problem not in friend2 and problem not in friend1:
                mapper[3].append(problem)

        mapper[1] = sorted(mapper[1])
        mapper[2] = sorted(mapper[2])
        mapper[3] = sorted(mapper[3])
        print("Case #{}:".format(_ + 1))
        if len(mapper[1]) >= len(mapper[2]) and len(mapper[1]) >= len(mapper[3]):
            print(1, len(mapper[1]), *mapper[1])
        if len(mapper[2]) >= len(mapper[1]) and len(mapper[2]) >= len(mapper[3]):
            print(2, len(mapper[2]), *mapper[2])
        if len(mapper[3]) >= len(mapper[1]) and len(mapper[3]) >= len(mapper[2]):
            print(3, len(mapper[3]), *mapper[3])