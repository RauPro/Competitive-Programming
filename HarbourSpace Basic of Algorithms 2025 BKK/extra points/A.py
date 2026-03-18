def lcs(s1, s2):
    len_s1 = len(s1)
    separator = chr(1)
    combined_text = s1 + separator + s2
    n_combined = len(combined_text)
    sa = list(range(n_combined))
    rank = [ord(combined_text[i]) for i in range(n_combined)]

    k_sa = 1
    while k_sa < n_combined:
        sa.sort(key=lambda i: (rank[i], rank[i + k_sa] if i + k_sa < n_combined else -1))

        new_rank = [0] * n_combined
        new_rank[sa[0]] = 0
        for i in range(1, n_combined):
            s1_idx, s2_idx = sa[i - 1], sa[i]

            pair1_rank1 = rank[s1_idx]
            pair1_rank2 = rank[s1_idx + k_sa] if s1_idx + k_sa < n_combined else -1

            pair2_rank1 = rank[s2_idx]
            pair2_rank2 = rank[s2_idx + k_sa] if s2_idx + k_sa < n_combined else -1

            if pair1_rank1 == pair2_rank1 and pair1_rank2 == pair2_rank2:
                new_rank[s2_idx] = new_rank[s1_idx]
            else:
                new_rank[s2_idx] = new_rank[s1_idx] + 1

        rank = new_rank
        if rank[sa[n_combined - 1]] == n_combined - 1:
            break
        k_sa *= 2
    lcp = [0] * n_combined
    k_lcp = 0
    rank_inv = [0] * n_combined
    for i in range(n_combined):
        rank_inv[sa[i]] = i

    for i in range(n_combined):
        if rank_inv[i] == n_combined - 1:
            k_lcp = 0
            continue
        j = sa[rank_inv[i] + 1]

        while i + k_lcp < n_combined and \
                j + k_lcp < n_combined and \
                combined_text[i + k_lcp] == combined_text[j + k_lcp]:
            k_lcp += 1

        lcp[rank_inv[i] + 1] = k_lcp
        if k_lcp > 0:
            k_lcp -= 1

    max_lcs_len = 0
    lcs_start_index_in_combined = -1

    for i in range(1, n_combined):
        suffix1_start_orig_idx = sa[i - 1]
        suffix2_start_orig_idx = sa[i]
        is_s1_suffix1 = (suffix1_start_orig_idx < len_s1)
        is_s2_suffix1 = (suffix1_start_orig_idx > len_s1)

        is_s1_suffix2 = (suffix2_start_orig_idx < len_s1)
        is_s2_suffix2 = (suffix2_start_orig_idx > len_s1)

        if (is_s1_suffix1 and is_s2_suffix2) or \
                (is_s2_suffix1 and is_s1_suffix2):
            if lcp[i] > max_lcs_len:
                max_lcs_len = lcp[i]
                lcs_start_index_in_combined = sa[i - 1]
    if max_lcs_len > 0:
        return combined_text[lcs_start_index_in_combined: lcs_start_index_in_combined + max_lcs_len]
    else:
        return ""


print(lcs(input(), input()))