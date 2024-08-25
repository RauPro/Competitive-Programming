mapper = {}
s = "ogabek marsharpov"
for it in s:
    if it not in mapper:
        mapper[it] = 0
    else:
        mapper[it] += 1

print(mapper)