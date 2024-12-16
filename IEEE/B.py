def main():
    import sys
    import math

    from math import comb

    N, M = map(int, sys.stdin.readline().split())
    half = (N -1 ) //2
    comb_val = comb(N-1, half)
    pow_val = pow(2, half, M)
    result = (comb_val * pow_val) % M
    print(result)

if __name__ == "__main__":
    main()