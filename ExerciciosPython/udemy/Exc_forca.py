"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

import os 
letras_adivinhadas = ""
palavra_chave = input("Bem vindo ao jogo da forca programada em python\nDigite uma palavra chave:").upper()
tentativas = 0
while True:
    palavra_adivinhada = ""
    letra = input("Digite uma letra:").upper()
    
    while len(letra) > 1:
        letra = input("Letra invalida !!!\nDigite apenas um caractere:").upper()
    tentativas +=1

    if letra in palavra_chave:
        letras_adivinhadas += letra

    for elemento in palavra_chave:
        if elemento in letras_adivinhadas:
            palavra_adivinhada += elemento
        else:
            palavra_adivinhada += "*"

    if palavra_adivinhada != palavra_chave:
        print(palavra_adivinhada)
    else:
        os.system("cls")
        print("Parabens!!!! Você venceu o jogo\nA palavra misteriosa era:",palavra_chave,"\n\n")
        print(f"Voce acertou em {tentativas} tentativas")
        palavra_chave = input("Digite uma nova palavra misteriosa:").upper()
        os.system('cls')
        letras_adivinhadas = ""
        continue



    