import random
import itertools

def generate_test(k_min=2, k_max=10,
                  len_min=0, len_max=20,
                  val_min=-1000, val_max=1000,
                  num_tests=5,
                  ensure_nonempty=False):
    """
    Generates `num_tests` random testcases for the “merge k sorted arrays” problem.
    - k_min, k_max: range for number of arrays (k)
    - len_min, len_max: range for each array’s length
    - val_min, val_max: range for element values
    - ensure_nonempty: if True, guarantees each array has at least 1 element
    """
    for ti in range(1, num_tests+1):
        k = random.randint(k_min, k_max)
        print(f"# Test #{ti}")
        print(k)
        arrays = []
        for _ in range(k):
            # optionally force minimum length of 1 to avoid empty array
            L = random.randint(max(1, len_min) if ensure_nonempty else len_min,
                               len_max)
            arr = sorted(random.randint(val_min, val_max) for __ in range(L))
            arrays.append(arr)
            if L:
                print(" ".join(map(str, arr)))
            else:
                print()  # blank line for an empty array
        # compute expected merged output
        merged = list(itertools.chain.from_iterable(arrays))
        merged.sort()
        print("# Expected output:")
        if merged:
            print(" ".join(map(str, merged)))
        else:
            print()  # nothing
        print()  # blank line between tests

if __name__ == "__main__":
    # Example: generate 10 random tests, total arrays 2..8, lengths up to 15
    generate_test(k_min=2, k_max=8,
                  len_min=0, len_max=15,
                  val_min=-500, val_max=500,
                  num_tests=10,
                  ensure_nonempty=False)
