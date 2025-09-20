stock = {
    "Almoxarifado A": {
        "luvas": {"current": 120, "ideal": 150, "validade": 30},
        "máscaras": {"current": 60, "ideal": 100, "validade": 15},
        "álcool": {"current": 80, "ideal": 80, "validade": 10}
    },
    "Almoxarifado B": {
        "luvas": {"current": 30, "ideal": 100, "validade": 25},
        "máscaras": {"current": 150, "ideal": 100, "validade": 40},
        "álcool": {"current": 20, "ideal": 80, "validade": 5}
    }
}

memory_diff = {}

def deepcopy_dict(d):
    """Faz cópia profunda de dicionários aninhados (sem usar import copy)."""
    if isinstance(d, dict):
        return {k: deepcopy_dict(v) for k, v in d.items()}
    elif isinstance(d, list):
        return [deepcopy_dict(v) for v in d]
    else:
        return d

def calculate_diff(current, ideal):
    key = (current, ideal)
    if key in memory_diff:
        return memory_diff[key]
    result = ideal - current
    memory_diff[key] = result
    return result

class Fila:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        return f"Fila: {self.items}"


class Pilha:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        return f"Pilha: {self.items}"

fila_consumo = Fila()
pilha_consumo = Pilha()

def registrar_consumo(item, quantidade):
    fila_consumo.enqueue((item, quantidade))
    pilha_consumo.push((item, quantidade))
    print(f"Consumo registrado: {item} - {quantidade} unidades.")

def mostrar_consumos():
    print("\n--- Histórico em ordem cronológica (Fila) ---")
    print(fila_consumo)
    print("\n--- Histórico em ordem inversa (Pilha) ---")
    print(pilha_consumo)

def busca_sequencial(lista, alvo):
    for i, item in enumerate(lista):
        if item == alvo:
            return i
    return -1

def busca_binaria(lista, alvo):
    lista_ordenada = sorted(lista)
    inicio, fim = 0, len(lista_ordenada) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista_ordenada[meio] == alvo:
            return meio
        elif lista_ordenada[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1

def testar_buscas():
    produtos = list({p for almox in stock.values() for p in almox.keys()})
    print("\nProdutos disponíveis:", produtos)
    alvo = input("Digite o nome do produto para buscar: ").strip().lower()

    seq_idx = busca_sequencial(produtos, alvo)
    bin_idx = busca_binaria(produtos, alvo)

    if seq_idx != -1:
        print(f"Busca Sequencial → '{alvo}' encontrado na posição {seq_idx}.")
    else:
        print(f"Busca Sequencial → '{alvo}' não encontrado.")

    if bin_idx != -1:
        print(f"Busca Binária → '{alvo}' encontrado na posição {bin_idx}.")
    else:
        print(f"Busca Binária → '{alvo}' não encontrado.")

def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio])
    direita = merge_sort(lista[meio:])
    return merge(esquerda, direita)

def merge(esq, dir):
    resultado = []
    i = j = 0
    while i < len(esq) and j < len(dir):
        if esq[i][1] <= dir[j][1]:
            resultado.append(esq[i])
            i += 1
        else:
            resultado.append(dir[j])
            j += 1
    resultado.extend(esq[i:])
    resultado.extend(dir[j:])
    return resultado

def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    pivo = lista[len(lista) // 2]
    menores = [x for x in lista if x[1] < pivo[1]]
    iguais = [x for x in lista if x[1] == pivo[1]]
    maiores = [x for x in lista if x[1] > pivo[1]]
    return quick_sort(menores) + iguais + quick_sort(maiores)

def testar_ordenacoes():
    insumos = []
    for local, itens in stock.items():
        for nome, dados in itens.items():
            insumos.append((nome, dados["current"]))

    print("\nLista original:", insumos)
    print("Merge Sort:", merge_sort(insumos))
    print("Quick Sort:", quick_sort(insumos))

def get_products(stock):
    products = set()
    for location in stock:
        products.update(stock[location].keys())
    return list(products)

def redistribute_items(auto_confirm=True):
    temp_stock = deepcopy_dict(stock)
    redistributions = []
    products = get_products(temp_stock)
    for product in products:
        shortage_locations = []
        surplus_locations = []
        for location in temp_stock:
            if product in temp_stock[location]:
                current = temp_stock[location][product]['current']
                ideal = temp_stock[location][product]['ideal']
                diff = calculate_diff(current, ideal)
                if diff > 0:
                    shortage_locations.append([location, diff])
                elif diff < 0:
                    surplus_locations.append([location, abs(diff)])
        for shortage in shortage_locations:
            for surplus in surplus_locations:
                if surplus[1] == 0:
                    continue
                qtd = min(shortage[1], surplus[1])
                if qtd > 0:
                    redistributions.append((product, surplus[0], shortage[0], qtd))
                    temp_stock[surplus[0]][product]['current'] -= qtd
                    temp_stock[shortage[0]][product]['current'] += qtd
                    surplus[1] -= qtd
                    shortage[1] -= qtd
    if not redistributions:
        print("Nenhuma redistribuição sugerida.")
        return
    for product, from_, to, qty in redistributions:
        stock[from_][product]['current'] -= qty
        stock[to][product]['current'] += qty
        print(f"{qty} unidades de {product} movidas de {from_} para {to}.")
    print("Redistribuição realizada com sucesso!")

def view_inventories():
    print("\n--- Estoques Atuais ---")
    for almox, itens in stock.items():
        print(f"\n{almox}:")
        for nome, dados in itens.items():
            print(f"  {nome} → atual={dados['current']} | ideal={dados['ideal']} | validade={dados['validade']}")

def start():
    while True:
        print("\n===== MENU =====")
        print("1. Verificar estoques")
        print("2. Registrar consumo (Fila/Pilha)")
        print("3. Mostrar consumos (Fila e Pilha)")
        print("4. Testar buscas (Sequencial/Binária)")
        print("5. Testar ordenações (Merge/Quick Sort)")
        print("6. Redistribuir estoques")
        print("7. Sair")

        opcao = input("Escolha: ").strip()
        match opcao:
            case "1":
                view_inventories()
            case "2":
                item = input("Nome do item: ").strip().lower()
                try:
                    qtd = int(input("Quantidade consumida: "))
                except:
                    print("Quantidade inválida.")
                    continue
                registrar_consumo(item, qtd)
            case "3":
                mostrar_consumos()
            case "4":
                testar_buscas()
            case "5":
                testar_ordenacoes()
            case "6":
                redistribute_items()
            case "7":
                print("Saindo... Obrigado por usar o sistema.")
                break
            case _:
                print("Opção inválida.")

if __name__ == "__main__":
    start()