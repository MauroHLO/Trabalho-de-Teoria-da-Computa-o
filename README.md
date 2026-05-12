# Trabalho-de-Teoria-da-Computacao
# Simulador de Máquina de Turing - UFC

Este projeto é uma implementação funcional e visual de uma **Máquina de Turing (MT)**, desenvolvida como parte da disciplina de **Teoria da Computação** na Universidade Federal do Ceará (UFC). O simulador permite a execução de algoritmos através de transições de estados, operando sobre uma fita bidirecional e infinita.

## 🚀 Funcionalidades

- **Motor de Simulação:** Suporte a leitura, escrita e movimento (Esquerda/Direita).
- **Interface Gráfica (GUI):** Visualização em tempo real da fita e do cabeçote utilizando `tkinter`.
- **Entrada Dinâmica:** Liberdade para o usuário testar qualquer sequência binária diretamente pelo console.
- **Algoritmo Padrão:** Implementação do transdutor que adiciona 'Y' no início e 'X' no fim de sequências binárias (conforme o arquivo `fonte.mt`).

## 📂 Estrutura do Projeto

A arquitetura do projeto é modular, facilitando a manutenção e a compreensão acadêmica:

- `main.py`: O ponto de entrada. Gerencia a interação com o usuário e configura os estados da máquina.
- `Machine.py`: O "hardware" da máquina. Gerencia a fita e a lógica de execução.
- `State.py`: Representa os estados e gerencia as transições disponíveis em cada um.
- `Edge.py`: Define o "contrato" de cada transição (Lê, Escreve, Move).
- `Transition.py`: Conecta um estado a uma aresta (Edge).
- `gui_turing.py`: Interface visual que desacelera a execução para fins didáticos.

## 🛠️ Como Executar

1. **Pré-requisitos:**
   - Possuir o Python 3.x instalado.
   - A biblioteca `tkinter` (já inclusa por padrão no Python na maioria dos sistemas).

2. **Passos:**
   - Clone este repositório ou baixe os arquivos.
   - Abra o terminal na pasta do projeto.
   - Execute o comando:
     ```bash
     python main.py
     ```
   - No console, digite a sequência binária desejada (ex: `1101`) ou apenas pressione **Enter** para usar a entrada padrão `101001`.
   - Uma janela abrirá. Clique em **EXECUTAR SIMULAÇÃO** para ver a mágica acontecer!

## 🧠 Conceitos Teóricos

Diferente de um Autômato Finito, esta Máquina de Turing é um **Transdutor Tipo 0** (Hierarquia de Chomsky). Ela demonstra:
1. **Memória de Escrita:** A capacidade de alterar os dados na fita.
2. **Movimento Bidirecional:** O cabeçote pode voltar para processar informações anteriores.
3. **Universalidade:** O motor pode simular qualquer algoritmo, bastando alterar as transições no `main.py`.

---
*Desenvolvido para fins acadêmicos - UFC.*
