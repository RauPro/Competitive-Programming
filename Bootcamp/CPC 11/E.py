def merge_and_count(arr, temp_arr, left, mid, right):
   i = left
   j = mid + 1
   k = left
   inv_count = 0
   while i <= mid and j <= right:
       if arr[i] <= arr[j]:
           temp_arr[k] = arr[i]
           i += 1
       else:
           temp_arr[k] = arr[j]
           inv_count += (mid - i + 1)
           j += 1
       k += 1
   while i <= mid:
       temp_arr[k] = arr[i]
       i += 1
       k += 1

   while j <= right:
       temp_arr[k] = arr[j]
       j += 1
       k += 1

   for i in range(left, right + 1):
       arr[i] = temp_arr[i]

   return inv_count


def merge_sort_and_count(arr, temp_arr, left, right):
   inv_count = 0
   if left < right:
       mid = (left + right) // 2

       inv_count += merge_sort_and_count(arr, temp_arr, left, mid)
       inv_count += merge_sort_and_count(arr, temp_arr, mid + 1, right)
       inv_count += merge_and_count(arr, temp_arr, left, mid, right)


   return inv_count



def count_inversions(arr):
   cop = arr.copy()
   temp_arr = [0] * len(arr)
   return merge_sort_and_count(cop, temp_arr, 0, len(cop) - 1)


t = int(input())
for i in range(t):
    n = int(input())
    list_a = list(input().split())
    list_b = list(input().split())
    index = {}
    ans = [0] * n
    for i, it in enumerate(list_a):
        index[it] = i + 1
    for i, it in enumerate(list_b):
        ans[i] = index[it]
    print(count_inversions(ans))