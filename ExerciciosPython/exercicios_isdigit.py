"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

numero = input("Digite um numero inteiro: ")

if numero.isdigit():
    numero_int = int(numero)
    par_impar = numero_int % 2
    if par_impar == 0:
        print("Numerpo par")
    else:
        print("numero Impar")
else:
    print("O numero fornecido não é inteiro")


# --------------------------------------------

# hora = input("Digite um horario: ")

# hora_int = int(hora)

# if hora_int <= 11:
#     print("Bom dia")
# elif hora_int >= 18:
#     print("Boa noite")
# else:
#     print("Boa tarde")

#  ---------------------------

# nome = input("Digite seu nome: ")

# if len(nome)<= 4:
#     print("Nome curto")
# elif len(nome) > 7:
#     print("Seu nome é grande")
# else:
#     print("Seu nome é normal")
