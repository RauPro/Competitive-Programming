n = int(input())
ans = 0
tables = []
total_zeros = 0
total_ones = 0
flag_zero = False
flag_one = False
zeros_table = []
ones_table = []
for i in range(n):
    s = input()
    zeros, ones = s.count('0'), s.count('1')
    taken_zeros = zeros
    taken_ones = ones
    if zeros > ones:
        total_ones += ones
        flag_zero = True
        taken_zeros = 0
        zeros_table.append(('0' * (len(s) - ones), taken_ones, ones, i))
    else:
        total_zeros += zeros
        flag_one = True
        taken_ones = 0
        ones_table.append(('1' * (len(s) - zeros), taken_zeros, zeros, i))


#print(ones_table)
#print(zeros_table)
ones_table.sort(key=lambda x: (len(x[0]) - x[1]))
zeros_table.sort(key=lambda x: (len(x[0]) - x[1]))
#print(total_ones, total_zeros)
#prior 0
order_zeros = False
if total_zeros > 0:
    if not zeros_table:
        ans += len(ones_table[0][0])
        ans += total_zeros - ones_table[0][1]
        zeros, ones = ones_table[0][2], len(ones_table[0][0])
        order_zeros = True
        if zeros > ones:
            total_ones -= ones
    else:
        ans += total_zeros
if total_ones > 0:
    if not ones_table:
        ans += len(zeros_table[0][0])
        ans += total_ones - (zeros_table[0][1])
    else:
        ans += total_ones

print(ans)