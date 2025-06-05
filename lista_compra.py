#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  5 14:47:37 2025

@author: anaalmeida
"""

# Lista de Compras
lista = []

def salvar_lista():
    with open("lista_compras.txt", "w") as arquivo:
        for item in lista:
            arquivo.write(f"{item['nome']},{item['quantidade']}\n")

def carregar_lista():
    global lista
    try:
        with open("lista_compras.txt", "r") as arquivo:
            lista = [{"nome": linha.split(",")[0], "quantidade": int(linha.split(",")[1])} 
                     for linha in arquivo if linha.strip()]
    except FileNotFoundError:
        lista = []

def adicionar_item():
    nome = input("Digite o nome do item: ")
    quantidade = int(input("Digite a quantidade: "))
    lista.append({"nome": nome, "quantidade": quantidade})
    salvar_lista()
    print(f"{quantidade} {nome}(s) adicionado(s)!")

def remover_item():
    nome = input("Digite o nome do item a remover: ")
    for item in lista:
        if item["nome"].lower() == nome.lower():
            lista.remove(item)
            salvar_lista()
            print(f"{nome} removido!")
            return
    print("Item não encontrado.")

def visualizar_lista():
    if not lista:
        print("Lista vazia!")
    else:
        print("\nLista de Compras:")
        for item in lista:
            print(f"- {item['quantidade']} {item['nome']}(s)")

# Carregar lista existente
carregar_lista()

while True:
    print("\n1. Adicionar item")
    print("2. Remover item")
    print("3. Visualizar lista")
    print("4. Sair")
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        adicionar_item()
    elif opcao == "2":
        remover_item()
    elif opcao == "3":
        visualizar_lista()
    elif opcao == "4":
        break
    else:
        print("Opção inválida!")