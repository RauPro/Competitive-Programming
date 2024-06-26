import random


def generate_test_case():
    # Max values according to constraints
    MAX_T = 10 ** 4
    MAX_N = 10 ** 9
    MAX_KQ = 10 ** 5
    MAX_B = 10 ** 9

    # Generate random number of test cases
    t = 500  # Using smaller t for simplicity in example
    print(t)

    for _ in range(t):
        # Randomly determine n, k, and q within the given constraints
        k = random.randint(1, min(100, MAX_KQ))  # Smaller k for manageability
        n = random.randint(k, min(1000, MAX_N))
        q = random.randint(1, min(100, MAX_KQ))

        # Generate k unique, sorted integers for a_i with a_k being n
        a = sorted(random.sample(range(1, n + 1), k - 1))
        a.append(n)  # Ensure that the last point is n

        # Generate k sorted integers for b_i
        b = sorted(random.randint(1, 1000) for _ in range(k))

        # Output n, k, q
        print(n, k, q)
        print(" ".join(map(str, a)))
        print(" ".join(map(str, b)))

        # Generate q queries
        for _ in range(q):
            d = random.randint(0, n)
            print(d)


# Call the function to generate test cases
generate_test_case()
