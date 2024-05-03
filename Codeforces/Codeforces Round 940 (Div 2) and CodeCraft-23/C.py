MOD = 10 ** 9 + 7


def count_final_configs(n, k, moves):
    # Inicializar el estado inicial (0 torres, ninguna fila/columna ocupada)
    initial_state = (0, 0, 0, 0)
    dp = {initial_state: 1}  # Diccionario para almacenar los estados válidos

    for r, c in moves:
        new_dp = {}
        for state, count in dp.items():
            white_count, black_count, row_mask, col_mask = state

            # Colocar una torre blanca
            new_row_mask = row_mask | (1 << r)
            new_col_mask = col_mask | (1 << c)
            if not (new_row_mask & (1 << r)) and not (new_col_mask & (1 << c)):
                new_white_count = white_count + 1
                new_state = (new_white_count, black_count, new_row_mask, new_col_mask)
                new_dp[new_state] = new_dp.get(new_state, 0) + count

            # Colocar una torre negra (si r != c)
            if r != c:
                new_row_mask = col_mask | (1 << c)
                new_col_mask = row_mask | (1 << r)
                if not (new_row_mask & (1 << c)) and not (new_col_mask & (1 << r)):
                    new_black_count = black_count + 1
                    new_state = (white_count, new_black_count, new_row_mask, new_col_mask)
                    new_dp[new_state] = new_dp.get(new_state, 0) + count

            # Mantener el estado actual
            new_dp[state] = new_dp.get(state, 0) + count

        dp = new_dp

    total_configs = sum(dp.values()) % MOD
    return total_configs


# Función principal
def main():
    t = int(input())  # Número de casos de prueba
    for _ in range(t):
        n, k = map(int, input().split())
        moves = [tuple(map(int, input().split())) for _ in range(k)]
        result = count_final_configs(n, k, moves)
        print(result)


if __name__ == "__main__":
    main()