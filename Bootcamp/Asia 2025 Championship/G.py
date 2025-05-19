t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    s1 = input()
    s2 = input()
    f = []
    current_block = 0
    for it in s1:
        current_block += it == '1'
        if it == '0':
            current_block = 0
        f.append(current_block)
    s = []
    current_block = 0
    for it in s2:
        current_block += it == '1'
        if it == '0':
            current_block = 0
        s.append(current_block)
    prefix_s = []
    for i in range(len(s)):
        if i + 1 < len(s):
            if s[i + 1] == 0 and s[i] != 0:
                prefix_s.append(s[i])
        if i == len(s) - 1:
            prefix_s.append(s[i])
        if s[i -1 ]!=0 and s[i] == 0: continue
        if s[i] == 0: prefix_s.append(s[i])
    prefix_f = []
    for i in range(len(f)):
        if i + 1 < len(f):
            if f[i + 1] == 0 and f[i] != 0:
                prefix_f.append(f[i])
        if i == len(f) - 1:
            prefix_f.append(f[i])
        if f[i - 1] != 0 and f[i] == 0: continue
        if f[i] == 0: prefix_f.append(f[i])

    prefix_f = [0] * (n + 1)
    current_block = 0
    i = 0
    for it in s1:
        if it == '0':i+=1
        else: prefix_f[i] += 1
    prefix_f = prefix_f[:i + 1]
    prefix_s = [0] * (m + 1)
    i = 0
    for it in s2:
        if it == '0':
            i += 1
        else:
            prefix_s[i] += 1
    prefix_s = prefix_s[:i + 1]
    #print( prefix_s, prefix_f)
    if len(prefix_s) == 0  and len(prefix_f) > 0:
        print("no")
        continue
    if len(prefix_s) > len(prefix_f):
        print("no")
        continue
    if prefix_s[0] > prefix_f[0] or prefix_s[-1] > prefix_f[-1]:
        print("no")
        continue
    i = 0
    j = 0
    no_ans = False
    while j < len(prefix_s):
        while i < len(prefix_f) and prefix_f[i] < prefix_s[j]:
            i += 1
        if i == len(prefix_f):
            no_ans = True
            break
        j += 1
        i += 1
    print("yes" if not no_ans else "no")