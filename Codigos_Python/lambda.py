# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.
# lista = [
#     {'nome': 'Luiz', 'sobrenome': 'miranda'},
#     {'nome': 'Maria', 'sobrenome': 'Oliveira'},
#     {'nome': 'Daniel', 'sobrenome': 'Silva'},
#     {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
#     {'nome': 'Aline', 'sobrenome': 'Souza'},
# ]
# lista = [4, 32, 1, 34, 5, 6, 6, 21, ]
# lista.sort(reverse=True)
# sorted(lista)
lista = [
    {'nome': 'Luiz', 'sobrenome': 'Miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

lista.sort(key = lambda item : item["nome"])

for elemento in lista:
    print(elemento)


'''
Explicação por cima da expressão lambda
# função lambda - em sua forma desenvolvida ela faria isso :
def func_lambda(b):
    return b*b

a = func_lambda(b)
    
# função lambda em sua forma resumida 
a   =   lambda         b:    b*b
var = função oculta  param     retorno


print(func_lambda(5))
print(a(5))
'''


# Para ordenarmos uma lista de dicionarios, precisamos informar ao sort qual sera nosso item de 
# ordenação

# esta é so uma função para evitar escrever o for sempre que deseja exibir uma lista 
def exibir(lista):
    for elemento in lista:
        print(elemento)
    print("")

# # Retorna uma cópia raza (apenas itens imutaveis) ordenada da sua lista
copia_lista = sorted(lista,key = lambda item :item["sobrenome"])

exibir(copia_lista)


# # ordena a propria lista segundo a chave que vc passar 
lista.sort(key=lambda item: item["nome"],reverse=True)

for elemento in lista:
    print(elemento)
    


