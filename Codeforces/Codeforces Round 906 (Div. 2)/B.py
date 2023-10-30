def can_be_good(string1, string2, length1, length2):
    is_string1_alternate, is_string2_alternate = 1, 1

    for i in range(1, length1):
        if string1[i] == string1[i - 1]:
            is_string1_alternate = 0
            break

    for i in range(1, length2):
        if string2[i] == string2[i - 1]:
            is_string2_alternate = 0
            break

    if is_string1_alternate:
        return "YES"

    if is_string1_alternate == 0 and is_string2_alternate == 0:
        return "NO"

    has_consecutive_zero = '00' in string1
    has_consecutive_one = '11' in string1

    if has_consecutive_zero and has_consecutive_one:
        return "NO"

    if has_consecutive_zero and (string2[0] == '1' and string2[-1] == '1'):
        return "YES"
    if has_consecutive_one and (string2[0] == '0' and string2[-1] == '0'):
        return "YES"

    return "NO"

if __name__ == "__main__":
    test_cases = int(input())
    for _ in range(test_cases):
        length1, length2 = map(int, input().split())
        string1 = input()
        string2 = input()
        print(can_be_good(string1, string2, length1, length2))
