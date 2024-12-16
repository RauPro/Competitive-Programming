def solve():
    import sys
    import threading

    def main():
        import sys
        S = sys.stdin.readline().strip()
        N = len(S)
        ans = [float('inf')] * (N + 1)
        mod = (1 << 61) - 1  # Large prime for modulus
        base = 911  # Base for hashing

        # Precompute prefix hashes and powers of base
        h = [0] * (N + 1)
        pow_base = [1] * (N + 1)

        for i in range(1, N + 1):
            h[i] = (h[i - 1] * base + ord(S[i - 1])) % mod
            pow_base[i] = (pow_base[i - 1] * base) % mod

        for L in range(1, N + 1):
            substrings = dict()

            # Compute hashes for all substrings of length L
            for i in range(N - L + 1):
                j = i + L - 1
                # Compute substring hash using precomputed prefix hashes
                hash_value = (h[j + 1] - h[i] * pow_base[L]) % mod
                if hash_value not in substrings:
                    substrings[hash_value] = []
                substrings[hash_value].append(i)

            # Process each unique substring
            for positions in substrings.values():
                intervals = []
                for pos in positions:
                    l = pos
                    r = pos + L - 1
                    intervals.append((l, r))

                # Merge intervals
                intervals.sort()
                merged = []
                for l, r in intervals:
                    if not merged or merged[-1][1] + 1 < l:
                        merged.append([l, r])
                    else:
                        merged[-1][1] = max(merged[-1][1], r)

                # Calculate total covered islands and connected components
                total_covered = sum(r - l + 1 for l, r in merged)
                num_components = len(merged) + (N - total_covered)
                ans[num_components] = min(ans[num_components], L)

        # Output the results
        print(' '.join(str(0 if val == float('inf') else val) for val in ans[1:N + 1]))
    threading.Thread(target=main).start()
solve()