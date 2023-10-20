import os

lista_compra = []
opcao_valida = "I-A-L"

while True:
    comando = input("Selecione uma opção\n[I]nserir, [A]pagar, [L]istar: ").upper()

    while comando not in opcao_valida:
        os.system("cls")
        comando = input("Opção inválida !!! Digite entre [I]nserir, [A]pagar, [L]istar:").upper()
        
    if comando == "I":
        os.system("cls")
        item = input("Digite o nome do item que deseja adicionar:")
        lista_compra.append(item)
    
    if comando == "A":
        os.system("cls")
        item_apagar = int(input("Digite o numero do item que deseja apagar:"))
        while item_apagar > len(lista_compra):
            item_apagar = int(input(f"Item inexistente\nSua lista possui {len(lista_compra)} elementos\nDigite o numero do elemento que deseja exluir:"))
        lista_compra.pop(item_apagar - 1)

    if comando == "L":
        os.system("cls")
        for indice, conteudo in enumerate(lista_compra):
            print(indice+1, conteudo)

    print(f"Sua lista possui: {len(lista_compra)}")
