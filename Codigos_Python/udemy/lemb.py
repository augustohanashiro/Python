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

nome = input("Digite o seu nome: ")
idade = input("Digite a sua idade: ")
espaco = " " in nome
nespaco = nome.count(" ")
if nome and idade:
    print(f"Seu nome é {nome}")
    print(f"Seu nome invertido é {nome[::-1]}")
    print(f"Seu nome possui espaços? {espaco}")
    print(f"Seu nome possui {len(nome)} caracteres ao total\n E tirando os espaços {len(nome) - nespaco}")
    print(f"Seu nome começa com {nome[0]} e termina com {nome[-1]}")

