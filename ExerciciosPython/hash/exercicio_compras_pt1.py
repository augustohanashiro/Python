# # Exercícios de fixação PT - 1

# A seguir, você encontrará alguns exercícios para fixar os conceitos aprendidos no curso até agora. Os exercícios estão divididos por exemplos práticos da vida real:
# 
# - lista de compras
# - previsão de vendas
# - relatório de vendas
# - segmentação de clientes
# - analisador de texto
# 
# Para cada assunto, você encontrará ao menos um exercício. Nos casos onde há mais de um exercício para o mesmo assunto, você será convidado a resolver o mesmo problema de formas diferentes. Isso é proposital, pois o objetivo é que você pratique o que aprendeu e, ao mesmo tempo, aprenda novas formas de resolver um mesmo problema. Por exemplo, usando diferentes estruturas de dados, ou diferentes formas de iterar sobre uma estrutura de dados, ou, ainda, utilizando funções.
# 
# Tente resolver os exercícios sozinho. Se tiver dificuldades, consulte o material do curso e, se ainda assim não conseguir resolver, consulte a solução.

# ## Lista de compras

# ### Primeira versão da lista de compras

# Escreva um programa que permita que um usuário crie uma lista de compras.
# O usuário deve ser capaz de adicionar itens, remover itens e visualizar a lista.
# 
# Estruture seu programa da seguinte forma:
# 
# 1. Crie uma lista vazia para armazenar os itens da lista de compras.
# 2. Crie um loop infinito que imprima um menu de opções ao usuário e permita que ele escolha uma opção.
# 3. Dentro do loop, use uma declaração if para executar a tarefa apropriada de acordo com a escolha do usuário.
# 4. Se o usuário escolher adicionar um item, solicite que ele digite o nome do item e adicione-o à lista.
# 5. Se o usuário escolher remover um item, solicite que ele digite o nome do item e remova-o da lista.
# 6. Se o usuário escolher ver a lista, mostre cada item da lista em sua própria linha.
# 7. Se o usuário escolher sair, encerre o loop usando break.
# 
# Exemplo de saída:
# 
# ```
# 1 Adicionar item
# 2 Remover item
# 3 Ver lista
# 4 Sair
# Escolha uma opção: 1
# Digite um item: banana
# 
# 1 Adicionar item
# 2 Remover item
# 3 Ver lista
# 4 Sair
# Escolha uma opção: 1
# Digite um item: maçã
# 
# 1 Adicionar item
# 2 Remover item
# 3 Ver lista
# 4 Sair
# Escolha uma opção: 3
# ['banana', 'maçã']
# 
# 1 Adicionar item
# 2 Remover item
# 3 Ver lista
# 4 Sair
# Escolha uma opção: 2
# Digite um item: banana
# 
# 1 Adicionar item
# 2 Remover item
# 3 Ver lista
# 4 Sair
# Escolha uma opção: 3
# ['maçã']
# 
# 1 Adicionar item
# 2 Remover item
# 3 Ver lista
# 4 Sair
# Escolha uma opção: 4
# ```
# 
import time
import os
lista_compra = []
menu = {
    "1":"Adcionar item",
    "2":"Remover item",
    "3":"Ver lista",
    "4":"Sair",
}

while True:
    os.system("cls")
    print("\n","Menu".center(20,"-"),"\n")
    for elemento in menu:
        print(elemento, "-", menu[elemento])
        
    opcao = input("O que deseja fazer? ")

    if opcao == "1":
        item = input("Digite o nome do item que deseja adcionar a sua lista:").upper()
        if item:
            lista_compra.append(item)
            print("Item adcionado com sucesso")
        else:
            print("Item inválido")
    
    elif opcao == "2":
        item = input("Digite o nome do item que deseja excluir:").upper()
        try:
            lista_compra.remove(item)
            print("Item removido")
        except ValueError:
            print("Item não encontrado")

    elif opcao == "3":
        if len(lista_compra) > 0:
            for indice,elemento in enumerate(lista_compra):
                print("{}-{}".format(indice+1,elemento))
            input("Para voltar ao menu, digite enter!")
            print("Voltando...")
        else:
            print("Lista Vazia")

    elif opcao == "4":
        print("Obrigado")
        break
    
    else:
        print("Opção invalida")
    time.sleep(1.5)