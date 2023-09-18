import os
palavra_forca = input("Bem vindo. Digite a palavra misteriosa:").upper()

letras_acertadas = ""
while True:
    palavra_formada = ""
    letra = input("Digite uma letra:").upper()

    while len(letra) > 1:
        print("Erro!!! Letra digitada invalida!")
        letra = input("Digite uma letra:").upper()

    if letra in palavra_forca:
        letras_acertadas += letra
    
    for elemento in palavra_forca:
        if elemento in letras_acertadas:
            palavra_formada += elemento
        else:
            palavra_formada += "*"
    
    if palavra_formada == palavra_forca:
        os.system("cls")
        print(f"Parabens!!!!!\nVocê acertou o desafio\nA palavra misteriosa era:{palavra_forca} ")
        palavra_forca = input("Digite uma nova palavra misteriosa:").upper()
        os.system("cls")
        letras_acertadas = ""
        continue
    else:
        print(palavra_formada)
