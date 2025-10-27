# 📦 Sistema de Controle de Estoque – Challenge DASA

**FIAP | Challenge 2025 (2º Semestre)**
**Disciplina:** Dynamic Programming

O projeto **Sistema de Controle de Estoque** foi desenvolvido com o objetivo de simular a gestão de insumos laboratoriais (reagentes e descartáveis) em almoxarifados de unidades de diagnóstico.

O sistema integra conceitos de **estruturas de dados clássicas** e **programação dinâmica**, permitindo tanto o registro eficiente de consumo de materiais quanto a **otimização da reposição de estoque** com base em restrições orçamentárias.

---

## 👥 Integrantes

| RA     | Nome            |
| ------ | --------------- |
| 558488 | Anthony Motobe  |
| 554743 | Guilherme Abe   |
| 554779 | Gustavo Paulino |
| 558017 | Victor Dias     |

---

## 🚀 Visão Geral das Sprints

### **Sprint 3 – Estruturas de Dados Clássicas**

Foco na aplicação prática de **filas, pilhas, buscas e ordenações** para manipular e consultar os insumos.

#### 🔧 Funcionalidades

* **Visualização de Estoques:**
  Exibe os insumos disponíveis em cada almoxarifado, incluindo quantidade atual, quantidade ideal e validade.

* **Registro de Consumo:**
  Insere movimentações em:

  * **Fila (Queue):** ordem cronológica (FIFO)
  * **Pilha (Stack):** ordem inversa (LIFO)

* **Histórico de Consumos:**
  Permite consultar o histórico completo — do mais antigo ao mais recente (FIFO) ou vice-versa (LIFO).

* **Buscas:**

  * **Sequencial:** percorre todos os insumos.
  * **Binária:** busca eficiente em lista previamente ordenada.

* **Ordenações:**

  * **Merge Sort:** algoritmo estável e de complexidade O(n log n).
  * **Quick Sort:** rápido em média, com divisão recursiva.

* **Redistribuição Automática:**
  Reequilibra estoques entre almoxarifados, corrigindo excessos e faltas automaticamente.

* **Memoização Simples:**
  Evita cálculos repetidos da diferença entre quantidade atual e ideal (`calculate_diff`).

---

### **Sprint 4 – Programação Dinâmica**

Foco na **otimização da reposição de estoque** por meio da aplicação do **Problema da Mochila (Knapsack 0/1)**.

#### ⚙️ Funcionalidades

* **Otimização de Reposição (Knapsack 0/1):**
  Determina a combinação ideal de insumos a repor para **maximizar a utilidade total (unidades repostas)** sem exceder o **orçamento máximo (capacidade)**.

* **Modelagem do Problema:**

  * **Peso:** custo do insumo
  * **Valor:** unidades a repor
  * **Capacidade:** orçamento disponível

* **Função de Transição:**
  [
  dp(i, w) = \max(dp(i-1, w), , valor[i] + dp(i-1, w - peso[i]))
  ]

* **Implementações Comparadas:**

  * Recursiva Pura
  * Memoização (Top-Down)
  * Iterativa (Bottom-Up)

* **Recomendação de Compras:**
  A versão iterativa reconstrói as decisões ótimas e indica **quais insumos devem ser comprados** para atingir a melhor reposição possível dentro do orçamento.

---

## 🧠 Estruturas e Algoritmos Utilizados

| Conceito                                | Aplicação                                                           |
| --------------------------------------- | ------------------------------------------------------------------- |
| **Fila (Queue)**                        | Registro de consumo em ordem cronológica (FIFO).                    |
| **Pilha (Stack)**                       | Registro de consumo em ordem inversa (LIFO).                        |
| **Busca Sequencial**                    | Percorre todos os insumos.                                          |
| **Busca Binária**                       | Pesquisa eficiente em lista ordenada.                               |
| **Merge Sort**                          | Ordenação estável (O(n log n)).                                     |
| **Quick Sort**                          | Ordenação eficiente em média (divisão recursiva).                   |
| **Programação Dinâmica (Knapsack 0/1)** | Otimização da reposição de estoque dentro de um orçamento limitado. |

---

## 📋 Estrutura do Menu (Sugerida)

1. Verificar estoques
2. Registrar consumo (Fila/Pilha)
3. Mostrar consumos (Fila e Pilha)
4. Testar buscas (Sequencial/Binária)
5. Testar ordenações (Merge/Quick Sort)
6. Redistribuir estoques
7. Otimizar reposição (DP – Problema da Mochila)
8. Sair

---

## 💡 Conclusão

O **Sistema de Controle de Estoque – Challenge DASA** demonstra como técnicas clássicas de estruturação de dados e **programação dinâmica** podem ser integradas em um projeto realista e funcional.

Mais do que um exercício acadêmico, este sistema representa uma simulação prática de **decisão ótima sob restrições**, aplicando lógica computacional para resolver um problema real de gestão e eficiência logística.  