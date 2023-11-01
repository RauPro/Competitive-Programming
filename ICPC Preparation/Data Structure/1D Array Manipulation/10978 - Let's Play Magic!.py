input = __import__('sys').stdin.readline
if __name__ == "__main__":
    while True:
        n = int(input())
        if n == 0: break
        cards = []
        position = []
        ans = ["*"] * n
        for _ in range(n):
            identifier, pos = map(str, input().split())
            cards.append(identifier)
            position.append(pos)
        curr = len(position[0])
        num_pos = [len(position[0])]
        for i in range(1, n):
            num_pos.append(len(position[i]))

        pointer = 0
        counter = 1
        element = 0
        for count in num_pos:
            counter = 1
            while True:
                if pointer == n:
                    pointer = 0
                elif ans[pointer] != "*":
                    pointer += 1
                    continue
                elif counter == count:
                    ans[pointer] = cards[element]
                    element += 1
                    break
                else:
                    pointer += 1
                    counter += 1
        print(" ".join(ans))
