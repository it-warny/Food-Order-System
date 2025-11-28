# Rest.PY 🍔

Um simulador simples de sistema de pedidos de restaurante via linha de comando (CLI), focado em estruturas de dados.

> 🚧 **Status:** Em desenvolvimento (Work In Progress)

## 📋 Sobre o Projeto

Este projeto implementa um sistema de gerenciamento de pedidos utilizando **Python**. O objetivo é simular uma fila de pedidos onde o gerente pode adicionar novos itens e marcar pedidos como concluídos.

O diferencial deste projeto é a implementação manual de uma **Lista Encadeada (Linked List)** para gerenciar a fila (`OrdersQueue`), em vez de usar listas padrão do Python.



[Image of singly linked list diagram]


## 🚀 Funcionalidades Atuais

* **Adicionar Pedido:** O usuário digita o nome do pedido e ele entra no final da fila (Enqueue).
* **Completar Pedido:** Remove o primeiro pedido da fila (FIFO - First In, First Out).
* **Listar Pedidos:** Mostra a fila atual sempre que um pedido é completado.
* **Tratamento de Input:** Capitalização automática e remoção de espaços em branco.

## 🛠️ Tecnologias Utilizadas

* Python 3
* Estruturas de Dados (Filas / Linked Lists)
* POO (Programação Orientada a Objetos)

## 💻 Como Rodar

1. Certifique-se de ter o Python instalado.
2. Clone este repositório.
3. Execute o arquivo principal:

```bash
python main.py
