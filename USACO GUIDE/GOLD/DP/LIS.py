from bisect import *

MAX_N = 11

n = 11
A = [-7, 10, 9, 2, 3, 8, 8, 1, 2, 3, 4]

L = [None] * MAX_N
lis = 0
for i in range(n):
    pos = bisect_left(L, A[i], 0, lis)
    L[pos] = A[i]
    if pos+1 > lis:
        lis = pos+1
    print('Considering element A[{}] = {}'.format(i, A[i]))
    print('LIS ending at A[{}] is of length {}: '.format(i, pos+1), end='')
    print('L is now: [' + ', '.join(map(str, L[:lis])) + ']\n')
print('Final LIS is of length:', L[:lis])