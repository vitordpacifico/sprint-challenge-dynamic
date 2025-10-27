stock = {
    "Almoxarifado A": {
        "luvas": {"current": 120, "ideal": 150},
        "mascaras": {"current": 60, "ideal": 100},
        "alcool": {"current": 80, "ideal": 80}
    },
    "Almoxarifado B": {
        "luvas": {"current": 30, "ideal": 100},
        "mascaras": {"current": 150, "ideal": 100},
        "alcool": {"current": 20, "ideal": 80}
    }
}

custos_unitarios = {
    "luvas": 2,
    "mascaras": 5,
    "alcool": 10
}

ORCAMENTO_TOTAL = 800

memo = {}

def preparar_dados_knapsack(stock_data, custos_data):
    nomes = []
    valores = []
    pesos = []
    deficit_agregado = {}
    for local in stock_data.values():
        for item, dados in local.items():
            diff = dados["ideal"] - dados["current"]
            if diff > 0:
                if item not in deficit_agregado:
                    deficit_agregado[item] = 0
                deficit_agregado[item] += diff

    for item, deficit in deficit_agregado.items():
        if item in custos_data:
            nomes.append(item)
            valores.append(deficit)
            pesos.append(deficit * custos_data[item])

    return nomes, valores, pesos

def knapsack_recursivo(W, pesos, valores, n):
    if n == 0 or W == 0:
        return 0

    if pesos[n-1] > W:
        return knapsack_recursivo(W, pesos, valores, n-1)

    nao_incluir = knapsack_recursivo(W, pesos, valores, n-1)
    
    incluir = valores[n-1] + knapsack_recursivo(W - pesos[n-1], pesos, valores, n-1)

    return max(nao_incluir, incluir)

def knapsack_memo(W, pesos, valores, n):
    key = (n, W)
    if key in memo:
        return memo[key]

    if n == 0 or W == 0:
        return 0

    if pesos[n-1] > W:
        resultado = knapsack_memo(W, pesos, valores, n-1)
    else:
        nao_incluir = knapsack_memo(W, pesos, valores, n-1)
        incluir = valores[n-1] + knapsack_memo(W - pesos[n-1], pesos, valores, n-1)
        resultado = max(nao_incluir, incluir)
    
    memo[key] = resultado
    return resultado

def knapsack_iterativo(W, pesos, valores, n):
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w_atual in range(1, W + 1):
            peso_item = pesos[i-1]
            valor_item = valores[i-1]

            if peso_item <= w_atual:
                dp[i][w_atual] = max(
                    dp[i-1][w_atual],
                    valor_item + dp[i-1][w_atual - peso_item]
                )
            else:
                dp[i][w_atual] = dp[i-1][w_atual]

    valor_maximo = dp[n][W]
    itens_incluidos = []
    
    w_restante = W
    for i in range(n, 0, -1):
        if valor_maximo > dp[i-1][w_restante]:
            itens_incluidos.append(nomes_itens[i-1])
            valor_maximo -= valores[i-1]
            w_restante -= pesos[i-1]

    return dp[n][W], itens_incluidos

if __name__ == "__main__":
    
    nomes_itens, valores, pesos = preparar_dados_knapsack(stock, custos_unitarios)
    n = len(valores)

    print("--- Problema de Otimização de Reposição (Knapsack) ---")
    print(f"Orçamento Total (W): {ORCAMENTO_TOTAL}")
    print("\nInsumos com déficit e seus custos/valores:")
    for i in range(n):
        print(f"  - {nomes_itens[i]}: Valor (Déficit) = {valores[i]}, Peso (Custo) = {pesos[i]}")

    print("\n--- Teste das 3 Versões ---")
    
    valor_max_iterativo, itens = knapsack_iterativo(ORCAMENTO_TOTAL, pesos, valores, n)
    print(f"[Iterativo]   Utilidade Máxima: {valor_max_iterativo}")

    memo.clear()
    valor_max_memo = knapsack_memo(ORCAMENTO_TOTAL, pesos, valores, n)
    print(f"[Memoização]  Utilidade Máxima: {valor_max_memo}")

    valor_max_recursivo = knapsack_recursivo(ORCAMENTO_TOTAL, pesos, valores, n)
    print(f"[Recursivo]   Utilidade Máxima: {valor_max_recursivo}")

    assert valor_max_iterativo == valor_max_memo == valor_max_recursivo
    
    print("\n--- VALIDAÇÃO ---")
    print("Resultados idênticos. As três implementações estão corretas.")
    print("\n--- SOLUÇÃO DO PROBLEMA ---")
    print(f"Para maximizar a reposição com um orçamento de R${ORCAMENTO_TOTAL}:")
    print(f"Itens a repor: {itens}")
    print(f"Utilidade (unidades repostas): {valor_max_iterativo}")