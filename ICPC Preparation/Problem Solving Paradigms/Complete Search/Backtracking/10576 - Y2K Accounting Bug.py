from typing import List


def isValid(months_values: List[int], current_month: int) -> bool:
    return sum(months_values[current_month - 5: current_month]) < 0


def backtracking(months_values, surplus, deficit, answer, current_month=0, current_sum=0):
    if current_month >= 5:
        if not isValid(months_values, current_month):
            return

    if current_month == len(months_values):
        answer[0] = max(answer[0], current_sum)
        return

    if answer[0] == float("-inf"):
        months_values[current_month] = surplus
        backtracking(months_values, surplus, deficit, answer, current_month + 1, current_sum + surplus)
        months_values[current_month] = -deficit
        backtracking(months_values, surplus, deficit, answer, current_month + 1, current_sum - deficit)


def main():
    months_values = [0] * 12
    while True:
        try:
            surplus, deficit = map(int, input().split())
        except EOFError:
            break
        answer = [float("-inf")]
        backtracking(months_values, surplus, deficit, answer)
        if answer[0] < 0:
            print("Deficit")
        else:
            print(answer[0])


if __name__ == "__main__":
    main()
