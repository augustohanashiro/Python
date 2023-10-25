frase = "       M   ais um dia,            a caminho de ser um programador em python"
frase_separada = frase.split(", ")

# Este metodo imprime os elementos da lista, sem espaços
for indice, conteudo in enumerate(frase_separada):
    print(conteudo.strip())



# for indice, conteudo in enumerate(frase_separada):
#     frase_separada[indice] = frase_separada[indice].strip()

# print(frase_separada)

'''
Metodos aprendidos

split() - Método de uma string  = separa as palavras de uma string atraves de um caractere
strip() - remove os caracteres em branco
join()  - Junta strings
"caractere entre strings".join(iteravel)
'''
