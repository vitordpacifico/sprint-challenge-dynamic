# 📦 Sistema de Controle de Estoque – Challenge DASA (Sprint 3)

Projeto desenvolvido para a disciplina **Dynamic Programming**, no **Challenge 2025 (2º Semestre)** da FIAP.  

Nosso sistema simula o controle de insumos (reagentes e descartáveis) em almoxarifados de unidades de diagnóstico, aplicando **estruturas de dados clássicas** e técnicas de **programação dinâmica** para otimizar o gerenciamento de estoque.

---

## 👥 Integrantes

- 558488 Anthony Motobe  
- 554743 Guilherme Abe  
- 554779 Gustavo Paulino  
- 558017 Victor Dias  

---

## 🚀 Funcionalidades

- **Visualização de Estoques**: mostra os insumos disponíveis em cada almoxarifado, com quantidade atual, ideal e validade.  
- **Registro de Consumo**: insere movimentações em uma **Fila** (ordem cronológica) e em uma **Pilha** (ordem inversa).  
- **Histórico de Consumos**: permite consultar facilmente o que foi consumido, do mais antigo ao mais recente.  
- **Buscas**:  
  - **Sequencial** → percorre a lista de insumos.  
  - **Binária** → pesquisa eficiente em lista ordenada.  
- **Ordenação de Insumos**:  
  - **Merge Sort**  
  - **Quick Sort**  
- **Redistribuição Automática**: realoca insumos entre almoxarifados para corrigir excessos e faltas.  
- **Memoização (Programação Dinâmica)**: evita cálculos repetidos da diferença entre quantidade atual e ideal (`calculate_diff`).  

---

## 🛠️ Estruturas e Algoritmos Utilizados

- **Fila (Queue)**: registra consumos em ordem cronológica.  
- **Pilha (Stack)**: armazena consumos em ordem inversa.  
- **Busca Sequencial**: procura insumos de forma linear.  
- **Busca Binária**: procura insumos de forma eficiente após ordenação.  
- **Merge Sort**: ordenação estável e eficiente (O(n log n)).  
- **Quick Sort**: ordenação eficiente em média, com divisão recursiva.  
- **Memoização**: otimiza o cálculo de diferenças entre quantidades.  

---

## 📋 Estrutura do Menu

1. Verificar estoques  
2. Registrar consumo (Fila/Pilha)  
3. Mostrar consumos (Fila e Pilha)  
4. Testar buscas (Sequencial/Binária)  
5. Testar ordenações (Merge/Quick Sort)  
6. Redistribuir estoques  
7. Sair  