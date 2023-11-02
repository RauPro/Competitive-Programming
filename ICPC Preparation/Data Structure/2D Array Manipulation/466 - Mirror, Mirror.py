import sys
input = sys.stdin.readline

def rotate_matrix_90(matrix):
    n = len(matrix)
    new_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            new_matrix[i][j], new_matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        new_matrix[i].reverse()

    return new_matrix


def rotate_matrix_180(matrix):
    n = len(matrix)
    new_matrix = []
    for i in range(n - 1, -1, -1):
        reversed_m = list(reversed(matrix[i]))
        new_matrix.append(reversed_m)

    return new_matrix


def rotate_matrix_270(matrix):
    n = len(matrix)
    new_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            new_matrix[i][j], new_matrix[j][i] = matrix[j][i], matrix[i][j]

    new_matrix.reverse()
    return new_matrix


def make_vertical(matrix):
    n = len(matrix)
    new_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        new_matrix[i] = matrix[i]
    new_matrix.reverse()
    return new_matrix


if __name__ == "__main__":
    case = 1
    while True:
        n = input()
        if not n: break
        n = int(n)
        matrix = []
        transformed = []
        for i in range(n):
            m_s, m_t = map(str, input().split())
            matrix.append(list(m_s))
            transformed.append(list(m_t))

        matrix_180 = rotate_matrix_180(matrix)
        matrix_90 = rotate_matrix_90(matrix)
        matrix_270 = rotate_matrix_270(matrix)
        vertical = make_vertical(matrix)
        vertical_180 = rotate_matrix_180(vertical)
        vertical_90 = rotate_matrix_90(vertical)
        vertical_270 = rotate_matrix_270(vertical)
        # print(vertical, matrix_180)
        if matrix == transformed:
            print("Pattern", case, "was preserved.")
        elif matrix_90 == transformed:
            print("Pattern", case, "was rotated 90 degrees.")
        elif matrix_180 == transformed:
            print("Pattern", case, "was rotated 180 degrees.")
        elif matrix_270 == transformed:
            print("Pattern", case, "was rotated 270 degrees.")
        elif vertical == transformed:
            print("Pattern", case, "was reflected vertically.")
        elif vertical_90 == transformed:
            print("Pattern", case, "was reflected vertically and rotated 90 degrees.")
        elif vertical_180 == transformed:
            print("Pattern", case, "was reflected vertically and rotated 180 degrees.")
        elif vertical_270 == transformed:
            print("Pattern", case, "was reflected vertically and rotated 270 degrees.")
        else:
            print("Pattern", case, "was improperly transformed.")
        case += 1
