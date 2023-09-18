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

palavra_secreta = "Augusto".upper()
letras_acertadas = ""
tentativas = 0
while True:
    palavra_final = ""
    
    letra_chute = input("Digite uma letra:").upper()
    
    while len(letra_chute) > 1:
        letra_chute = input("ERRO!!! Digite apenas uma letra! :").upper()

    tentativas += 1

    if letra_chute in palavra_secreta:
        letras_acertadas += letra_chute

    for letra in palavra_secreta:
        if letra in letras_acertadas:
            palavra_final += letra
        else:
            palavra_final += "*"
    
    if palavra_final != palavra_secreta:
        print(palavra_final)
    else:
        os.system("cls")
        print(f"Parabens!!! Voce adivinhou a palavra chave\nPalavra secreta era: {palavra_secreta}")
        print(f"Voce acertou em {tentativas}")
        letras_acertadas = ""
        tentativas = 0
        palavra_secreta = input("Digite qual a próxima palavra misteriosa:").upper()
        os.system("cls")


