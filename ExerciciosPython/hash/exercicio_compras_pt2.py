# ### Segunda versão da lista de compras


# Mude o programa de lista de compras para usar um dicionário ao invés de uma lista.
# O programa deve ter as mesmas funcionalidades, mas agora deve ser possível
# adicionar mais de uma unidade de um item na lista de compras. Ou seja, o dicionário
# deve armazenar o nome do item e a quantidade desejada pelo usuário. Por exemplo,
# se o usuário digitar "banana" e "2", o dicionário deve armazenar "banana" como chave
# e 2 como valor. A estrutura do dicionário ficaria assim: `{"banana": 2}`.
# 
# O programa deve permitir que o usuário adicione, remova e visualize o dicionário de compras.
# 
# Além disso, o programa deve mostrar uma mensagem de erro se o usuário tentar
# usar uma opção inválida do menu. Por exemplo, se o usuário digitar 5, o programa
# deve mostrar a mensagem "Opção inválida. Por favor, escolha uma opção válida." e
# mostrar o menu novamente. Além disso, o programa deve ser *case insensitive*, ou seja,
# "Maçã" e "maçã" devem ser considerados o mesmo item.
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
# Digite a quantidade: 2
# 
# 1 Adicionar item
# 2 Remover item
# 3 Ver lista
# 4 Sair
# Escolha uma opção: 1
# Digite um item: maçã
# Digite a quantidade: 3
# 
# 1 Adicionar item
# 2 Remover item
# 3 Ver lista
# 4 Sair
# Escolha uma opção: 3
# {'banana': 2, 'maçã': 3}
# 
# 1 Adicionar item
# 2 Remover item
# 3 Ver lista
# 4 Sair
# Escolha uma opção: 2
# Digite um item: banana
# Digite a quantidade: 1
# 
# 1 Adicionar item
# 2 Remover item
# 3 Ver lista
# 4 Sair
# Escolha uma opção: 3
# {'banana': 1, 'maçã': 3}
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
lista_compra = {}
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
        quantidade = int(input("Digite a quantidade desejada:"))
        if item and quantidade:
            lista_compra[f"{item}"] = quantidade
        else:
            print("Item inválido")
    
    elif opcao == "2":
        item = input("Digite o nome do item que deseja excluir:").upper()
        try:
            del lista_compra[f"{item}"]
            print("Item removido")
        except KeyError:
            print("Item não encontrado")

    elif opcao == "3":
        if len(lista_compra) > 0:
            for item in lista_compra.items():
                print("{}".format(item))
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