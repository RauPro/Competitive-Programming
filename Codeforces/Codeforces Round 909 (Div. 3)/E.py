def min_operations_to_sort(t, test_cases):
    results = []

    for n, arr in test_cases:
        if sorted(arr) == arr:
            results.append(0)
            continue

        sorted_index = None
        for i in range(n - 1, 0, -1):
            if arr[i] < arr[i - 1]:
                sorted_index = i
                break

        if sorted_index is None:
            results.append(-1)
        else:
            results.append(sorted_index)

    return results

# Ejemplo de uso
t = 5
test_cases = [
    (5, [6, 4, 1, 2, 5]),
    (7, [4, 5, 3, 7, 8, 6, 2]),
    (6, [4, 3, 1, 2, 6, 4]),
    (4, [5, 2, 4, 2]),
    (3, [2, 2, 3])
]

print(min_operations_to_sort(t, test_cases))
