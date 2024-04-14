arr  = [1 ,2, 3, -5 , 6, 7, -2]

max_global = 0
current_max = 0
for i in range(len(arr)):
    current_max = max(arr[i], current_max + arr[i])
    max_global = max(current_max, max_global)
print(max_global)