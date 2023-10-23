# escrever o nome na vertical

nome = input("Digite seu nome: ")
contador = 0
nova_string = ""

while contador < len(nome):
    print("*",nome[contador],"*")
    letra = nome[contador]
    nova_string += "*" + letra
    contador+=1

nova_string+= "*"
print(nova_string)