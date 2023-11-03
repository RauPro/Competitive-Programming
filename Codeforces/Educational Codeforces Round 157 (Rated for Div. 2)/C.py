from collections import defaultdict

def sum_of_digits(string):
    return sum(int(char) for char in string)

def calculate_pairs(n, tickets):
    sums = defaultdict(int)
    for ticket in tickets:
        length = len(ticket)
        for i in range(length + 1):
            first_half = sum_of_digits(ticket[:i])
            second_half = sum_of_digits(ticket[i:])
            sums[(length, first_half, second_half)] += 1
    print(sums)
    count = 0
    sums_keys = list(sums.keys())
    for i in range(len(sums_keys)):
        for j in range(i + 1, len(sums_keys)):
            for k in range(sums[sums_keys[i]] * sums[sums_keys[j]]):
                if sums_keys[i][0] == sums_keys[j][0] and sums_keys[i][1] == sums_keys[j][2] and sums_keys[i][2] == sums_keys[j][1]:
                    count += 1
    print(sums_keys)

    return count

# Leer la cantidad de trozos de boleto
n = int(input().strip())
# Leer los trozos de boleto
tickets = input().strip().split()

# Calcular e imprimir el número de pares de boletos de la suerte
print(calculate_pairs(n, tickets))
