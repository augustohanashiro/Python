# """
# Exercício
# Peça ao usuário para digitar seu nome
# Peça ao usuário para digitar sua idade
# Se nome e idade forem digitados:
#     Exiba:
#         Seu nome é {nome}
#         Seu nome invertido é {nome invertido}
#         Seu nome contém (ou não) espaços
#         Seu nome tem {n} letras
#         A primeira letra do seu nome é {letra}
#         A última letra do seu nome é {letra}
# Se nada for digitado em nome ou idade: 
#     exiba "Desculpe, você deixou campos vazios."
# """

nome = input("Digite seu Nome:")
idade = input("Digite sua idade:")

# Lembrete -  toda string vazia é lida como false
if  nome or idade:
    print(f"\nSeu nome é: {nome}")
    print(f"Seu nome invertido é: {nome[::-1]}")

    if " " in nome:
        espaco = nome.count(" ")
        print(f"Seu nome contém {espaco} espaços")
    else:
        print(f"Seu nome não contém espaços")
        
    print(f"Seu nome contém {len(nome) - espaco} letras")
    print(f"A primeira letra do seu nome é {nome[0]}")
    print(f"A última letra do seu nome é {nome[-1]}")
else:
    print("Voce esqueceu de prencher um campo")


    

    