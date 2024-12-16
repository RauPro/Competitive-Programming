from math import gcd
from sys import stdin, stdout


def main():
    input = stdin.read
    data = input().split()

    index = 0
    N = int(data[index])
    Q = int(data[index + 1])
    index += 2

    # Initial salaries and happiness
    salaries = list(map(int, data[index:index + N]))
    index += N
    happiness = [0] * N

    output = []

    for _ in range(Q):
        event_type = int(data[index])
        l = int(data[index + 1]) - 1  # Convert to 0-based index
        r = int(data[index + 2]) - 1
        if event_type == 0:
            # Type 0: Set salaries from l to r to c
            c = int(data[index + 3])
            for i in range(l, r + 1):
                if salaries[i] < c:
                    happiness[i] += 1  # Salary increased
                elif salaries[i] > c:
                    happiness[i] -= 1  # Salary decreased
                salaries[i] = c
            index += 4
        elif event_type == 1:
            # Type 1: Change salaries from l to r by c
            c = int(data[index + 3])
            for i in range(l, r + 1):
                if c > 0:
                    happiness[i] += 1  # Salary will increase
                elif c < 0:
                    happiness[i] -= 1  # Salary will decrease
                salaries[i] += c
            index += 4
        elif event_type == 2:
            # Type 2: Calculate average salary from l to r
            total_salary = sum(salaries[l:r + 1])
            count = r - l + 1
            P = total_salary
            Q = count
            d = gcd(P, Q)
            output.append(f"{P // d}/{Q // d}")
            index += 3
        elif event_type == 3:
            # Type 3: Calculate average happiness from l to r
            total_happiness = sum(happiness[l:r + 1])
            count = r - l + 1
            P = total_happiness
            Q = count
            d = gcd(P, Q)
            output.append(f"{P // d}/{Q // d}")
            index += 3

    # Output all results
    stdout.write("\n".join(output) + "\n")


if __name__ == "__main__":
    main()