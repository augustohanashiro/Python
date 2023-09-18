'''
Como saber qual a letra que mais apareceu em uma frase
'''

frase = ("O python é uma linguagem de programação multiparadigma"\
         "Python foi criado por guido van rossum ")

contador  = 0
letra_mais_apareceu = ""
letra_mais_apareceu_n_vezes = 0

while contador < len(frase):
    if frase[contador] == " ":
        contador +=1
        continue
    
    letra_percorrida_caractere = frase[contador]
    letra_percorrida_numero_vezes = frase.count(frase[contador])

    if (letra_percorrida_numero_vezes > letra_mais_apareceu_n_vezes):
        letra_mais_apareceu_n_vezes = letra_percorrida_numero_vezes
        letra_mais_apareceu = letra_percorrida_caractere

    contador +=1

print(f"'{letra_mais_apareceu}' é a letra que mais apareceu na frase, com um total de {letra_mais_apareceu_n_vezes}")